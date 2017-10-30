import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


class my_mail():
    def __init__(self, text, my_user):
        self.my_sender = 'xx'  # 发件人邮箱账号
        self.my_pass = 'xx'  # 发件人邮箱密码(当时申请smtp给的口令)
        self.my_user = my_user  # 收件人邮箱账号，我这边发送给自己
        self.text = text

    def mail(self):
        ret = True
        try:
            msg = MIMEText(self.text, 'plain', 'utf-8')
            msg['From'] = formataddr(["自己", self.my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            msg['To'] = formataddr(["自己啦", self.my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            msg['Subject'] = "动漫更新"  # 邮件的主题，也可以说是标题

            server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是465
            server.login(self.my_sender, self.my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(self.my_sender, [self.my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
        except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
            ret = False
        return ret

    def run(self):
        ret = self.mail()
        if ret:
            print("邮件发送成功")
        else:
            print("邮件发送失败")

if __name__ == '__main__':
    mail = my_mail('aa')
    mail.run()
