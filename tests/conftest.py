import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from settings import valid_email, valid_password

@pytest.fixture(autouse=True)
def driver():
    cService = webdriver.ChromeService(executable_path='C:\ChromeDriver\chromedriver.exe')
    pytest.driver = webdriver.Chrome(service=cService)
    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends.skillfactory.ru/login')
    yield pytest.driver

    pytest.driver.quit()

@pytest.fixture()
def my_pets():

    # Установка явного ожидания
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'email')))

    # Ввод эл. почты
    pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)

    # Установка явного ожидания
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'pass')))

    # Ввод пароля
    pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)

    # Установка явного ожидания
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))

    # Клик по кнопке "Войти"
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Установка явного ожидания
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Мои питомцы')))

    # Клик по ссылке "Мои питомцы"
    pytest.driver.find_element(By.LINK_TEXT, 'Мои питомцы').click()
