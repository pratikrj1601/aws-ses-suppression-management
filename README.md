# AWS SESv2 Suppressed Email Addresses Manager

## Overview
This Python script allows you to list suppressed email addresses or delete them from AWS SESv2 (Simple Email Service).

## Authors

- Pratik Joshi
- Shivam Bhanvadia

## Usage

### Prerequisites
Before using the script, make sure you have the following:

- Python 3 installed
- AWS CLI configured with appropriate permissions

### Authentication
Before running the script, you need to authenticate with AWS. If you're using Okta for authentication, run the following command in your terminal to set the appropriate role:

```
eval $(okta-aws-login)
```

### Running the Script
To use the script, run the aws-ses-email-suppression.py file with the appropriate command-line arguments.

#### List Suppressed Email Addresses
```
python3 aws-ses-email-suppression.py <region> --list "email1@example.com,email2@example.com"
```

#### Sample Output
```
+--------------------------+--------+----------------------------------+
| EmailAddress             | Reason | LastUpdateTime                   |
+--------------------------+--------+----------------------------------+
| abc@gmail.com            | NA     | 2022-04-20T25:00:31.293000+05:30 |
+--------------------------+--------+----------------------------------+
| def@gmail.com            | -      | -                                |
+--------------------------+--------+----------------------------------+
| xyz@gmail.com            | NA     | 2022-02-28T05:53:22.252000+05:30 |
+--------------------------+--------+----------------------------------+
```

#### Delete Suppressed Email Addresses
```
python3 aws-ses-email-suppression.py <region> --delete "email3@example.com,email4@example.com"
```

#### Sample Output
```
Deleted user: email3@example.com
Deleted user: email4@example.com
```

### Help Menu
You can also access the help menu to view the available options:
python aws-ses-email-suppression.py --help

```
usage: aws-ses-email-suppression.py [-h] [--list EMAILS] [--delete EMAILS]
                                    {af-south-1,ap-east-1,ap-south-2,ap-southeast-3,ap-southeast-4,ap-south-1,ap-northeast-3,ap-northeast-2,ap-southeast-1,ap-southeast-2,ap-northeast-1,us-gov-east-1,us-gov-west-1,ca-central-1,ca-west-1,cn-north-1,cn-northwest-1,eu-central-1,eu-west-1,eu-west-2,eu-south-1,eu-west-3,eu-south-2,eu-north-1,eu-central-2,il-central-1,me-south-1,me-central-1,sa-east-1,us-east-1,us-east-2,us-west-1,us-west-2}

List suppressed email addresses or delete them from AWS SES v2

positional arguments:
  {af-south-1,ap-east-1,ap-south-2,ap-southeast-3,ap-southeast-4,ap-south-1,ap-northeast-3,ap-northeast-2,ap-southeast-1,ap-southeast-2,ap-northeast-1,us-gov-east-1,us-gov-west-1,ca-central-1,ca-west-1,cn-north-1,cn-northwest-1,eu-central-1,eu-west-1,eu-west-2,eu-south-1,eu-west-3,eu-south-2,eu-north-1,eu-central-2,il-central-1,me-south-1,me-central-1,sa-east-1,us-east-1,us-east-2,us-west-1,us-west-2}
                        AWS region

options:
  -h, --help            show this help message and exit
  --list EMAILS         List suppressed email addresses separated by commas
  --delete EMAILS       Delete suppressed email addresses separated by commas
```
