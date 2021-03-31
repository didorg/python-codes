__author__ = "didorg"
# selenium
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://theautomationzone.blogspot.com/2020/07/xpath-practice.html")
print(driver.find_element_by_xpath("//*[@id='id1']").text)
