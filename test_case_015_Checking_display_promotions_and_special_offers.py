import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Фикстура для инициализации и завершения работы драйвера
@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # Запуск драйвера Chrome
    yield driver  # Возврат драйвера тестовой функции
    driver.quit()  # Закрытие драйвера после выполнения теста


def test_promotions_display(driver):
    driver.get("https://rt-internet.ru/akcii")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#b21908")))

    # Проверка акции "Великолепная четверка"
    assert driver.find_element(By.CSS_SELECTOR, "#b21908").is_displayed()
    assert driver.find_element(By.CSS_SELECTOR, "#b21907 > p").is_displayed()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#b21978 > p")))  # Явное
    # ожидание
    assert driver.find_element(By.CSS_SELECTOR, "#b21978 > p").is_displayed()
    assert driver.find_element(By.CSS_SELECTOR, "#b21912").is_displayed()

    # Проверка "Случайной акции"
    assert driver.find_element(By.CSS_SELECTOR, "#b21952").is_displayed()
    assert driver.find_element(By.CSS_SELECTOR, "#b21953").is_displayed()
    assert driver.find_element(By.CSS_SELECTOR, "#b21955").is_displayed()
