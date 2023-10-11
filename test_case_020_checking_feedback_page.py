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


def test_feedback_page(driver):
    driver.get("https://rt-internet.ru/help#/quiz-choice")

    # Проверка наличия различных форм обратной связи и их отображения
    feedback_boxes = {
        "Социальные сети": "#i11317",
        "Телефон поддержки": "#i11339",
        "Онлайн чаты и мессенджеры": "#i11326",
        "E-mail": "#i11335",
        "Офисы": "#i11343",
        "Сайт поддержки": "#i11483"
    }

    for box_name, selector in feedback_boxes.items():
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
        assert element.is_displayed(), f"{box_name} box is not displayed"

        # Проверка кликабельности иконок социальных сетей
    ok_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#b11324 > img"))
    )
    assert ok_icon.is_displayed()

    vk_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#b11322 > img"))
    )
    assert vk_icon.is_displayed()

    phone_number = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#b11342 > p > a"))
    )
    assert phone_number.text == "8 800 100 08 00"
    assert phone_number.is_enabled()

    viber_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#b11329 > p > a:nth-child(2)"))
    )
    assert viber_link.is_enabled()

    # Проверка ссылок в боксах
    email_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#i11335 a"))
    )
    assert email_link.get_attribute("href") == "https://lk.rt.ru/"

    offices_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#i11343 a"))
    )
    assert offices_link.get_attribute("href") == "https://rt.ru/sale-office"

    support_site_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#i11483 a"))
    )
    assert support_site_link.get_attribute("href") == "https://moscow.old.rt.ru/service"
