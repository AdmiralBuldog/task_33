import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_business_page_info(driver):
    driver.get("https://rt-internet.ru/")
    driver.find_element(By.CSS_SELECTOR, "a[href='/business']").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#b13153"))
    )

    assert "Популярные бизнес решения от Ростелеком" in driver.page_source

    assert driver.find_element(By.CSS_SELECTOR, "#c_13151").is_displayed()

