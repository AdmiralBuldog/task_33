import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


# Фикстура для инициализации и завершения работы драйвера
@pytest.fixture
def driver():
    # Инициализация драйвера
    driver = webdriver.Chrome()
    yield driver  # Возврат драйвера тестовой функции
    driver.quit()  # Закрытие драйвера после выполнения теста


def test_tariffs_display(driver):
    # Переход на главную страницу Ростелеком
    driver.get("https://rt-internet.ru/")

    # Ожидание загрузки страницы (опционально, зависит от скорости вашего интернета)
    driver.implicitly_wait(10)

    # Поиск элементов с названиями тарифов и их стоимостью
    tariff_names_elements = driver.find_elements(By.CSS_SELECTOR, '.tarifs-name')
    tariff_cost_elements = driver.find_elements(By.CSS_SELECTOR, '.tarifs-cost .tarif-ap')

    # Извлечение текста из найденных элементов и вывод их в консоль
    for name_element, cost_element in zip(tariff_names_elements, tariff_cost_elements):
        tariff_name = name_element.text
        tariff_cost = cost_element.text
        print(f'Название тарифа: {tariff_name}, Стоимость тарифа: {tariff_cost}')

