import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class DashboardPage():
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait



    def choose_project(self, name):

        el = self.driver.find_element_by_xpath('/html/body/header/div[1]/span/div[1]/form/div')
        el.click()
        el = self.driver.find_element_by_xpath('//*[@id="activeProject_chosen"]/div/div/input')
        el.send_keys(name)
        el.send_keys(Keys.ENTER)


    def click_tasks(self):
        self.driver.find_element_by_xpath('//*[@id="wrapper"]/ul/li[7]/a').click()


    def add_task(self):
        self.driver.find_element_by_xpath('//*[@id="content"]/article/nav/ul/li/a').click()
        time.sleep(2)


    def fill_the_fields_for_task(self, list_of_date):
        self.driver.find_element_by_xpath('//*[@id="title"]').send_keys(list_of_date[0])
        self.driver.find_element_by_xpath('//*[@id="description"]').send_keys(list_of_date[1])
        el = self.driver.find_element_by_xpath('//*[@id="token-input-environments"]')
        el.send_keys(list_of_date[2])
        time.sleep(1)
        el.send_keys(Keys.ENTER)

        el = self.driver.find_element_by_xpath('//*[@id="token-input-versions"]')
        el.send_keys(list_of_date[3])
        time.sleep(1)
        el.send_keys(Keys.ENTER)

        el = self.driver.find_element_by_xpath('//*[@id="dueDate"]')
        el.send_keys(list_of_date[4])

        self.driver.find_element_by_xpath('//*[@id="j_assignToMe"]').click()
        time.sleep(1)


    def click_save(self):
        self.driver.find_element_by_xpath('//*[@id="save"]').click()
        time.sleep(1)
        result = self.driver.find_element_by_xpath('//*[@id="j_info_box"]/p')
        return result


    def check_if_task_was_added(self, title):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, f"(//a[contains(text(),'{title}')])")))
            return True
        except:
            print()
            print("There is no task")
            return False



