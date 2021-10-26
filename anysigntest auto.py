from selenium import webdriver
import time
import pyautogui as pag


pw='Input Your Password'
URL='https://reaver.softforum.com/up/anySign/test/'

options = webdriver.ChromeOptions()
#options.add_argument('window-size=1920,1080')

driver = webdriver.Chrome('chromedriver', options=options)
driver.implicitly_wait(5)

driver.get(url=URL)
driver.find_element_by_xpath('//*[@id="form_SignDataCMS"]/table/tbody/tr[7]/td[2]/input[1]').click()
driver.find_element_by_xpath('//*[@id="xTsign_tab1_img"]').click()
driver.find_element_by_xpath('//*[@id="xwup_media_hdd"]/span[1]').click()
time.sleep(1)
driver.find_element_by_id('certselect_tk1').click()
pag.typewrite(pw)
driver.find_element_by_xpath('//*[@id="xwup_OkButton"]').click()



