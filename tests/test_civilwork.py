import pytest
import logging
from selenium.webdriver.common.by import By

@pytest.mark.civilwork
def test_excavation(browser):
    expected_quantity = "4100.00"
    expected_unit = "cum"
    expected_rate = "180.00"
    expected_cost = "7,38,000.00"

    browser.implicitly_wait(10)

    actual_quantity = browser.find_element(By.XPATH, "//span[text()='Excavation']//parent::td//following-sibling::td[@id='quantity']").text
    actual_unit = browser.find_element(By.XPATH, "//span[text()='Excavation']//parent::td//following-sibling::td[@id='unit']").text
    actual_rate = browser.find_element(By.XPATH, "//span[text()='Excavation']//parent::td//following-sibling::td[@id='rate']").text
    actual_cost = browser.find_element(By.XPATH, "//span[text()='Excavation']//parent::td//following-sibling::td[@id='total']").text

    logging.info(f"Excavation - Expected Quantity: {expected_quantity}, Actual Quantity: {actual_quantity}")
    logging.info(f"Excavation - Expected Unit: {expected_unit}, Actual Unit: {actual_unit}")
    logging.info(f"Excavation - Expected Rate: {expected_rate}, Actual Rate: {actual_rate}")
    logging.info(f"Excavation - Expected Cost: {expected_cost}, Actual Cost: {actual_cost}")

    assert expected_quantity == actual_quantity
    assert expected_unit == actual_unit
    assert expected_rate == actual_rate
    assert expected_cost == actual_cost

@pytest.mark.civilwork
def test_backfilling(browser):
    expected_quantity = "130.40"
    expected_unit = "cum"
    expected_rate = "280.00"
    expected_cost = "36,512.04"

    browser.implicitly_wait(10)

    actual_quantity = browser.find_element(By.XPATH, "//span[text()='Backfilling']//parent::td//following-sibling::td[@id='quantity']").text
    actual_unit = browser.find_element(By.XPATH, "//span[text()='Backfilling']//parent::td//following-sibling::td[@id='unit']").text
    actual_rate = browser.find_element(By.XPATH, "//span[text()='Backfilling']//parent::td//following-sibling::td[@id='rate']").text
    actual_cost = browser.find_element(By.XPATH, "//span[text()='Backfilling']//parent::td//following-sibling::td[@id='total']").text

    logging.info(f"Backfilling - Expected Quantity: {expected_quantity}, Actual Quantity: {actual_quantity}")
    logging.info(f"Backfilling - Expected Unit: {expected_unit}, Actual Unit: {actual_unit}")
    logging.info(f"Backfilling - Expected Rate: {expected_rate}, Actual Rate: {actual_rate}")
    logging.info(f"Backfilling - Expected Cost: {expected_cost}, Actual Cost: {actual_cost}")

    assert expected_quantity == actual_quantity
    assert expected_unit == actual_unit
    assert expected_rate == actual_rate
    assert expected_cost == actual_cost

@pytest.mark.civilwork
def test_soling(browser):
    expected_quantity = "611.88"
    expected_unit = "sqft"
    expected_rate = "40.30"
    expected_cost = "24,658.88"

    browser.implicitly_wait(10)

    actual_quantity = browser.find_element(By.XPATH, "//span[text()='Soling']//parent::td//following-sibling::td[@id='quantity']").text
    actual_unit = browser.find_element(By.XPATH, "//span[text()='Soling']//parent::td//following-sibling::td[@id='unit']").text
    actual_rate = browser.find_element(By.XPATH, "//span[text()='Soling']//parent::td//following-sibling::td[@id='rate']").text
    actual_cost = browser.find_element(By.XPATH, "//span[text()='Soling']//parent::td//following-sibling::td[@id='total']").text

    logging.info(f"Soling - Expected Quantity: {expected_quantity}, Actual Quantity: {actual_quantity}")
    logging.info(f"Soling - Expected Unit: {expected_unit}, Actual Unit: {actual_unit}")
    logging.info(f"Soling - Expected Rate: {expected_rate}, Actual Rate: {actual_rate}")
    logging.info(f"Soling - Expected Cost: {expected_cost}, Actual Cost: {actual_cost}")

    assert expected_quantity == actual_quantity
    assert expected_unit == actual_unit
    assert expected_rate == actual_rate
    assert expected_cost == actual_cost

@pytest.mark.civilwork
def test_antitermite(browser):
    expected_quantity = "2000.00"
    expected_unit = "cum"
    expected_rate = "280.00"
    expected_cost = "50000.04"

    browser.implicitly_wait(10)

    actual_quantity = browser.find_element(By.XPATH, "//span[text()='Antitermite']//parent::td//following-sibling::td[@id='quantity']").text
    actual_unit = browser.find_element(By.XPATH, "//span[text()='Antitermite']//parent::td//following-sibling::td[@id='unit']").text
    actual_rate = browser.find_element(By.XPATH, "//span[text()='Antitermite']//parent::td//following-sibling::td[@id='rate']").text
    actual_cost = browser.find_element(By.XPATH, "//span[text()='Antitermite']//parent::td//following-sibling::td[@id='total']").text

    logging.info(f"Antitermite - Expected Quantity: {expected_quantity}, Actual Quantity: {actual_quantity}")
    logging.info(f"Antitermite - Expected Unit: {expected_unit}, Actual Unit: {actual_unit}")
    logging.info(f"Antitermite - Expected Rate: {expected_rate}, Actual Rate: {actual_rate}")
    logging.info(f"Antitermite - Expected Cost: {expected_cost}, Actual Cost: {actual_cost}")

    assert expected_quantity == actual_quantity
    assert expected_unit == actual_unit
    assert expected_rate == actual_rate
    assert expected_cost == actual_cost