import os
from alumnium import Alumni
from selenium.webdriver import Chrome
from pytest import fixture

@fixture
def driver():
    driver = Chrome()
    yield driver
    driver.quit()

@fixture
def al(driver: Chrome):
    al = Alumni(driver)
    yield al
    al.quit()

def test_login(al: Alumni, driver: Chrome):
    al = Alumni(driver)
    driver.get("https://www.saucedemo.com/")
    al.check("Page title contains 'Swag Labs'")
    al.do("type 'standard_user' into the Username field")
    al.do("type 'secret_sauce' into the Password field") # This is a public password for the demo account
    al.do("click the 'Login' button")
    al.check("User is logged in and can access the products page")
    assert al.get("Sauce Labs Backpack price") == "$29.99"