# run pip install qrcode pyotp

import pyotp
import qrcode
import time
#import myemail

########

import os
import smtplib
#import src.myotpgenerator
import myotpgenerator
#import src.mytotp
import mytotp
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv



def generate_totp():
    #key = "@LibossoIT"
    key = pyotp.random_base32()

    print(key)

    #totp = pyotp.TOTP('base32secret3232')
    #totp = pyotp.TOTP(key)
    totp = pyotp.TOTP(key, interval=600)
    totp.now() # => '492039'

    print(totp.now())

    rtotp=totp.now()

    #type(rtotp)

    print(f"this is the created rtotp {rtotp}")

    print(type(rtotp))

    return rtotp



def check_totp(user_totp,rtotp):

    if (user_totp == rtotp):
        print(f"Your OTP from mytotpgenerator is:  {rtotp} is valid")
    else:
        print(f"Your OTP from mytotpgenerator is:  {rtotp} is not valid")

    return user_totp



# Load environment variables from .env
load_dotenv()

# SMTP and Gmail credentials
SMTP_SERVER ="smtp.gmail.com"
SMTP_PORT =  587

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_email(recipient_email, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = recipient_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, recipient_email, msg.as_string())

        print("Email sent successfully ! ")
    except Exception as e:
        print(f"Error sending mail: {e}")

    return None
    

def totpCode(userEmail):


#if __name__ == "__main__":

    #recipient = "ericlibosso@gmail.com"
    recipient = userEmail
    subject = " Test Email from Python"
    body_totp = int("{totp}".format(otp = myotpgenerator.generate_otp(), totp = mytotp.generate_totp()))
    body = f""" Dear [Recipient’s Name],

        Thank you for signing up for [website/email list]. We’re excited to have you on board. Here are your account details: 

        Username: [Username]
        Password: selected password 

        Your bodyTOTP: {body_totp}

        You needn’t do anything at this point. Just enjoy your new account. Make sure to save this email for future reference.

        Thank you for once again registering for our [website/event]. In case of any questions, contact support at [support email address]. 

        Best regards,
        [Your Name], [Your Title]
        [Company Name] """
    
    send_email(recipient, subject, body)

    user_key = int (input(f"1. Enter the OTP Code you received:"))

    check_totp(user_key,body_totp)

    #check_totp = check_totp(user_key,body_totp)

    print("OTP SUBMITTED! ")

    #return user_key



if __name__ == "__main__":

    totpCode()
    
    