import smtplib
from email.mime.text import MIMEText


def send_email(smtp_info, msg):
    with smtplib.SMTP(smtp_info["smtp_server"], smtp_info["smtp_port"]) as server:
        # TLS connect
        server.starttls()
        # login
        server.login(smtp_info["smtp_user_id"], smtp_info["smtp_user_pw"])

        # send email
        response = server.sendmail(msg['from'], msg['to'], msg.as_string())

        # successfully send email --> result = {}
        if not response:
            print('Email has been sent successfully')
        else:
            print(response)


def send_notification(param):
    smtp_info = dict({"smtp_server": "smtp.naver.com",  # SMTP server address
                  "smtp_user_id": smtp_user_id,
                  "smtp_user_pw": smtp_user_pw,
                  "smtp_port": 587})  # SMTP server port

    title = param[0]
    content = param[1]
    sender = smtp_user_id
    receiver = param[2]

    msg = MIMEText(_text=content, _charset="utf-8")
    msg['Subject'] = title
    msg['From'] = sender
    msg['To'] = receiver

    send_email(smtp_info, msg)

