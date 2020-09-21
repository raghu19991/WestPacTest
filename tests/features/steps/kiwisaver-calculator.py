from behave import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pages.KSCalculator import KSCalculator


@when(u'I Click information icon besides {label_Name}')
def step_impl(context,label_Name):
    icon_path="(//div[contains(@label,'{}')]//div[contains(@class,'field-info')]//button[1])[1]".format(label_Name)
    driver = context.driver
    KSCalculator(context).switch_to_frame()
    WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.ID, 'widget-loading-mask')))
    element=KSCalculator(context).wait_for_element_to_load("xpath",icon_path)
    assert element.is_displayed()
    element.click()

@then(u'message “{expected_text}” is displayed below the {field_name} field')
def step_impl(context, expected_text,field_name):
    driver=context.driver
    path_to_field = "(//div[contains(@label,'{}')]//div[contains(@class,'field-message')]//p[1])[1]".format(field_name)
    visibleText=KSCalculator(context).wait_for_element_to_load("xpath",path_to_field)
    visibleText=visibleText.get_attribute("innerHTML")
    assert visibleText == expected_text

@when(u'I populate calculator with below fields')
def step_impl(context):
    driver=context.driver
    WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.ID, 'widget-loading-mask')))
    field_values = dict(zip(context.table.headings,context.table.rows[0].cells))
    for field,value in field_values.items():
        f=KSCalculator(context)
        f.populate_fields(field,value)

@when(u'I click button View your KiwiSaver retirement projections')
def step_impl(context):
    driver=context.driver
    waitForButton=KSCalculator(context).wait_for_element_to_load("xpath","//button/span[text()='View your KiwiSaver retirement projections']")
    if waitForButton.is_displayed() is True:
        driver.execute_script("arguments[0].scrollIntoView();", waitForButton)
        waitForButton.click()
    else:
        driver.find_element_by_xpath("//div[contains(@label,'Current age')]//input[@type='text']").send_keys(Keys.TAB)


@then(u'Projected balance at retirement is shown on the screen as {projection}')
def step_impl(context,projection):
    driver=context.driver
    result="results-heading"
    result=KSCalculator(context).wait_for_element_to_load("class name","result-value")
    result=result.text
    assert result == "$\n"+projection