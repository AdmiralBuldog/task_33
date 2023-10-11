import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from credentials6 import login, password  # Импорт данных из файла credentials6.py


# Фикстура для инициализации и завершения работы драйвера
@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # Запуск драйвера Chrome
    yield driver  # Возврат драйвера тестовой функции
    driver.quit()  # Закрытие драйвера после выполнения теста


def test_login_with_incorrect_password(driver):
    # Переход на начальную страницу
    driver.get("https://lk.rt.ru/")

    # Ожидание и клик по кнопке "Войти с паролем"
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "standard_auth_btn"))).click()

    # Задержка 5 секунд
    time.sleep(5)

    # Клик по кнопке "Логин"
    driver.find_element(By.ID, "t-btn-tab-login").click()

    # Ожидание появления полей ввода логина и пароля
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#username")))
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#password")))

    # Ввод логина и неверного пароля
    driver.find_element(By.CSS_SELECTOR, "#username").send_keys(login)
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)

    # Задержка 30 секунд для ввода капчи вручную (у меня начала появляться капча, поэтому сделал задержку)
    time.sleep(30)

    # Клик по кнопке "Войти"
    driver.find_element(By.ID, "kc-login").click()

    # Ожидание появления сообщения об ошибке (предположим, что селектор сообщения об ошибке #form-error-message)
    error_message = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#form-error-message"))
    )

    # Проверка, что текст сообщения об ошибке соответствует ожидаемому
    assert error_message.text == "Неверный логин или пароль", f"Unexpected error message: {error_message.text}"
