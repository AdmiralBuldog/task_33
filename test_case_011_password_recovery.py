# Импорт необходимых библиотек и модулей
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import email_config  # Импорт конфигурационного файла с электронной почтой


@pytest.fixture
def driver():
    # Инициализация веб-драйвера
    driver = webdriver.Chrome()
    yield driver
    driver.quit()  # Закрыть браузер после завершения теста


def test_password_recovery(driver):
    # Открыть сайт Ростелеком
    driver.get("https://lk.rt.ru")

    # Ожидание появления кнопки "Войти с паролем" и клик по ней
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#standard_auth_btn"))
    ).click()

    # Ожидание появления кнопки "Забыл пароль" и клик по ней
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#forgot_password"))
    ).click()

    # Клик по кнопке для восстановления пароля по почте
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#t-btn-tab-mail"))
    ).click()
    
    # Ожидание появления поля ввода почты, ввод почты
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#username"))
    ).send_keys(email_config.email)  # Использование электронной почты из конфигурационного файла

    # Ожидание появления кнопки "Продолжить" и клик по ней
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#reset"))
    ).click()

    # Ожидание в 20 секунд для ручного ввода кода из почты
    print("Ожидание ввода кода из почты...")
    driver.implicitly_wait(20)  # Пауза в 20 секунд

    # Попытка найти сообщение об ошибке
    error_message_element = EC.presence_of_element_located((By.CSS_SELECTOR, "#form-error-message"))
    success_window_element = EC.presence_of_element_located((By.CSS_SELECTOR, "#page-right > div"))

    if WebDriverWait(driver, 10).until(error_message_element):
        error_message = driver.find_element(By.CSS_SELECTOR, "#form-error-message").text
        assert error_message == "Этот пароль уже использовался, укажите другой пароль", f"Ошибка: {error_message}"
    elif WebDriverWait(driver, 10).until(success_window_element):
        print("Процесс восстановления пароля прошел успешно")
    elif driver.current_url == "https://lk.rt.ru":
        print("Процесс восстановления пароля прошел успешно, пользователь перенаправлен на страницу авторизации")
    else:
        print("Неизвестное состояние, тест не удался")
