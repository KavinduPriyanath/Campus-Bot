from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "D:\chdriver\chromedriver.exe"

option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome(PATH,options=option) #run annonymously
#driver = webdriver.Chrome(PATH)

driver.get("https://ugvle.ucsc.cmb.ac.lk/login/index.php")

my_name = "" #username
my_pass = "" #password

username = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")

username.send_keys(my_name)
password.send_keys(my_pass)
password.send_keys(Keys.RETURN)

driver.get("https://ugvle.ucsc.cmb.ac.lk/calendar/view.php?view=upcoming")

upevent = driver.find_element_by_class_name("calendarwrapper")

def perform():
	print(upevent.text)


