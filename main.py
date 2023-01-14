import random
import smtplib
import datetime as dt

my_email = "janek.kowalski@gmail.com"
my_password = "password"

now = dt.datetime.now()
weekday =now.weekday()

if weekday ==0:
    with open("quotes.txt")as quotes_file:
        all_quotes = quotes_file.readline()
        quote = random.choice(all_quotes)

    with  smtplib.SMTP("smptp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="jan.kowalski@gamil.com",
            msg=f"Subject: Monday Motivation \n\n{quote}")
        connection.close()







