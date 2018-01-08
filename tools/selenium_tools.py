from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



def _get_driver():
    driver = webdriver.PhantomJS(desired_capabilities=_set_driver_ua())
    Logger.info('Initialize PhantomJS Webdriver')
    _set_cookies(driver, my_session().cookies)
    Logger.info('Initialize Webdriver Cookies')
    _set_driver_window_size(driver)
    Logger.info('Initialize Webdriver Finished')
    return driver


def _set_driver_ua():
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = (_get_user_agent())
    return dcap


def _set_cookies(driver, cookies):
    for c in cookies:
        driver.add_cookie({'name': c.name, 'value': c.value, 'path': c.path, 'expiry': c.expires, 'domain': c.domain})


def _set_driver_window_size(driver):
    driver.set_window_position(0, 0)
    driver.set_window_size(1920, 1080)
