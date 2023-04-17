import csv
import random
import email_validator
from faker import Faker

def generate_email():
    # Generate a random email address
    fake = Faker()
    first_name = fake.first_name().lower()
    last_name = fake.last_name().lower()
    domain = random.choice(['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com'])
    username = f"{first_name}{last_name}{random.randint(1, 500)}"
    email = f"{username}@{domain}"
    return email

def generate_authenticated_emails(num_emails):
    # Generate a list of authenticated email addresses
    emails = []
    for i in range(num_emails):
        email = generate_email()
        try:
            # Validate the email address using email_validator library
            email_validator.validate_email(email, check_deliverability=True)
            emails.append(email)
            print(f"Added email: {email}")
        except email_validator.EmailNotValidError:
            # Ignore invalid email addresses
            print(f"Ignored invalid email: {email}")
            pass
    # Remove duplicates from the list of emails
    emails = list(set(emails))
    return emails

def write_emails_to_csv(filename, emails):
    # Write the emails to a CSV file
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for email in emails:
            writer.writerow([email])

