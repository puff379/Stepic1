from selenium import webdriver
import os

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/file_input.html")

input1 = browser.find_element_by_css_selector("[name='firstname']")
input1.send_keys("Руслан")
input2 = browser.find_element_by_css_selector("[name='lastname']")
input2.send_keys("Умов")
input3 = browser.find_element_by_css_selector("[name='email']")
input3.send_keys("mail@exeample.com")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "requiremets.txt"
file_path = os.path.join(current_dir, file_name)

element = browser.find_element_by_id("file")
element.send_keys(file_path)

button = browser.find_element_by_tag_name("button").click()
