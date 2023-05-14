import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
options.binary_location = r"C:/Program Files/Mozilla Firefox/firefox.exe"
driver = webdriver.Firefox(options=options, executable_path=("C:/Users/Laca/Desktop/Suli/Szoftverteszt/teszt1/geckodriver"))

driver.get("http://127.0.0.1:5500/kiegeszitok.html/")
#time.sleep(3)
driver.save_screenshot("Kiegeszitok.png")

elem = driver.find_element(By.CLASS_NAME,"btn")
elem.click()
time.sleep(3)

