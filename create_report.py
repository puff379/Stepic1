from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("https://megusta.staging.posiflora.com/admin/login")

input1 = browser.find_element_by_id("mat-input-0")
input1.send_keys("flowershop")
input2 = browser.find_element_by_id("mat-input-1")
input2.send_keys("flower")
button = browser.find_element_by_class_name("mat-button-wrapper")
button.click()

browser.get("https://megusta.staging.posiflora.com/admin/reports/create")
time.sleep(8)
button1 = browser.find_element_by_class_name("bem-button")
button1.click()
