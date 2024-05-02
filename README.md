# AWS SESv2 Suppressed Email Addresses Manager

----------------------------------------------------------------------------------------------------------------------
## Overview
This Python script allows you to list suppressed email addresses or delete them from AWS SESv2 (Simple Email Service).
----------------------------------------------------------------------------------------------------------------------

--------------------------------
## Authors

- Pratik Joshi
- Shivam Bhanvadia
--------------------------------

-----------------------------------------------------------------------------------------------------------------------------------------
## Usage

### Prerequisites
Before using the script, make sure you have the following:

- Python 3 installed
- AWS CLI configured with appropriate permissions

### Authentication
Before running the script, you need to authenticate with AWS. If you're using Okta for authentication, run the following command in your terminal to set the appropriate role:

eval $(okta-aws-login)
-----------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------------------
### Running the Script
To use the script, run the aws-ses-email-suppression.py file with the appropriate command-line arguments.

#### List Suppressed Email Addresses
python3 aws-ses-email-suppression.py <region> --list "email1@example.com,email2@example.com"

#### Sample Output
+--------------------------+--------+----------------------------------+
| EmailAddress             | Reason | LastUpdateTime                   |
+--------------------------+--------+----------------------------------+
| abc@gmail.com            | NA     | 2022-04-20T25:00:31.293000+05:30 |
+--------------------------+--------+----------------------------------+
| def@gmail.com            | -      | -                                |
+--------------------------+--------+----------------------------------+
| xyz@gmail.com            | NA     | 2022-02-28T05:53:22.252000+05:30 |
+--------------------------+--------+----------------------------------+

### Delete Suppressed Email Addresses
python3 aws-ses-email-suppression.py <region> --delete "email3@example.com,email4@example.com"

#### Sample Output
Deleted user: email3@example.com
Deleted user: email4@example.com
---------------------------------------------------------------------------------------------------------


### Help Menu
You can also access the help menu to view the available options:
python script.py --help
