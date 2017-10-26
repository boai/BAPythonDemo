import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

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

# mail_title = 'Email test by Python'
# mail_content = """
# <p>Python 邮件发送测试【内容HTML 格式】...</p>
# <p><a href="https://www.baidu.com">这是一个链接</a></p>
# """
#
# demo_smtp.ba_smtp_sendEmail(mail_title, mail_content, 'html', sender, receivers, mail_host, mail_user, mail_pwd)
#


# 创建一个带附件的实例
message = MIMEMultipart()
message['From'] = Header("菜鸟教程", 'utf-8')
message['To'] = Header("测试", 'utf-8')
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

# 邮件正文内容
message.attach(MIMEText('这是菜鸟教程Python 邮件发送测试……', 'plain', 'utf-8'))

# 构造附件1，传送当前目录下的 test.txt 文件
att1 = MIMEText(open('test.txt', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="test.txt"'
message.attach(att1)

# 构造附件2，传送当前目录下的 runoob.txt 文件
att2 = MIMEText(open('test.txt', 'rb').read(), 'base64', 'utf-8')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="runoob.txt"'
message.attach(att2)

try:
    # 启用SSL发信, 端口一般是465
    smtpObj = smtplib.SMTP_SSL(mail_host, 465)
    # 登录验证
    smtpObj.login(mail_user, mail_pwd)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print("Error: 无法发送邮件")
    print(e)