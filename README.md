# VaultWarden on AWS

This solution deploys the [VaultWarden](https://github.com/dani-garcia/vaultwarden) solution on AWS using ECS, Fargate and EFS.

## Pre requisities

- AWS VPC with:
  - 3 x Public Subnets (default route Internet Gateway), in 3 difference  AZs
  - 3 x Private Subnets (default route NAT Gateway), in 3 difference  AZs
  - 1 x ECS Cluster configured for Fargate
  - 1 x ACM Public SSL Certificate for the Domain to be used.
  - SES configured to be able to send from one validated email address
  - 1 x S3 Bucket (for Load Balancer logs) - requires [S3 Bucket Policy](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/enable-access-logging.html) with prefix value of `vaultwarden-alb`

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

### Admin Panel

The Admin Panel of VaultWarden is blocked by the WAF deliberately.

Access can be gained at `http://{ecs task private IP}/admin`

> **Note**: To gain access you will need to do so from a resource that has private IP access and update the ECS security group.
