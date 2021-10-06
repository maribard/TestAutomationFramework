#from selenium.webdriver.chrome.webdriver import webdriver
import time

import pytest

from pages.dashboard_page import DashboardPage
from pages.logging_page import LoggingPage
from pages.testarena_launch_page import LaunchPage


@pytest.mark.usefixtures("setup")
class TestDemo():
    def test_demo_fail_login(self):
        # Launching browser and opening the arena website
        lp = LaunchPage(self.driver)
        lp.choose_demo()
        time.sleep(1)
        lg_p = LoggingPage(self.driver, self.wait)
        lg_p.login("failde_login")
        lg_p.password("failed_pass")
        curr_url = lg_p.click_login()
        assert curr_url == "http://demo.testarena.pl/logowanie"


    def test_demo_success_login(self):
        time.sleep(1)
        lg_p = LoggingPage(self.driver, self.wait)
        lg_p.login("administrator@testarena.pl")
        lg_p.password("sumXQQ72$L")
        curr_url = lg_p.click_login()
        assert curr_url == "http://demo.testarena.pl/"


    def test_demo_add_task(self):
        list_of_date = ["New1", "gege", "Chrome", "1.1", "2018-06-14 23:59", "Gall Anonim (administrator@testarena.pl)"]
        db = DashboardPage(self.driver, self.wait)
        db.choose_project("Monika123")
        db.click_tasks()
        db.add_task()
        db.fill_the_fields_for_task(list_of_date)
        result = db.click_save()
        assert result.text == "Task successfully added!"


    def test_demo_check_if_task_wask_added(self):
        db = DashboardPage(self.driver, self.wait)
        db.click_tasks()
        assert db.check_if_task_was_added("New1") == True








