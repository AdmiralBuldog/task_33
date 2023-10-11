import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from credentials import correct_login, correct_password  # Импорт данных для входа из файла credentials.py


# Фикстура для инициализации и завершения работы драйвера
@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # Запуск драйвера Chrome
    yield driver  # Возврат драйвера тестовой функции
    driver.quit()  # Закрытие драйвера после выполнения теста


def test_client_cabinet(driver):

    # Переход на сайт Ростелеком
    driver.get("https://lk.rt.ru/")

    # Вход в кабинет клиента
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#standard_auth_btn"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#username"))).send_keys(correct_login)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#password"))).send_keys(
        correct_password)
    driver.find_element(By.ID, "kc-login").click()

    # Проверка работы кабинета
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,
                                          "#root > div > div > div.StyledPageContent-llZWey.bEuybU > div > div > "
                                          "div.StyledEntryPageLeftPart-goVwnv.iYgrwF > div > div:nth-child(2)"))
    )
    assert driver.find_element(By.CSS_SELECTOR,
                               "#root > div > div > div.StyledPageContent-llZWey.bEuybU > div > div > "
                               "div.StyledEntryPageRightPart-jdDEQA.fSLyHv > "
                               "div.StyledRightPartItem-yxKwy.StyledRightPartItemDesktop-gdKqzo.iTvAyD.cWppie"
                               "").is_displayed(), "Лента событий не найдена"
    assert driver.find_element(By.CSS_SELECTOR,
                               "#root > div > div > div.StyledPageContent-llZWey.bEuybU > div > div > "
                               "div.StyledEntryPageRightPart-jdDEQA.fSLyHv > div:nth-child(5)").is_displayed(), (
        "Специальные "
        "предложения не "
        "найдены")

    assert driver.find_element(By.CSS_SELECTOR,
                               "#root > div > div > div.StyledPageContent-llZWey.bEuybU > div > div > "
                               "div.StyledEntryPageRightPart-jdDEQA.fSLyHv > div:nth-child(7)").is_displayed(), (
        "Блок 'Лучшее от "
        "Ростелеком' не найден")
