from selenium import webdriver
import math
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")

fly_button = browser.find_element_by_tag_name("button").click()
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

n = browser.find_element_by_id("input_value")
x = n.text
y = calc(x)

input = browser.find_element_by_id("answer")
input.send_keys(y)

button = browser.find_element_by_class_name("btn-primary").click()
time.sleep(3)
alert = browser.switch_to.alert
alert.accept()
browser.quit()




