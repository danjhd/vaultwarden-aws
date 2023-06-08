# VaultWarden on AWS

This solution deploys the [VaultWarden](https://github.com/dani-garcia/vaultwarden) solution on AWS using ECS, Fargate and EFS.

## Pre requisities

- [AWS CLI](https://aws.amazon.com/cli/)
- Python > 3.7
- An AWS S3 bucket for the CloudFormation Assets to be uploaded to.
- An AWS ACM Public SSL Certificate for the Domain to be used.
- AWS SES configured to be able to send from one validated email address

## Deployment

```bash
aws cloudformation package --template-file template.yaml --s3-bucket {YOUR S3 BUCKET} --output-template-file packaged-template.yaml
```

> **Note**: Make sure to replace `{YOUR S3 BUCKET}` with the name of your own S3 bucket.

You can then navigate to the AWS CloudFormation console in the same region and deploy a new stack by specifying the `packaged-template.yaml` file that was just created/

## Access

Once the stack deployment is complete you will see two outputs:

- LoadBalancerDNSName
- AdminTokenSecretId

Create a new CNAME entry in your DNS provider using the `LoadBalancerDNSName` value and the DomainName you chose.

Once DNS has been propagated you should be able to access the Web Interface at:
https://{DOMAINNAME}

### Admin Panel

The Admin Panel of VaultWarden is blocked by the WAF deliberately.

Access can be gained at `http://{ecs task private IP}/admin`

The Admin Token can be found in Secrets Manager, the Secret Arn is shown in the `AdminTokenSecretId` output.

> **Note**: To gain access you will need to do so from a resource that has private IP access and update the ECS security group.
