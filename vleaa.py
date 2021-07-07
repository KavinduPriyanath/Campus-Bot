from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

j = 0 #variable to control scrolling 

def execute():
	PATH = "D:\chdriver\chromedriver.exe"
	driver = webdriver.Chrome(PATH)

	driver.maximize_window()	
	driver.get("https://ugvle.ucsc.cmb.ac.lk/login/index.php")

	my_name = "" #username
	my_pass = "" #password

	username = driver.find_element_by_name("username")
	password = driver.find_element_by_name("password")

	username.send_keys(my_name)
	password.send_keys(my_pass)
	password.send_keys(Keys.RETURN)

	enh = driver.find_element_by_link_text("ENH1201") #Enhancement
	enh.click()
	time.sleep(1)
	for i in range(1, 10):
		driver.execute_script("window.scrollTo("+str(j)+","+str(j+500 * i)+")")
		time.sleep(1)
	driver.back()

	cs1201 = driver.find_element_by_link_text("SCS1201") #Data Structures and Algorithms
	cs1201.click()
	time.sleep(1)
	for i in range(1, 10):
		driver.execute_script("window.scrollTo("+str(j)+","+str(j+500 * i)+")")
		time.sleep(1)
	driver.back()

	cs1202 = driver.find_element_by_link_text("SCS1202") #C Programming
	cs1202.click()
	time.sleep(1)
	for i in range(1, 10):
		driver.execute_script("window.scrollTo("+str(j)+","+str(j+500 * i)+")")
		time.sleep(1)
	driver.back()

	cs1203 = driver.find_element_by_link_text("SCS1203") #DataBases
	cs1203.click()
	time.sleep(1)
	for i in range(1, 10):
		driver.execute_script("window.scrollTo("+str(j)+","+str(j+500 * i)+")")
		time.sleep(1)
	driver.back()

	cs1204 = driver.find_element_by_link_text("SCS1204") #Discrete Mathematics
	cs1204.click()
	time.sleep(1)
	for i in range(1, 10):
		driver.execute_script("window.scrollTo("+str(j)+","+str(j+500 * i)+")")
		time.sleep(1)
	driver.back()

	cs1205 = driver.find_element_by_link_text("SCS1205") #Computer Systems
	cs1205.click()
	time.sleep(1)
	for i in range(1, 10):
		driver.execute_script("window.scrollTo("+str(j)+","+str(j+500 * i)+")")
		time.sleep(1)
	driver.back()

	cs1206 = driver.find_element_by_link_text("SCS1206") #Linux Systems
	cs1206.click()
	time.sleep(1)
	for i in range(1, 10):
		driver.execute_script("window.scrollTo("+str(j)+","+str(j+500 * i)+")")
		time.sleep(1)
	driver.back()

	cs1207 = driver.find_element_by_link_text("SCS1207") #Software Engineering
	cs1207.click()
	time.sleep(1)
	for i in range(1, 10):
		driver.execute_script("window.scrollTo("+str(j)+","+str(j+500 * i)+")")
		time.sleep(1)
	driver.back()

	driver.execute_script("window.scrollTo(0,0)")

	driver.quit()





