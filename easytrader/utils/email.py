import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


class EmailSender:
    """QQ邮箱邮件发送类"""
    
    def __init__(self, sender_email: str, sender_auth_code: str):
        self.sender_email = sender_email
        self.sender_auth_code = sender_auth_code
        self.smtp_server = 'smtp.qq.com'
        self.smtp_port = 587
    
    def send(self, receiver_email: str, subject: str, content: str, is_html: bool = False) -> bool:
        """发送邮件"""
        try:
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = receiver_email
            msg['Subject'] = Header(subject, 'utf-8')
            msg.attach(MIMEText(content, 'html' if is_html else 'plain', 'utf-8'))
            
            smtp = smtplib.SMTP(self.smtp_server, self.smtp_port)
            smtp.starttls()
            smtp.login(self.sender_email, self.sender_auth_code)
            smtp.sendmail(self.sender_email, receiver_email, msg.as_string())
            smtp.quit()
            return True
        except Exception as e:
            print(f"发送邮件错误: {e}")
            return False


if __name__ == "__main__":
    SENDER_EMAIL = "xxx@qq.com"
    SENDER_AUTH_CODE = "xxx"
    RECEIVER_EMAIL = "xxx"
    
    email_sender = EmailSender(SENDER_EMAIL, SENDER_AUTH_CODE)
    email_sender.send(
        receiver_email=RECEIVER_EMAIL,
        subject="测试邮件",
        content="这是一封测试邮件，使用QQ邮箱发送。\n\n如果您收到此邮件，说明配置正确！"
    )
