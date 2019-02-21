from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException

file = "chromedriver.exe"
try:
    driver = webdriver.Chrome(executable_path=file)
except WebDriverException:
    print(f'The system cannot find the file specified: "{file}"')
    exit(0)
timeout = 10


def close_and_finish_execution():
    """
    Closes current window then
    Closes the browser and shuts down the ChromeDriver then
    Exists from the script.
    :return:
    """
    driver.close()
    driver.quit()
    exit(0)


def get_element_with_xpath(_xpath=None):
    """
    Locates and returns the web element with given xpath,
    If element is not available warns user about it and closes browser
    If xpath is not given warns that it is mandatory and closes browser.
    :param _xpath:
    :return:
    """
    if _xpath:
        try:
            return WebDriverWait(driver, timeout).until(
                ec.presence_of_element_located((By.XPATH, _xpath)))
        except TimeoutException:
            print(f'Element with xpath "{_xpath}" was not found in "{timeout}" seconds.')
            close_and_finish_execution()
    else:
        print(f'Attribute xpath is mandatory.')
        close_and_finish_execution()


def get_all_elements_with_xpath(_xpath=None):
    """
    Locates and returns the web element with given xpath,
    If element is not available warns user about it and closes browser
    If xpath is not given warns that it is mandatory and closes browser.
    :param _xpath:
    :return:
    """
    if _xpath:
        try:
            return WebDriverWait(driver, timeout).until(
                ec.presence_of_all_elements_located((By.XPATH, _xpath)))
        except TimeoutException:
            print(f'Element with xpath "{_xpath}" was not found in "{timeout}" seconds.')
            close_and_finish_execution()
    else:
        print(f'Attribute xpath is mandatory.')
        close_and_finish_execution()


def print_found_urls_hrefs(elements=None, count=10):
    """
    Prints all elements which have href attribute
    :param elements:
    :param count:
    :return:
    """
    if count > len(elements):
        print(f'Max value of "count: {count}" can not exceed "given elements count: {len(elements)}".')
        close_and_finish_execution()
    if elements and count:
        for num, video in enumerate(elements):
            if num == count:
                break
            href = video.get_attribute("href")
            if href is None:
                print(f'Element "{video}" has no href attribute.')
                continue
            else:
                print(f"{num+1}. {href}")
    else:
        print(f'Attribute elements and count are mandatory.')
        close_and_finish_execution()
