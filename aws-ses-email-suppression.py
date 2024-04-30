

import subprocess, json
from rich.console import Console
from rich.table import Table

available_regions = ["af-south-1", "ap-east-1", "ap-south-2", "ap-southeast-3", "ap-southeast-4", "ap-south-1", "ap-northeast-3", "ap-northeast-2", "ap-southeast-1", "ap-southeast-2", "ap-northeast-1", "us-gov-east-1", "us-gov-west-1", "ca-central-1", "ca-west-1", "cn-north-1", "cn-northwest-1", "eu-central-1", "eu-west-1", "eu-west-2", "eu-south-1", "eu-west-3", "eu-south-2", "eu-north-1", "eu-central-2", "il-central-1", "me-south-1", "me-central-1", "sa-east-1", "us-east-1", "us-east-2", "us-west-1", "us-west-2"]

all_responses = {}

# # Prompt the user to input the AWS region
region = input("Enter the AWS region (e.g., us-west-2): ")

def get_emails():
    # Prompt the user to input a list of email addresses separated by commas
    email_input = str(input("Enter a list of email addresses separated by commas: ")).strip().split(",")
    print()
    return set(email_input)

if region in available_regions:
    # # Prompt the user to choose between listing suppressed email addresses and deleting them
    choice = input("Enter 'list' to list suppressed email addresses or 'delete' to delete them: ").lower()

    if choice == 'list':
        email_input = get_emails()
        for email in email_input:
            print("<-- Listing for user:", email, " -->")
            get_emails_cmd = "aws sesv2 get-suppressed-destination --output json --region " + region + " --email-address " + str(email)
            result = subprocess.run(get_emails_cmd, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                response = json.loads(result.stdout)
                Reason,LastUpdateTime = response['SuppressedDestination']['Reason'], response['SuppressedDestination']['LastUpdateTime']
                all_responses[email] = [Reason,LastUpdateTime]
                # print("\nCommand executed successfully")
            else:
                Reason,LastUpdateTime = ["-", "-"]
                all_responses[email] = [Reason,LastUpdateTime]
                # print("\nError executing command")

        # Create a table instance
        table = Table(title="Suppressed Email Addresses List")
        table.add_column("EmailAddress")
        table.add_column("Reason")
        table.add_column("LastUpdateTime")

        # Add data to the table
        for key, value in all_responses.items():
            table.add_row(key, value[0], value[1])
        
        # Print the table
        console = Console()
        console.print(table)

    elif choice == 'delete':
        email_input = get_emails()

        # Following loop will iterate through each email and deletes them using AWS rest API call

        for email in email_input:
            print("\n<-- Deleting user: ", email, " -->")
            get_emails_cmd = "aws sesv2 delete-suppressed-destination --output json --region " + region + " --email-address " + str(email)
            subprocess.run(get_emails_cmd, shell=True)
            print("\n<-- Deleted user: ", email, " -->")

        # Again iterating to validate the emails have been deleted
        print("\n================================\n")
        print("Deletion completed, again iterating to validate the emails have been deleted !")

        for email in email_input:
            get_emails_cmd = "aws sesv2 get-suppressed-destination --region " + region + " --email-address " + str(email)
            subprocess.run(get_emails_cmd, shell=True)

        
    else:
        print("Invalid choice. Please enter 'list' or 'delete'.")
else:
    print("You have entered a wrong region. please select the correct region !!\nexiting script ....")
    exit()