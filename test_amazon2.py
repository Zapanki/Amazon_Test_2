import time

import pytest
from selenium.webdriver.common.by import By
expected_title = 'Amazon.com. Spend less. Smile more.'
base_url = 'https://www.amazon.com'


@pytest.mark.parametrize("item", [
    "nike air max",
    "reebok crossfit shoes men",
    "puma sneakers",
    "adidas classic shoes"])
@pytest.mark.regressiontest
def test_search(browser_firefox, item):
    # navigate to Amazon.com home page
    browser_firefox.get(base_url)
    # verify that website title is Amazon.com
    assert browser_firefox.title == expected_title
    # locate search field element and enter search item from the list in the search field
    browser_firefox.find_element(By.ID, "twotabsearchtextbox").send_keys(item)
    browser_firefox.find_element(By.XPATH,"//input[@value='Go']").click()
    time.sleep(3)
    browser_firefox.find_element(By.ID, "a-autoid-0-announce").click()
    browser_firefox.find_element(By.ID, "s-result-sort-select_5").click()
    time.sleep(2)
    browser_firefox.find_element(By.ID, "low-price").send_keys("500")
    browser_firefox.find_element(By.CLASS_NAME, "a-button-input").click()
    # locate and click on search button
    # verify the page title