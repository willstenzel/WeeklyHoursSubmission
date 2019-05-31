from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import os
import time

driver = webdriver.Firefox()

root_url = 'https://studentemployment.neu.edu/'

# User login
driver.get(root_url + 'tsx_studentjobs.aspx')
driver.find_element_by_id('Skin_ctl08_LoginNameText').send_keys('stenzel.w')
driver.find_element_by_id('Skin_ctl08_LoginPasswordText').send_keys(os.environ.get('PASSWORD', ""))
driver.find_element_by_name('Skin$ctl08$ctl14').click()

driver.find_element_by_xpath('//*[@title="Co-op Research Assistant"]').click()

try:
    driver.find_element_by_xpath('//*[@title="Start time sheet"]').click()
except NoSuchElementException:
    driver.find_element_by_xpath('//*[@title="Go to time sheet"]').click()

# browser.switchTo().alert().accept()
driver.find_element_by_tag_name('body').send_keys(Keys.ENTER)


weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for weekday in weekdays:

    driver.find_element_by_xpath('//*[@title="Add a New Entry"]').click()

    day_select = driver.find_element_by_id('Skin_body_ctl01_WDL')
    for option in day_select.find_elements_by_tag_name('option'):
        if weekday in option.text:
            option.click()
            break

    start_time_select = driver.find_element_by_id('Skin_body_ctl01_StartDateTime1')
    for option in start_time_select.find_elements_by_tag_name('option'):
        if "8:45AM" in option.text:
            option.click()
            break

    end_time_select = driver.find_element_by_id('Skin_body_ctl01_EndDateTime1')
    for option in end_time_select.find_elements_by_tag_name('option'):
        if "12:00PM" in option.text:
            option.click()
            break

    driver.find_element_by_xpath("//input[@type='submit']").click()

    driver.find_element_by_xpath('//*[@title="Add a New Entry"]').click()

    day_select = driver.find_element_by_id('Skin_body_ctl01_WDL')
    for option in day_select.find_elements_by_tag_name('option'):
        if weekday in option.text:
            option.click()
            break

    start_time_select = driver.find_element_by_id('Skin_body_ctl01_StartDateTime1')
    for option in start_time_select.find_elements_by_tag_name('option'):
        if "12:30PM" in option.text:
            option.click()
            break

    end_time_select = driver.find_element_by_id('Skin_body_ctl01_EndDateTime1')
    for option in end_time_select.find_elements_by_tag_name('option'):
        if "5:15PM" in option.text:
            option.click()
            break

    driver.find_element_by_xpath("//input[@type='submit']").click()


driver.find_element_by_xpath('//a[contains(@href, "ConfirmTimesheet")]').click()

time.sleep(160)
driver.quit()