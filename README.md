# VaultWarden on AWS

This solution deploys the [VaultWarden](https://github.com/dani-garcia/vaultwarden) solution on AWS using ECS, Fargate and EFS.

## Pre requisities

- An AWS ACM Public SSL Certificate for the Domain to be used.
- AWS SES configured to be able to send from one validated email address
- [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)
- Docker Desktop (or Python 3.10 available locally)

## Deployment

```bash
# If you have Docker Desktop
sam build -u
# If you have Python 3.10 running locally
sam build
```

```bash
sam deploy --guided
# Follow the prompts and supplied the requested values
```

## Access

Once the SAM CLI has completed the deployment you will see two outputs:

```txt
----------------------------------------------------------------------------------------------
Outputs
----------------------------------------------------------------------------------------------
Key                 LoadBalancerDNSName
Description         -
Value               xxxxxxxxxxxxxxxxxxxxxxxxx.elb.amazonaws.com

Key                 AdminTokenSecretId
Description         -
Value               arn:aws:secretsmanager:XX-XXXX-X:XXXXXXXXXXXX:secret:AdminToken-XXXXXXXXXX
----------------------------------------------------------------------------------------------
```

Create a new CNAME entry in your DNS provider using the `LoadBalancerDNSName` value and the DomainName you chose.

Once DNS has been propogated you should be able to access the Web Interface at:
https://{DOMAINNAME}

### Admin Panel

The Admin Panel of VaultWarden is blocked by the WAF deliberately.

Access can be gained at `http://{ecs task private IP}/admin`

The Admin Token can be found in Secrets Manager, the Secret Arn is shown in the `AdminTokenSecretId` output.

> **Note**: To gain access you will need to do so from a resource that has private IP access and update the ECS security group.
