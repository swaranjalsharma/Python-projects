import re

email = input("Enter your email")

def is_valid_email(email):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._%+-]+\.[a-zA-Z]{2,}$'

    if re.match(email_pattern, email):
        return True
    else:
        return False
    
emails = ["test@example.com", "invalid-email", "another.testAdomain.org", "bad@domain", "good123@sub.domain.com", "arambhsharma2002@gmail.com"]
print(is_valid_email(email))