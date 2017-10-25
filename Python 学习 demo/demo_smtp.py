
import smtplib

from email.header import Header
from email.mime.text import MIMEText
# 发送带附件的邮件 需要导入的头文件
from email.mime.multipart import MIMEMultipart
# HTML 文本中添加图片
from email.mime.image import MIMEImage

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

'''
email_title：邮件标题
email_content：邮件内容
email_type：邮件类型，例如：纯中文内容传'plain'，如果是 HTML 标签传'html'
email_sender：发送者
email_receiver：接收者
email_host：第三方 SMTP 服务，例如：'smtp.qq.com'
email_user：主发送方
email_pwd：授权密码，非登录密码
'''
def ba_smtp_sendEmail(email_title, email_content, email_type, email_sender, email_receiver, email_host, email_user, email_pwd):

    # 内容, 格式, 编码
    message = MIMEText(email_content, email_type, 'utf-8')
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
        print('邮件发送成功!')
    except smtplib.SMTPException as e:
        print("Error: 无法发送邮件")
        print(e)

def ba_smtp_sendEmail_htmlImage(email_title, email_content, email_type, email_sender, email_receiver, email_host, email_user, email_pwd):
    msgRoot = MIMEMultipart('related')
    msgRoot['From'] = Header("W3Cschool教程", 'utf-8')
    msgRoot['To'] = Header("测试", 'utf-8')
    subject = 'Python SMTP 邮件测试'
    msgRoot['Subject'] = Header(subject, 'utf-8')

    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)

    mail_msg = """
    <p>Python 邮件发送测试...html 图片</p>
    <p><a href="http://www.baidu.com">博爱链接</a></p>
    <p>图片演示：</p>
    <p><img src="cid:image1"></p>
    """
    msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))

    # 指定图片为当前目录
    fp = open('02_1600x900.jpg', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    # 定义图片 ID，在 HTML 文本中引用
    msgImage.add_header('Content-ID', '<image1>')
    msgRoot.attach(msgImage)

    try:
        # 启用SSL发信, 端口一般是465
        smtpObj = smtplib.SMTP_SSL(email_host, 465)
        # 登录验证
        smtpObj.login(email_user, email_pwd)
        # 发送
        smtpObj.sendmail(email_sender, email_receiver, msgRoot.as_string())
        print('邮件发送成功!')
    except smtplib.SMTPException as e:
        print("Error: 无法发送邮件")
        print(e)


def ba_smtp_sendEmail_attach(email_title, email_content, email_type, email_sender, email_receiver, email_host, email_user, email_pwd):

    # 创建一个带附件的实例
    message = MIMEMultipart()
    # message['From'] = '{}'.format(email_sender)
    message['From'] = Header('FROM TEST', 'utf-8')
    # message['To'] = ','.join(email_receiver)
    message['To'] = Header('sunboyan@outlook.com', 'utf-8')
    # message['Subject'] = email_title
    message['Subject'] = Header('TITLE', 'utf-8')

    # 邮件正文内容
    message.attach(MIMEText('CONTENT TEST', email_type, 'utf-8'))

    # 构造附件1，传送当前目录下的 test.txt 文件
    att1 = MIMEText(open('test.txt', 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename="test.txt"'
    message.attach(att1)

    try:
        # 启用SSL发信, 端口一般是465
        smtpObj = smtplib.SMTP_SSL(email_host, 465)
        # 登录验证
        smtpObj.login(email_user, email_pwd)
        # 发送
        smtpObj.sendmail(email_sender, email_receiver, message.as_string())
        print('邮件发送成功!')
    except smtplib.SMTPException as e:
        print("Error: 无法发送邮件")
        print(e)


if __name__ == '__main__':

    # i = 0
    # while i < 2:
    #     title = ('%s%d'%(mail_title, i))
    #     ba_smtp_sendEmail(title, mail_content, 'plain', sender, receivers, mail_host,mail_user, mail_pwd)
    #     i += 1
    # print('邮件发送完毕！结束循环！')

    ba_smtp_sendEmail_htmlImage(mail_title, mail_content, 'html', sender, receivers, mail_host, mail_user, mail_pwd)


