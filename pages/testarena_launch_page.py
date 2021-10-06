import time

class LaunchPage():
    def __init__(self, driver):
        self.driver = driver

    def choose_demo(self):
        self.driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div[1]/div/p[2]/a').click()
        self.driver.switch_to.window(self.driver.window_handles[1])
