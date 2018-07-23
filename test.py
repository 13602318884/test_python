#-- coding: utf-8 --   #注意这里不能写成 coding = utf-8，不然会报错，要写成   -- coding: utf-8 --
from selenium import webdriver
import time

#以下三个依赖包为发送测试报告邮件需要的
import smtplib
from email.mime.text import MIMEText
from email.header import Header

#访问测试环境
driver=webdriver.Firefox()
driver.get("http://192.168.10.99:8082/login")
driver.maximize_window()

#定位账号输入框并且填入登录用户名
driver.find_element_by_id('t_UserName').send_keys('teacher@simpleware.com.cn')
time.sleep(1)

#定位密码输入框并且输入登录密码
driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/form/div[3]/input').send_keys('123456')
time.sleep(1)

#定位登录按钮，定价登录
driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/form/div[4]/input').click()
time.sleep(3)

#将页面滚动条拖到底部
js="var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
time.sleep(3)

#将滚动条移动到页面的顶部
js_="var q=document.documentElement.scrollTop=0"
driver.execute_script(js_)
time.sleep(3)

#点击学校首页
driver.find_element_by_xpath('/html/body/div/div[2]/ul/li[1]/a').click()
time.sleep(2)

#点击在线实验
driver.find_element_by_xpath('/html/body/div/div[2]/ul/li[2]/a').click()
time.sleep(2)

#点击技能竞赛
driver.find_element_by_xpath('/html/body/div/div[2]/ul/li[3]/a').click()
time.sleep(5)
#将句柄切换到新打开的页面，然后关闭
windows = driver.window_handles
driver.switch_to.window(windows[1])

#关闭当前页面
driver.close()
time.sleep(2)
#driver.quit()#关闭所有页面

#想切换回当前原有页面继续进行下面操作需要加入这一句
driver.switch_to.window(windows[0])
time.sleep(2)

#点击专业体系
driver.find_element_by_xpath('/html/body/div/div[2]/ul/li[4]/a').click()
time.sleep(2)

#点击帮助中心
driver.find_element_by_xpath('/html/body/div/div[2]/ul/li[5]/a').click()
time.sleep(3)

#拖动到可见的位置
target = driver.find_element_by_xpath("/html/body/div/div[3]/div[3]/div[1]/div[2]/p[9]/img")
driver.execute_script("arguments[0].scrollIntoView();", target)


# #以下为配置报告发送到邮箱的代码部分
#
#发送html格式的邮件
#发送邮箱
sender = "410860291@qq.com"
# 接收邮箱
receiver = "410860291@qq.com"
# 发送邮件主题
subject = "自动化测试"
# 发送邮箱服务器
smtpserver = "smtp.qq.com"
# 发送邮箱用户/密码
username = "410860291@qq.com"
password = "speelacvqspucbbe"

# HTML形式的邮件
msg = MIMEText("<html><h1>This Test Report!</h1></html>", "html", "utf-8")
msg["Subject"] = Header(subject, "utf-8")

smtp = smtplib.SMTP_SSL(smtpserver, 465)
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
# #以上代码是配置邮箱
