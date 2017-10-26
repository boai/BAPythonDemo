
import demo_smtp

# 第三方 SMTP 服务
# SMTP服务器
mail_host = 'smtp.qq.com'
# 用户名
mail_user = '137361770@qq.com'
# 授权密码，非登录密码
mail_pwd = 'twmryjnhaigabjde'

# 发件人邮箱(最好写全, 不然会失败)
sender = '137361770@qq.com'
# 接收邮件，可设置为你的QQ邮箱或者其他邮箱
# receivers = ['sunboyan@outlook.com', '1299625033@qq.com']
receivers = ['sunboyan@outlook.com']

mail_title = 'Email test by Python'
mail_content = """
<p>Python 邮件发送测试【测试发送附件】...</p>
<p><a href="https://www.baidu.com">这是一个链接</a></p>
"""

demo_smtp.ba_smtp_sendEmail(mail_title, mail_content, 'html', sender, receivers, mail_host, mail_user, mail_pwd)

# demo_smtp.ba_smtp_sendEmail_attach(mail_title, mail_content, 'plain', sender, receivers, mail_host, mail_user, mail_pwd)

