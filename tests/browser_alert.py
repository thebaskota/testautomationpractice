from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import test_logger
import test_status
from web_driver_factory import get_web_driver_instance


def test_browser_alert():
    log = test_logger.test_logger()
    driver = get_web_driver_instance("chrome")

    log.info("<-------------Browser alert Test Starts--------------->")
    driver.get("https://testautomationpractice.blogspot.com/")

    # locators and test_data, ideally this would be separate from the test.
    alert_button_locator = (By.CSS_SELECTOR, 'button[onclick = "myFunction()"]')
    ok_text_locator = (By.XPATH, '//p[contains(text(), "You pressed OK!")]')
    cancel_text_locator = (By.XPATH, '//p[contains(text(), "You pressed Cancel!")]')

    log.info("clicking on the button that produces browser alert")
    alert_button_element = WebDriverWait(driver, 30).until(EC.presence_of_element_located(alert_button_locator))
    alert_button_element.click()

    log.info("switching to alert box")
    alert = driver.switch_to.alert

    log.info("accepting the alert")
    alert.accept()

    log.info(" checking the ok alert text")
    try:
        ok_text_element = WebDriverWait(driver, 30).until(EC.presence_of_element_located(ok_text_locator))
    except Exception as e:
        ok_text_element = None
        log.error(f"Cannot find the web element due to exception {e}")

    test_status.assert_true(ok_text_element is not None, "Ok Alert Text Present Check")

    log.info("clicking on the button that produces browser alert")
    alert_button_element = WebDriverWait(driver, 30).until(EC.presence_of_element_located(alert_button_locator))
    alert_button_element.click()

    log.info("switching to alert box")
    alert = driver.switch_to.alert

    log.info("dismissing the alert")
    alert.dismiss()

    log.info(" checking the cancel alert text")
    try:
        cancel_text_element = WebDriverWait(driver, 30).until(EC.presence_of_element_located(cancel_text_locator))
    except Exception as e:
        cancel_text_element = None
        log.error(f"Cannot find the web element due to exception {e}")

    test_status.assert_true(cancel_text_element is not None, "cancel Alert Text Present Check")

    log.info("<-------------Browser alert Test Starts--------------->")
