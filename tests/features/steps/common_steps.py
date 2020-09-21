from behave import *
from selenium.webdriver.common.action_chains import ActionChains
from pages.KSCalculator import KSCalculator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@given(u'I navigate to Kiwisaver Calculator Page')
def step_impl(context):
    KiwisaverCalculatorPage_URL="https://www.westpac.co.nz/kiwisaver/calculators/kiwisaver-calculator/"
    global driver
    driver = context.driver
    if driver.current_url == KiwisaverCalculatorPage_URL:
        return
    else:
        #driver.get(KiwisaverCalculatorPage_URL)
        '''
        Navigating from HomePage as requested.The page can be accessed directly using above line
        '''
        kiwiSaver_Tab = KSCalculator(context).wait_for_element_to_load("id","ubermenu-section-link-kiwisaver-ps")
        ActionChains(driver).move_to_element(kiwiSaver_Tab).perform()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "ubermenu-item-cta-kiwisaver-calculators-ps")))
        KSCalculator(context).find_and_click_resource_using("id","ubermenu-item-cta-kiwisaver-calculators-ps")
        driver.find_element_by_xpath("//a[@href='/kiwisaver/calculators/kiwisaver-calculator/' and text()='Click here to get started.']").click()
        KSCalculator(context).wait_for_element_to_load("xpath","//iframe[starts-with(@src, '/calculator-widgets/kiwisaver-calculator/')]")

