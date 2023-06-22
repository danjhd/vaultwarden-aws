import boto3
import json
import logging
import os
import time
import shutil
from botocore.exceptions import ClientError


def lambda_handler(event, context):
    timestr = time.strftime("%Y%m%d-%H%M%S")
    shutil.make_archive(f'/tmp/{timestr}', 'zip', '/mnt/efs')
    upload_file(f"/tmp/{timestr}.zip", f"{os.environ['BackupBucket']}")
    return None


def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True