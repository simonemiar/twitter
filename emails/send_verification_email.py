from bottle import request
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_verification_email(user_verification_key, user_email):
        print(user_email)

        sender_email = "simonemiaa@gmail.com"
        receiver_email = user_email
        password = "zatovtlritcjgxfq"

        message = MIMEMultipart("alternative")
        message["Subject"] = "Verify your user"
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
                <h4>Thank you for signing up to Twitter</h4><br>
                <p>To finish signing up to twitter please<br>
                presh below link to verify your user. <br>
                Without verification you will not be able to login to your accout<br>
                <br>
                <a href="http://127.0.0.1:4000/verified/{user_verification_key}">Verify your user here</a><br>
                <br>
                /sincerely twitter
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