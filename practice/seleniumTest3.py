from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Firefox()
#browser.get('http://mail.yahoo.com')
#emailElem = browser.find_element_by_id('login-username')
#emailElem.send_keys('not_my_real_email')
#passwordElem = browser.find_element_by_id('login-passwd')
#passwordElem.send_keys('12345')
#passwordElem.submit()
browser.get('http://mail.google.com')
emailElem = browser.find_element_by_id('Email')
logonEmail = 'rooneybb2'  #fill in your gmail name
emailElem.send_keys(logonEmail)
nextElem = browser.find_element_by_id('next')
nextElem.submit()
try: 
	element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "Passwd"))
                                                   )
	currentPage = browser.current_url
	print(currentPage)
	browser.get(currentPage)
	passwdElem = browser.find_element_by_id('Passwd')
	logonPw = '########'  #fill in your pw
	passwdElem.send_keys(logonPw)
	signInElem = browser.find_element_by_id('signIn')
	signInElem.submit()
	signInElem.send_keys(Keys.ENTER)
finally:
	#browser.quit()
        print("It Works!!!")


