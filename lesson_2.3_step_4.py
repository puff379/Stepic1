from selenium import webdriver
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/alert_accept.html")

button = browser.find_element_by_tag_name("button").click()

confirm = browser.switch_to.alert
confirm.accept()

n = browser.find_element_by_id("input_value")
x = n.text
y = calc(x)

input = browser.find_element_by_id("answer")
input.send_keys(y)

button1 = browser.find_element_by_class_name("btn-primary").click()