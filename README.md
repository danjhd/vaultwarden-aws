# VaultWarden on AWS

This solution deploys the [VaultWarden](https://github.com/dani-garcia/vaultwarden) solution on AWS using ECS, Fargate and EFS.

## Pre requisities

- AWS VPC with:
  - 3 x Public Subnets (default route Internet Gateway), in 3 difference  AZs
  - 3 x Private Subnets (default route NAT Gateway), in 3 difference  AZs
  - 1 x ECS Cluster configured for Fargate
  - 1 x ACM Public SSL Certificate for the Domain to be used.
  - SES configured to be able to send from one validated email address

- AWS CLI
- AWS SAM CLI
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

Key                 AdminToken
Description         -
Value               Xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
----------------------------------------------------------------------------------------------
```

Create a new CNAME entry in your DNS provider using the `LoadBalancerDNSName` value and the DomainName you chose.

Once DNS has been propogated you should be able to access the Web Interface at:
https://{DOMAINNAME}

The Admin Panel of VaultWarden can be accessed at:
https://{DOMAINNAME}/admin
You will be asked for a Admin Token when accessing this URL and for that you should supply the value of the `AdminToken` output.
