import pytest
from selenium.webdriver.common.by import By

@pytest.mark.rcc
def test_pcc_m_15(browser):
    expected_quantity = "4100.00"
    expected_unit = "cum"
    expected_rate = "180.00"
    expected_cost = "7,38,000.00"

    browser.implicitly_wait(10)

    actual_quantity = browser.find_element(By.XPATH, "//span[text()='PCC M 15']//parent::td//following-sibling::td[@id='quantity']").text
    actual_unit = browser.find_element(By.XPATH, "//span[text()='PCC M 15']//parent::td//following-sibling::td[@id='unit']").text
    actual_rate = browser.find_element(By.XPATH, "//span[text()='PCC M 15']//parent::td//following-sibling::td[@id='rate']").text
    actual_cost = browser.find_element(By.XPATH, "//span[text()='PCC M 15']//parent::td//following-sibling::td[@id='total']").text

    assert expected_quantity == actual_quantity
    assert expected_unit == actual_unit
    assert expected_rate == actual_rate
    assert expected_cost == actual_cost

@pytest.mark.rcc
def test_concrete_m_25(browser):
    expected_quantity = "130.40"
    expected_unit = "cum"
    expected_rate = "280.00"
    expected_cost = "36,512.04"

    browser.implicitly_wait(10)

    actual_quantity = browser.find_element(By.XPATH, "//span[text()='Concrete M 25']//parent::td//following-sibling::td[@id='quantity']").text
    actual_unit = browser.find_element(By.XPATH, "//span[text()='Concrete M 25']//parent::td//following-sibling::td[@id='unit']").text
    actual_rate = browser.find_element(By.XPATH, "//span[text()='Concrete M 25']//parent::td//following-sibling::td[@id='rate']").text
    actual_cost = browser.find_element(By.XPATH, "//span[text()='Concrete M 25']//parent::td//following-sibling::td[@id='total']").text

    assert expected_quantity == actual_quantity
    assert expected_unit == actual_unit
    assert expected_rate == actual_rate
    assert expected_cost == actual_cost


@pytest.mark.rcc
def test_steel(browser):
    expected_quantity = "3494.65"
    expected_unit = "Kg"
    expected_rate = "64.97"
    expected_cost = "2,27,047.72"

    browser.implicitly_wait(10)

    actual_quantity = browser.find_element(By.XPATH, "//span[text()='Steel']//parent::td//following-sibling::td[@id='quantity']").text
    actual_unit = browser.find_element(By.XPATH, "//span[text()='Steel']//parent::td//following-sibling::td[@id='unit']").text
    actual_rate = browser.find_element(By.XPATH, "//span[text()='Steel']//parent::td//following-sibling::td[@id='rate']").text
    actual_cost = browser.find_element(By.XPATH, "//span[text()='Steel']//parent::td//following-sibling::td[@id='total']").text

    assert expected_quantity == actual_quantity
    assert expected_unit == actual_unit
    assert expected_rate == actual_rate
    assert expected_cost == actual_cost










