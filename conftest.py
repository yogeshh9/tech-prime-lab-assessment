import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()

    wait = WebDriverWait(driver, 15)
    driver.get("https://mysitebook.io/")
    driver.maximize_window()

    close_popup = driver.find_element(By.XPATH, "//div[@id='close']/child::img")
    wait.until(EC.element_to_be_clickable(close_popup))
    close_popup.click()

    login_button = driver.find_element(By.LINK_TEXT, 'LOGIN')
    wait.until(EC.element_to_be_clickable(login_button))
    login_button.click()

    window_tabs = driver.window_handles

    driver.switch_to.window(window_tabs[1])
    wait.until(EC.presence_of_element_located((By.ID, 'mobileNumber')))

    try:
        enter_phNo = driver.find_element(By.ID, 'mobileNumber')
        enter_phNo.send_keys('7391028745')
        driver.find_element(By.XPATH, "//button[text()=' Continue ']").click()
        wait.until(EC.presence_of_element_located((By.ID, 'password')))
        password = driver.find_element(By.ID, 'password')
        password.send_keys("Pass@1234")
        driver.find_element(By.XPATH, "//button[text()=' Login ']").click()
    except NoSuchElementException:
        raise ValueError("Enter registered mobile number")
    finally:
        wait.until(EC.title_is("Projects | Active"))
        assert driver.title == 'Projects | Active'

    driver.implicitly_wait(10)
    project = driver.find_element(By.XPATH, "//span[text()=' Sample bungalow project']")
    project.click()
    detailed_estimate_quotation = driver.find_element(By.XPATH, "//p[text()=' Detailed Estimate']")
    wait.until(EC.element_to_be_clickable(detailed_estimate_quotation))
    detailed_estimate_quotation.click()

    driver.implicitly_wait(10)

    element = driver.find_element(By.XPATH, "//th[text()='Description']")
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    driver.implicitly_wait(5)

    yield driver
    driver.quit()