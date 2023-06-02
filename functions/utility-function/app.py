import base64
import hashlib
import hmac
import logging
import os

from crhelper import CfnResource
from argon2 import PasswordHasher

logger = logging.getLogger(__name__)
helper = CfnResource(json_logging=False, log_level="DEBUG", boto_level="CRITICAL")

try:
    pass
except Exception as e:
    helper.init_failure(e)


@helper.create
@helper.update
def create(event, context):
    helper.Data["SmtpPassword"] = smtp_password(
        event["ResourceProperties"]["SecretAccessKey"]
    )
    helper.Data["AdminToken"] = argon2_phc(
        event["ResourceProperties"]["Token"]
    )
    return "Utility"


@helper.delete
def delete(event, context):
    return None


def smtp_password(secret_access_key):
    signature = sign(
        (f"AWS4{secret_access_key}").encode("utf-8"),
        "11111111",
    )
    signature = sign(signature, os.environ["AWS_REGION"])
    signature = sign(signature, "ses")
    signature = sign(signature, "aws4_request")
    signature = sign(signature, "SendRawEmail")
    signature_and_version = bytes([0x04]) + signature
    password = base64.b64encode(signature_and_version)
    return password.decode("utf-8")


def sign(key, msg):
    return hmac.new(key, msg.encode("utf-8"), hashlib.sha256).digest()


def argon2_phc(token):
    ph = PasswordHasher(time_cost=2, memory_cost=19456, parallelism=1)
    return ph.hash(token)


def handler(event, context):
    helper(event, context)
