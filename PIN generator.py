from selenium import webdriver
import time
import pyautogui as pag

pw='Input Password'
newpw='Input new Password'
URL='https://demo.hancomwith.com:9443/anysign/issue.html#'

options = webdriver.ChromeOptions()
options.add_argument('window-size=1920,1080')


driver = webdriver.Chrome('chromedriver', options=options)
driver.implicitly_wait(20)


driver.get(url=URL)


#for i in range(2):
driver.find_element_by_xpath('//*[@id="header"]/ul/li[2]/a').click()
driver.find_element_by_xpath('//*[@id="div-content-pin"]/div[2]/form[2]/fieldset/dl/dd[1]/a').click()
#time.sleep(1)
driver.find_element_by_xpath('//*[@id="div-content-pin"]/div[2]/form[2]/fieldset/div/a[1]').click()
driver.find_element_by_xpath('//*[@id="apn_regist_new_pw"]').send_keys(pw)
driver.find_element_by_xpath('//*[@id="apn_regist_chk_pw"]').send_keys(pw)
driver.find_element_by_xpath('//*[@id="AnyPIN"]/div/div[9]/button').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/a').click()
driver.find_element_by_xpath('//*[@id="header"]/h1/a').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="intro"]/div/ul/li[2]/a').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="login-area"]/div[1]/ul/li[2]').click()
time.sleep(2) 
driver.find_element_by_xpath('//*[@id="apn_ori_pw"]').send_keys(pw)
driver.find_element_by_xpath('//*[@id="AnyPIN"]/div/div[9]/button').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="header"]/h1/a').click()
driver.find_element_by_xpath('//*[@id="intro"]/div/ul/li[3]/a').click()
driver.find_element_by_xpath('//*[@id="accordion"]/div[2]/div[1]/h4/a').click()
driver.find_element_by_xpath('//*[@id="apn_ori_pw"]').send_keys(pw)
driver.find_element_by_xpath('//*[@id="AnyPIN"]/div/div[9]/button').click()
driver.find_element_by_xpath('//*[@id="apn_change_new_pw"]').send_keys(newpw)
driver.find_element_by_xpath('//*[@id="apn_change_chk_pw"]').send_keys(newpw)
driver.find_element_by_xpath('//*[@id="AnyPIN"]/div/div[9]/button').click()
time.sleep(1)
pag.press('enter')
driver.find_element_by_xpath('//*[@id="pin-delete"]').click()
driver.find_element_by_xpath('//*[@id="apn_chk_box"]').click()
driver.find_element_by_xpath('//*[@id="apn_ori_pw"]').send_keys(newpw)
driver.find_element_by_xpath('//*[@id="AnyPIN"]/div/div[9]/button').click()
time.sleep(1)
pag.press('enter')
