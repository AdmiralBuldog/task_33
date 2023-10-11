import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# Фикстура для инициализации и завершения работы драйвера
@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # Запуск драйвера Chrome
    yield driver  # Возврат драйвера тестовой функции
    driver.quit()  # Закрытие драйвера после выполнения теста


def test_accessibility_of_main_page(driver):
    # Открытие браузера выполняется автоматически фикстурой driver

    #  Переход на главную страницу Ростелеком
    driver.get("https://rt-internet.ru/")

    #  Ожидание загрузки страницы (ожидание появления уникального элемента на главной странице)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#c_17311"))
    )

    #  Проверка доступности страницы
    assert "Ростелеком" in driver.title, f"Expected 'Ростелеком' in title, but got {driver.title}"
    # Проверка, что на странице нет сообщений об ошибках (пример для простого сообщения об ошибке)
    assert "Ошибка" not in driver.page_source, "Ошибка найдена на главной странице"
