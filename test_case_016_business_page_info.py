import pytest  # Импортирование библиотеки pytest для организации тестирования
from selenium import webdriver  # Импортирование webdriver для управления браузером
from selenium.webdriver.common.by import By  # Импортирование By для указания способа поиска элемента
from selenium.webdriver.support.ui import WebDriverWait  # Импортирование WebDriverWait для организации явных ожиданий
from selenium.webdriver.support import expected_conditions as EC  # Импортирование expected_conditions для определения условий ожидания


@pytest.fixture  # Определение фикстуры для инициализации и завершения работы драйвера
def driver():
    driver = webdriver.Chrome()  # Создание экземпляра драйвера Chrome
    yield driver  # Возврат драйвера тестовой функции и ожидание завершения теста
    driver.quit()  # Закрытие браузера после завершения теста


def test_business_page_info(driver):  # Определение тестовой функции для проверки информации на странице бизнеса
    driver.get("https://rt-internet.ru/")  # Открытие главной страницы сайта
    driver.find_element(By.CSS_SELECTOR, "a[href='/business']").click()  # Переход на страницу бизнеса по ссылке

    WebDriverWait(driver, 10).until(  # Ожидание появления элемента на странице в течение 10 секунд
        EC.presence_of_element_located((By.CSS_SELECTOR, "#b13153"))
    )

    assert "Популярные бизнес решения от Ростелеком" in driver.page_source  # Проверка наличия текста на странице

    assert driver.find_element(By.CSS_SELECTOR, "#c_13151").is_displayed()  # Проверка отображения элемента на странице
