import smtplib
from email.mime.text import MIMEText

def send_mail(content, email):
    msg_from = '1724647576@qq.com'  # 发送方邮箱
    passwd = 'ezdgvskeyvpvdbdh'  # 填入发送方邮箱的授权码
    msg_to = email
    subject = "点名"
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发送一般使用465端口，使用163邮箱的话，需要更换成smtp.163.com
        s.login(msg_from, passwd)
        s.sendmail(msg_from, msg_to, msg.as_string())
    except Exception as e:
        return 0
        print('error')
        return False
    else:
        return 1
        print('邮件发送成功')

    finally:
        s.quit()
    return True

if __name__ == '__main__':
    message = '测试'
    email = '1724647576@qq.com'
    send_mail(message, email)
