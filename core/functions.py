import re

from core.models import User


def create_dummy_users(**kwargs):
    user_emails = ["arun@gmail.com", "binks@gmail.com",
                   "sam@gmail.com", "tim@gmail.com", "raj@gmail.com",
                   "george@gmail.com", "christopher@gmail.com", "confluence@gmail.com",
                   "sundar@gmail.com", "bai@gmail.com", "peter@gmail.com", "bill@gmail.com"]
    for user_email in user_emails:
        if not User.objects.filter(email=user_email).exists():
            if re.search(r'[a-zA-Z0-9]+', user_email).group() == "sangeeth":
                user_obj = User.objects.create_superuser(email=user_email,
                                                         password=re.search(r'[a-zA-Z0-9]+', user_email).group())
            else:

                user_obj = User.objects.create_user(email=user_email,
                                                    password=re.search(r'[a-zA-Z0-9]+', user_email).group())

    return True
