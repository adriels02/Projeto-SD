import smtplib
from email.mime.text import MIMEText

def send_test_email():
    msg = MIMEText('This is a test email.')
    msg['Subject'] = 'Test Email'
    msg['From'] = 'bluelock.ifpe.ahmk@gmail.com'
    msg['To'] = 'filhosilvaalvesmurilo@gmail.com'

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login('bluelock.ifpe.ahmk@gmail.com', 'cvwj taub gnzf vddt')
            server.send_message(msg)
        print('Email sent successfully!')
    except Exception as e:
        print(f'Failed to send email: {e}')

send_test_email()
