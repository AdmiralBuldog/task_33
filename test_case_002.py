import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Получение логина и пароля из отдельного файла
from credentials2 import incorrect_password, correct_login


@pytest.fixture  # Декоратор, указывающий, что следующая функция является фикстурой pytest
def driver():  # Определение фикстуры, которая предоставляет объект драйвера браузера
    driver = webdriver.Chrome()  # Создание нового экземпляра драйвера Chrome
    driver.maximize_window()  # Максимизация окна браузера
    yield driver  # Возвращение драйвера вызывающему коду и приостановка функции до завершения теста
    driver.quit()  # Закрытие браузера и завершение сессии драйвера после завершения теста



def test_login_with_incorrect_password(driver):
    # Переход на начальную страницу
    driver.get("https://lk.rt.ru/")

    # Ожидание и клик по кнопке "Войти с паролем"
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "standard_auth_btn"))).click()

    # Задержка 5 секунд
    time.sleep(5)

    # Клик по кнопке "Почта"
    driver.find_element(By.ID, "t-btn-tab-mail").click()

    # Ожидание появления полей ввода логина и пароля
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#username")))
    WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#password")))

    # Ввод логина и неверного пароля
    driver.find_element(By.CSS_SELECTOR, "#username").send_keys(correct_login)
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys(incorrect_password)

    # Клик по кнопке "Войти"
    driver.find_element(By.ID, "kc-login").click()

    # Ожидание сообщения об ошибке
    error_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                    "#form-error-message")))

    # Проверка текста сообщения об ошибке
    assert error_message.text == "Неверный логин или пароль"

    # Находим элемент с заголовком страницы
    header_element = driver.find_element(By.CSS_SELECTOR, "#page-right > div > div.card-container__wrapper > h1")

    # Проверка, что текст элемента соответствует ожидаемому заголовку страницы "Авторизация"
    assert header_element.text == "Ростелеком"
