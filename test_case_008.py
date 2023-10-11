import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


# Фикстура для инициализации и завершения работы драйвера
@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # Запуск драйвера Chrome
    yield driver  # Возврат драйвера тестовой функции
    driver.quit()  # Закрытие драйвера после выполнения теста


def test_contact_info_accessibility(driver):
    # Открытие браузера (выполняется автоматически фикстурой driver)

    # Переход на сайт Ростелеком
    driver.get("https://rt-internet.ru/")

    # Поиск контактной информации
    driver.get("https://rt-internet.ru/contacts")

    # Проверка доступности контактов
    # Проверка наличия блока "Полезные сервисы Ростелеком"
    assert len(driver.find_elements(By.CSS_SELECTOR, "#b11642")) > 0, "Блок 'Полезные сервисы Ростелеком' не найден"

    # Проверка наличия блока "Как подключить Ростелеком"
    assert len(driver.find_elements(By.CSS_SELECTOR, "#b11415")) > 0, "Блок 'Как подключить Ростелеком' не найден"
