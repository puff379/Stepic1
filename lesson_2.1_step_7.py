from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/get_attribute.html")

x_element = browser.find_element_by_tag_name("img")
x = x_element.get_attribute("valuex")
y = calc(x)

input_result = browser.find_element_by_id("answer")
input_result.send_keys(y)

checkbox = browser.find_element_by_id("robotCheckbox")
checkbox.click()
r_button = browser.find_element_by_id("robotsRule")
r_button.click()

button = browser.find_element_by_class_name("btn")
button.click()
