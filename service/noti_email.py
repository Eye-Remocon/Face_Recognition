import smtplib, base64
from email.mime.text import MIMEText

smtp_user = ""  # 입력된 "이메일:비밀번호"를 base64 형식으로 인코딩
smtp_user_decode = base64.b64decode(smtp_user).decode("ASCII")  # base64를 디코딩을 통해 이메일:비밀번호 형식으로 변환

smtp_user_id = smtp_user_decode.split(":")[0]
smtp_user_pw = smtp_user_decode.split(":")[1]

smtp_info = dict({"smtp_server": "smtp.naver.com",  # SMTP 서버 주소
                  "smtp_user_id": smtp_user_id,
                  "smtp_user_pw": smtp_user_pw,
                  "smtp_port": 587})  # SMTP 서버 포트

# 메일 내용 작성
title = "python으로 이메일 보내기" # 예시 문구
content = "python으로 이메일 보내기 테스트" # 예시 문구
sender = "" # 보내는 사람의 이메일 주소
receiver = "" # 받는 사람의 이메일 주소

# 메일 객체 생성 : 메시지 내용에는 한글이 들어가기 때문에 한글을 지원하는 문자 체계인 UTF-8을 명시해줍니다.
msg = MIMEText(_text=content, _charset="utf-8")  # 메일 내용

msg['Subject'] = title     # 메일 제목
msg['From'] = sender       # 송신자
msg['To'] = receiver       # 수신자


def send_email(smtp_info, msg):
    with smtplib.SMTP(smtp_info["smtp_server"], smtp_info["smtp_port"]) as server:
        # TLS 보안 연결
        server.starttls()
        # 로그인
        server.login(smtp_info["smtp_user_id"], smtp_info["smtp_user_pw"])

        # 로그인 된 서버에 이메일 전송
        response = server.sendmail(msg['from'], msg['to'], msg.as_string())  # 메시지를 보낼때는 .as_string() 메소드를 사용해서 문자열로 바꿔줍니다.

        # 이메일을 성공적으로 보내면 결과는 {}
        if not response:
            print('이메일을 성공적으로 보냈습니다.')
        else:
            print(response)


send_email(smtp_info, msg)