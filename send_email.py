# Python code to illustrate sending email from
import smtplib
# Create SMTP Session
s = smtplib.SMTP('smtp-mail.outlook.com', 587)
# start TSL for security
s.starttls()
# Authentication
s.login("yourmail@hotmail.com", "pass123")
# message to be send
SUBJECT = "Subject - Title - Developer - Test"   
TEXT = "Send a Message using Python and smtplib"
message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
# sending the email
s.sendmail("yourmail@hotmail.com", "mailto@hotmail.com", message)
# terminating the session
s.quit()