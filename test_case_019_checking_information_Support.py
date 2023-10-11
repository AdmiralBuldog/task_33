import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_support_section_display(driver):
    driver.get("https://rt-internet.ru/")

    # Переход в раздел "Поддержка"
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#b22937 > p > a"))).click()

    # Проверка текста "что требуется" и блока под текстом
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#c_11768")))
    assert "Что требуется" in element.text

    # Проверка блока Техподдержка/Обслуживание под текстом "Что требуется"
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#i11771")))
    assert "Техподдержка/Обслуживание" in element.text

    # Проверка блока "Действия по заявке" под текстом "Что требуется"
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#i11772")))
    assert "Действия по заявке" in element.text

    # Проверка блока "Подключить Ростелеком" под текстом "Что требуется"
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#i11770")))
    assert "Подключить Ростелеком" in element.text