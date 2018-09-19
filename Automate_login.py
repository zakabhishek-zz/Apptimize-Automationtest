import os
import uuid
from selenium import webdriver




chromedriver = "/Users/abhi-macbookpro/PycharmProjects/Apptimize_1/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://apptimize.com")
#driver.quit


register_btn=driver.find_element_by_xpath('//*[@id="nav-main"]/ul[2]/li[2]/a')

register_btn.click()

#Fill Form
first_name=driver.find_element_by_id('fname').send_keys('Abc')
last_name=driver.find_element_by_id('lname').send_keys('Xyz')
email_id=driver.find_element_by_id('email').send_keys('abc@gmail.com')
email = driver.find_element_by_id('email')
emailAdd = "abc+" + str(uuid.uuid4()) + "@gmail.com"
email.send_keys(emailAdd)


company=driver.find_element_by_id('company').send_keys('Apptimize Candidate')
phone=driver.find_element_by_id('phone').send_keys('123456789')
job_title=driver.find_element_by_id('jobtitle').send_keys('Intern')
password=driver.find_element_by_id('password').send_keys('terminator90!')
eula= driver.find_element_by_xpath('//*[@id="eula"]')
register_apptimize=driver.find_element_by_class_name('optanon-alert-box-button-container').click()


driver.get("http://apptimize.com")


#Login
sign_in=driver.find_element_by_xpath('//*[@id="nav-main"]/ul[2]/li[1]/a').click()
login_username=driver.find_element_by_id('zet-login-email').send_keys('abc@gmail.com')
login_password=driver.find_element_by_id('zet-login-password').send_keys('terminator90!')
login_btn=driver.find_element_by_id('zet-loginbtn').click()


#App creation
'''
driver.find_element_by_xpath('/html/body/div[3]/ng-view/div/div[3]/div/div/div/span[2]/em/a').send_keys('Jaggu-Dada')
driver.find_element_by_id('zet-new-feature-option-2').click()
driver.find_element_by_css_selector('#experiment-setup-view > div > div.main-zindex-context > div > div > div.setup-main > div > div > setup-footer > div > div > div > button').click()
driver.find_element_by_css_selector('//*[@id="experiment-setup-view"]/div/div[2]/div/div/div[2]/div/div/setup-footer/div/div/div/button').click()
''' #Not Sure about this part because we have to create an app first and then replicate the steps mentioned in the assignment. So I had to create the app first in order for the automation to work.



#Logout
logout_arrow=driver.find_element_by_xpath('//*[@id="zet-navbar-caretdown"]').click()
logout_signout=driver.find_element_by_xpath('//*[@id="zet-navbar-signout"]').click()

driver.close()