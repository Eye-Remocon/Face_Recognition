import smtplib, base64
from email.mime.text import MIMEText

smtp_user = ""  # 입력된 "이메일:비밀번호"를 base64 형식으로 인코딩
# ex) 이메일이 "abcd1234@naver.com", 비밀번호가 "12345678"이라면 smtp_user = "YWJjZDEyMzRAbmF2ZXIuY29tOjEyMzQ1Njc4"
smtp_user_decode = base64.b64decode(smtp_user).decode("ASCII")  # base64를 디코딩을 통해 이메일:비밀번호 형식으로 변환

smtp_user_id = smtp_user_decode.split(":")[0]
smtp_user_pw = smtp_user_decode.split(":")[1]

smtp_info = dict({"smtp_server": "smtp.naver.com",  # SMTP 서버 주소
                  "smtp_user_id": smtp_user_id,
                  "smtp_user_pw": smtp_user_pw,
                  "smtp_port": 587})  # SMTP 서버 포트

# 메일 내용 작성
title = "긴급 상황 발생" # 예시 문구
content = "긴급 상황이 발생했습니다. 즉시 확인해 주시기 바랍니다." # 예시 문구
sender = "" # 보내는 사람의 이메일 주소
receiver = "" # 받는 사람의 이메일 주소

# 메일 객체 생성 : 메시지 내용에는 한글이 들어가기 때문에 한글을 지원하는 문자 체계인 UTF-8을 명시해줍니다.
msg = MIMEText(_text=content, _charset="utf-8")  # 메일 내용

msg['Subject'] = title     # 메일 제목
msg['From'] = sender       # 송신자
msg['To'] = receiver       # 수신자


def send_email():
    smtp_info = dict({"smtp_server": "smtp.naver.com",  # SMTP 서버 주소
                  "smtp_user_id": smtp_user_id,
                  "smtp_user_pw": smtp_user_pw,
                  "smtp_port": 587})  # SMTP 서버 포트
    
    msg = MIMEText(_text=content, _charset="utf-8")  # 메일 내용

    msg['Subject'] = title     # 메일 제목
    msg['From'] = sender       # 송신자
    msg['To'] = receiver       # 수신자
    
    with smtplib.SMTP(smtp_info["smtp_server"], smtp_info["smtp_port"]) as server:
        server.starttls()
        server.login(smtp_info["smtp_user_id"], smtp_info["smtp_user_pw"])
        response = server.sendmail(msg['from'], msg['to'], msg.as_string())
        
        if not response:
            print('이메일을 성공적으로 보냈습니다.')
        else:
            print(response)
