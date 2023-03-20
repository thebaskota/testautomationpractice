from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.microsoft import IEDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.ie.service import Service as IEService


def get_web_driver_instance(browser="chrome"):
    """
    Get WebDriver Instance based on the browser passed

    :return driver:
    """

    if browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    elif browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    elif browser == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

    elif browser == "ie":
        driver = webdriver.Ie(service=IEService(IEDriverManager().install()))

    else:
        # if the name of the browser is not on the list, or not passed, use chrome
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    # Maximize the window
    driver.maximize_window()

    return driver


