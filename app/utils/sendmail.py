import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from ..templates.email_templates.emailtemaples import Template
from ..common.common import DEFAULT_FROM_EMAIL, HOST_SMTP_USERNAME, HOST_SMTP_SERVER, HOST_SMTP_PASSWORD, HOST_SMTP_PORT


def email_type(subject, msg):
    if subject == 'GebreKoo Email':
        return Template.verify_email(msg)
    elif subject == 'welcome':
        return Template.verify_user(msg)


class Email:
    def sendEmail(receiver_email, subject, msg):
        # HTML content
        # Create the email message
        email_message = MIMEMultipart()
        email_message['From'] = DEFAULT_FROM_EMAIL
        email_message['To'] = receiver_email
        email_message['Subject'] = subject

        # Attach HTML content
        email_message.attach(MIMEText(email_type(subject, msg), 'html'))
        # email_message.attach(MIMEText(message, 'plain'))

        try:
            # Create an SMTP connection
            smtp_connection = smtplib.SMTP(HOST_SMTP_SERVER, HOST_SMTP_PORT)
            smtp_connection.starttls()
            smtp_connection.login(HOST_SMTP_USERNAME, HOST_SMTP_PASSWORD)

            # Send the email
            smtp_connection.sendmail(
                DEFAULT_FROM_EMAIL, receiver_email, email_message.as_string())

            print("Email sent successfully!")
            return True

        except smtplib.SMTPException as e:
            print("Error occurred while sending the email:", str(e))
            return False

        finally:
            # Close the SMTP connection
            smtp_connection.quit()
