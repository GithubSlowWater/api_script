# _*_ coding:utf-8 _*_
# smtplib模块负责连接服务器和发送邮件
# MIMEText：定义邮件的文字数据
# MIMEImage：定义邮件的图片数据
# MIMEMultipart：负责将文字图片音频组装在一起添加附件
import smtplib  # 加载smtplib模块
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import os
import time 

sender = 'wsyceshi002@126.com'  # 发件人邮箱账号
receive = '568033067@qq.com'  # 收件人邮箱账号
passwd = 'KINGCHEN123'
mailserver = 'smtp.126.com'
port = '25'
sub = '区块链自动化测试报告'
file_dir = 'reports'
times = time.strftime('%Y-%m-%d_%H:%M:%S_',time.localtime())

# 返回附件文件名
def file_path(file_dir):
    for root, dirs, files in os.walk(file_dir):
        return files[0]

try:
    msg = MIMEMultipart('related')
    msg['From'] = formataddr(["sender", sender])  # 发件人邮箱昵称、发件人邮箱账号
    msg['To'] = formataddr(["receiver", receive])  # 收件人邮箱昵称、收件人邮箱账号
    msg['Subject'] = sub
    #文本信息
    #txt = MIMEText('this is a test mail', 'plain', 'utf-8')
    #msg.attach(txt)

    #附件信息
    attach = MIMEApplication(open("E:\\Python\\Httprunner\\BC\\reports\\" + file_path(file_dir), 'rb').read())
    attach.add_header('Content-Disposition', 'attachment', filename=times + 'ApiTest.html')
    msg.attach(attach)

    #正文显示图片
    body = """
    <b>本轮接口测试已完毕</b>
    <b>详细请看自动化测试报告:</b> 
    <br><img src="cid:image"><br>
    """
    text = MIMEText(body, 'html', 'utf-8')
    f = open('E:\\Kingsoft\\JX3HD\\bin\\zhcn_hd\\DCIM\\2018-08-17_22-46-49-000.jpg', 'rb')
    pic = MIMEImage(f.read())
    f.close()
    pic.add_header('Content-ID', '<image>')
    msg.attach(text)
    msg.attach(pic)


    server = smtplib.SMTP(mailserver, port)  # 发件人邮箱中的SMTP服务器，端口是25
    server.login(sender, passwd)  # 发件人邮箱账号、邮箱密码
    server.sendmail(sender, receive, msg.as_string())  # 发件人邮箱账号、收件人邮箱账号、发送邮件
    server.quit()
    print('邮件发送success')
except Exception as e:
        print(e)