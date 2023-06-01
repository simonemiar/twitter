from bottle import request
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_verification_email(user_verification_key, user_email):
        print(user_email)

        sender_email = "simonemiaa@gmail.com"
        receiver_email = "pobiv67582@ratedane.com"
        password = "zatovtlritcjgxfq"

        message = MIMEMultipart("alternative")
        message["Subject"] = "multipart test"
        message["From"] = sender_email
        message["To"] = receiver_email

        # Create the plain-text and HTML version of your message
        text = """\
        Hi,
        How are you?
        www.your_website_here.com"""
        html = f"""\
        <html>
            <body>
            <p>Hi,<br>
                Thank you for signing up?<br>

                <a href="http://127.0.0.1:5000/verified/{user_verification_key}">YOUR WEBSITE HERE</a>
            </p>
            </body>
        </html>
        """
        # Change above url to pythonanywhere
        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )

        return 