import pytest
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

    assert expected_quantity == actual_quantity
    assert expected_unit == actual_unit
    assert expected_rate == actual_rate
    assert expected_cost == actual_cost












