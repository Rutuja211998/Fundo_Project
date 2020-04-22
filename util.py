import re


def validate_email(email):  # validation for email is checked here by using regex

    email = email
    pattern = "^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$"
    x = re.search(pattern, email)
    if (x):
        return True
    else:
        return False