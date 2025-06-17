from playwright.sync_api import Page, expect

import pytest

import time
def test_example(page: Page) -> None:
    
    page.goto("http://saucedemo.com/")
    
    page.locator("[data-test=\"username\"]").click()
    time.sleep(5)
    page.locator("[data-test=\"username\"]").fill("standard_user")
    time.sleep(5)
    page.locator("[data-test=\"password\"]").click()
    time.sleep(5)
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    try :
        expect(page).to_have_url("https://www.saucedemo.com")
    except:
        print("Login failed")
    expect(page).to_have_url("https://www.saucedemo.com")