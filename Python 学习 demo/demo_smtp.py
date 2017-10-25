
import smtplib

from email.header import Header
from email.mime.text import MIMEText

# 第三方 SMTP 服务
# SMTP服务器
mail_host = 'smtp.qq.com'
# 用户名
mail_user = '137361770@qq.com'
# 授权密码，非登录密码
mail_pwd = 'qhbibauvewgebjbi'

# 发件人邮箱(最好写全, 不然会失败)
sender = '137361770@qq.com'
# 接收邮件，可设置为你的QQ邮箱或者其他邮箱
# receivers = ['sunboyan@outlook.com', '1299625033@qq.com']
receivers = ['sunboyan@outlook.com']

mail_title = 'Email test by Python'
mail_content = 'welcome to boaihome!'

def ba_smtp_sendEmail(email_title, email_content, email_sender, email_receiver, email_host, email_user, email_pwd):

    # 内容, 格式, 编码
    message = MIMEText(email_content, 'plain', 'utf-8')
    message['From'] = '{}'.format(email_sender)
    message['To'] = ','.join(email_receiver)
    message['Subject'] = email_title

    try:
        # 启用SSL发信, 端口一般是465
        smtpObj = smtplib.SMTP_SSL(email_host, 465)
        # 登录验证
        smtpObj.login(email_user, email_pwd)
        # 发送
        smtpObj.sendmail(email_sender, email_receiver, message.as_string())
        print('mail has been send successfully!')
    except smtplib.SMTPException as e:
        print("Error: 无法发送邮件")
        print(e)


if __name__ == '__main__':

    i = 0
    while i < 3:
        title = ('%s%d'%(mail_title, i))
        ba_smtp_sendEmail(title, mail_content, sender, receivers, mail_host,mail_user, mail_pwd)
        i += 1
    print('邮件发送完毕！结束循环！')

