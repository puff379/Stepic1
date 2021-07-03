from selenium import webdriver
import time
import os
link = "https://megusta.staging.posiflora.com/admin/login"

browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_id("mat-input-0")
input1.send_keys("flowershop")
input2 = browser.find_element_by_id("mat-input-1")
input2.send_keys("flower")
button = browser.find_element_by_class_name("mat-button-wrapper")
button.click()

browser.get("https://megusta.staging.posiflora.com/admin/customers/import")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "requiremets.txt"
file_path = os.path.join(current_dir, file_name)
time.sleep(3)
element = browser.find_element_by_css_selector("[type='file']")
element.send_keys(file_path)

#div>button:nth-child(3)[type='button']