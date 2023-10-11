import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture  # Определение фикстуры для инициализации и завершения работы драйвера
def driver():
    driver = webdriver.Chrome()  # Создание экземпляра драйвера Chrome
    yield driver  # Возврат драйвера тестовой функции и ожидание завершения теста
    driver.quit()  # Закрытие браузера после завершения теста


def test_region_change_functionality(driver):
    driver.get("https://rt-internet.ru/")

    # Находим и кликаем на меню для выбора региона
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#b22925"))
    ).click()

    # Вводим в строку город Санкт-Петербург
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#myInputCity"))
    ).send_keys("Санкт-Петербург")

    # Выбираем Санкт-Петербург из выпадающего списка
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#searchList > li > a"))
    ).click()

    # Проверяем, что регион успешно изменен на выбранный
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#b22925"), "Санкт-Петербург")
    )
