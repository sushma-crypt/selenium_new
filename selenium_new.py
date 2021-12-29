from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time

PATH =("C:\webdrivers\chromedriver.exe")
driver =webdriver.Chrome(PATH)
driver.maximize_window()
driver.get("http://eeaonline.eea.state.ma.us/Portal/#!/search/asbestos")
driver.find_element(By.ID,"TownName").click()



countryDD = Select(select)
countryDD.select_by_visible_text('ACTON').click()
countryDD.send_keys(Keys.RETURN)

click_ACTON = driver.find_element_by_class_name("btn btn-primary btn-custom pull-right").click()