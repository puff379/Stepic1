from selenium import webdriver
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects1.html")

n1 = browser.find_element_by_css_selector("span#num1")
n2 = browser.find_element_by_css_selector("span#num2")

x = n1.text
y = n2.text
z = int(x) + int(y)

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(str(z))
button = browser.find_element_by_class_name("btn").click()
