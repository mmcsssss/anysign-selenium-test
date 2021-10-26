from selenium import webdriver
import time
import pyautogui as pag


pw='Input Your Password'
URL='https://demo.hancomwith.com:9443/anysign/issue.html#'

options = webdriver.ChromeOptions()
options.add_argument('window-size=1920,1080')

driver = webdriver.Chrome('chromedriver', options=options)
driver.implicitly_wait(20)

driver.get(url=URL)
for i in range(0,1000):
	driver.find_element_by_xpath('//*[@id="div-content-certificate"]/div[2]/form[2]/fieldset/dl/dd[1]/a').click()
	driver.find_element_by_xpath('//*[@id="confirmBtn"]').click()
	driver.find_element_by_xpath('//*[@id="xwup_savepasswd_tek_input1"]').send_keys(pw)
	driver.find_element_by_xpath('//*[@id="xwup_savepasswd_tek_input2"]').send_keys(pw)
	driver.find_element_by_xpath('//*[@id="xwup_ok"]').click()
	driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/a').click()




