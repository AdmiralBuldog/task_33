import requests
import pytest
import ssl
import socket
from urllib.parse import urlparse


def test_https_security():
    # URL сайта Ростелеком
    url = "https://rt-internet.ru/"

    # Выполнение HTTP-запроса к сайту Ростелеком
    response = requests.get(url)

    # Проверка, что протокол соединения - HTTPS
    assert response.url.startswith("https://"), f"Протокол соединения не HTTPS: {response.url}"

    # Получение имени хоста и порта из URL
    parsed_url = urlparse(url)
    host = parsed_url.hostname
    port = parsed_url.port if parsed_url.port else 443  # Если порт не указан, используется порт по умолчанию для
    # HTTPS (443)

    # Установка соединения для проверки SSL-сертификата
    context = ssl.create_default_context()
    with context.wrap_socket(socket.socket(), server_hostname=host) as s:
        s.connect((host, port))
        cert = s.getpeercert()

    # Проверка, что SSL-сертификат действителен
    assert cert, "SSL-сертификат не действителен или отсутствует"

    # Если обе проверки прошли успешно, тест будет считаться пройденным


# Запуск теста
if __name__ == "__main__":
    pytest.main([__file__])
