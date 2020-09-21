from behave import fixture, use_fixture, model
from selenium import webdriver
#from selenium.webdriver.chrome.options import Options as ChromeOptions
#from selenium.webdriver.firefox.options import Options as FFOptions
from webdriver_manager.chrome import ChromeDriverManager

@fixture
def browser(context):
    if 'browser' in context.config.userdata:
        if context.config.userdata['browser'] is not None:
            browser_name=context.config.userdata['browser'].lower()
            use_fixture(eval(browser_name),context)
    else:
        use_fixture(chrome,context)

def chrome(context):
    context.driver = webdriver.Chrome()
    yield context.driver

def firefox(context):
    context.driver = webdriver.Firefox()
    yield context.driver


def before_all(context):
    use_fixture(browser, context)
    context.driver.get("https://www.westpac.co.nz/")
    context.driver.maximize_window()

def get_driver(context):
    return context.driver

def after_all(context):
    context.driver.quit()