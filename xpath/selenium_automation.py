# Bibliography
# https://theautomationzone.blogspot.com/
# https://www.youtube.com/watch?v=NhG__BL8zFo&ab_channel=AutomationZone

# selenium
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://theautomationzone.blogspot.com/2020/07/xpath-practice.html")
print(driver.find_element_by_xpath("//*[@id='id1']").text)
