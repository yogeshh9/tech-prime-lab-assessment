import pytest
import logging
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def pytest_configure():
    log_filename = f"./logs/test_log{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
    logging.basicConfig(
        level=logging.INFO,
        filename= log_filename,
        format= '%(asctime)s %(levelname)s %(message)s'
    )

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)
    driver.get("https://mysitebook.io/")
    driver.maximize_window()
    logging.info("Browser launched and maximized.")

    close_popup = driver.find_element(By.XPATH, "//div[@id='close']/child::img")
    wait.until(EC.element_to_be_clickable(close_popup))
    close_popup.click()
    logging.info("Popup closed.")

    login_button = driver.find_element(By.LINK_TEXT, 'LOGIN')
    wait.until(EC.element_to_be_clickable(login_button))
    login_button.click()
    logging.info("Clicked on LOGIN button.")

    window_tabs = driver.window_handles
    driver.switch_to.window(window_tabs[1])
    wait.until(EC.presence_of_element_located((By.ID, 'mobileNumber')))
    logging.info("Switched to login window.")

    try:
        enter_phNo = driver.find_element(By.ID, 'mobileNumber')
        enter_phNo.send_keys('7391028745')
        driver.find_element(By.XPATH, "//button[text()=' Continue ']").click()
        logging.info("Entered mobile number and clicked continue.")

        wait.until(EC.presence_of_element_located((By.ID, 'password')))
        password = driver.find_element(By.ID, 'password')
        password.send_keys("Pass@1234")
        driver.find_element(By.XPATH, "//button[text()=' Login ']").click()
        logging.info("Entered password and clicked login.")
    except NoSuchElementException:
        logging.error("Element not found: Enter registered mobile number.")
        raise ValueError("Enter registered mobile number")

    wait.until(EC.title_is("Projects | Active"))
    assert driver.title == 'Projects | Active'
    logging.info("Logged in successfully, title verified.")

    driver.implicitly_wait(10)
    project = driver.find_element(By.XPATH, "//span[text()=' Sample bungalow project']")
    project.click()
    logging.info("Clicked on Sample bungalow project.")

    detailed_estimate_quotation = driver.find_element(By.XPATH, "//p[text()=' Detailed Estimate']")
    wait.until(EC.element_to_be_clickable(detailed_estimate_quotation))
    detailed_estimate_quotation.click()
    logging.info("Clicked on Detailed Estimate.")

    driver.implicitly_wait(10)
    element = driver.find_element(By.XPATH, "//th[text()='Description']")
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    logging.info("Scrolled to Description element.")

    yield driver
    driver.quit()
    logging.info("Browser closed.")