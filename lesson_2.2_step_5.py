from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get(" http://SunInJuly.github.io/execute_script.html")

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

input_result = browser.find_element_by_id("answer")
#browser.execute_script("return arguments[0].scrollIntoView(true);", input_result)
input_result.send_keys(y)

checkbox = browser.find_element_by_id("robotCheckbox")
browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
checkbox.click()

r_button = browser.find_element_by_css_selector("[for='robotsRule']")
r_button.click()

button = browser.find_element_by_class_name("btn").click()
#button.click()

