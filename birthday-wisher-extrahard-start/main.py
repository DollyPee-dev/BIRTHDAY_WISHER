##################### Extra Hard Starting Project ######################
from smtplib import *
import pandas as pd
import datetime as dt
import random
import os

#  Check if today matches a birthday in the birthdays.csv

data = pd.read_csv("birthday-wisher-extrahard-start/birthdays.csv")
now = dt.datetime.now()

my_email = os.environ.get("EMAIL")
my_password = os.environ.get("PASSWORD")

today_matches = data[
    (data["month"] == now.month) & (data["day"] == now.day)
].to_dict(orient="records")

if today_matches:

    with SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)

        for person in today_matches:
            name = person["name"]
            email = person["email"]

            birthday_text = f"birthday-wisher-extrahard-start/letter_templates/letter_{random.randint(1,5)}.txt"

    #
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

            with open(birthday_text) as file_data:
                text = file_data.read().replace("[NAME]", name)

# 4. Send the letter generated in step 3 to that person's email address.

            connection.sendmail(
                from_addr=my_email,
                to_addrs= email,
                msg=f"Subject: Happy Birthday {name} \n\n {text}"
            )



