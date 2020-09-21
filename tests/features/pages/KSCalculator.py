from environment import fixture,get_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class KSCalculator():
    instance = None
    field_types={'Current age': 'text','Employment status': 'select','Current KiwiSaver balance': 'text',
            'Voluntary contributions': 'text','Frequency': 'select','Risk profile': 'radio','Savings goal at retirement': 'text',
            'Salary or wages per year (before tax)': 'text','KiwiSaver member contribution': 'radio' }

    def __init__(self,context):
        self.driver = get_driver(context)

    def populate_fields(self,field,value):
        if self.field_types[field]=='text':
            self.I_enter_text(field,value)
        elif self.field_types[field]=='select':
            self.I_select_dropdown(field,value)
        elif self.field_types[field]=='radio':
            self.I_choose_radio_button(field,value)
        else:
            print("Please pass the field name that is shown on the KiwiSaver Calulator Page")
            assert False

    def I_enter_text(self,field,value):
        field_path = "//div[contains(@label,'{}')]".format(field)
        value_path = field_path + "//input[@type='text']"
        g= self.driver.find_element_by_xpath(value_path)
        g.clear()
        g.send_keys(value)

    def I_select_dropdown(self,field,value):
        if value in [None,'','0']:
            return
        if field=="Frequency":
            field="Voluntary contributions"
        field_path = "//div[contains(@label,'{}')]".format(field)
        dropdown_path=field_path+"//div[contains(@class,'select-control')]"
        value_path = field_path + "//li/div/span"
        self.find_and_click_resource_using("xpath",dropdown_path)
        options=self.driver.find_elements_by_xpath(value_path)
        for option in options:
            if option.get_attribute('innerHTML').lower()==value.lower():
                option.click()
                break

    def I_choose_radio_button(self,field,value):
        field_path = "//div[contains(@label,'{}')]".format(field)
        value_path = field_path + "//span[@class='input-label']"
        radio_buttons=self.driver.find_elements_by_xpath(value_path)
        for button in radio_buttons:
            if button.text == value:
                button.click()

    def find_and_click_resource_using(self,locatorType,value):
        """
        The function waits for the resource to load and clicks it
        :param locatorType: Locator type ("id","xpath","link text","name""class name","css selector")
        :param value: Actual value of the locator i.e value of xpath of xpath,css,id etc.
        :return: Doesnt return anything
        """
        locatorType=locatorType.lower()
        resource=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (locatorType, value)))
        resource.click()

    def wait_for_element_to_load(self,locatorType,value):
        """
        The function waits for the widget to load and time's out after 10 sec if it doesnt find any
        :param locatorType: Locator type ("id","xpath","link text","name""class name","css selector")
        :param value: Locator value
        :return: Doesnt return anything
        """
        locatorType=locatorType.lower()
        res=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (locatorType, value)))
        return res

    def switch_to_frame(self):
        """
        This switches the frame to the specified iframe embed within the HTML
        """
        calFrame=self.wait_for_element_to_load("xpath","//iframe[starts-with(@src, '/calculator-widgets/kiwisaver-calculator/')]")
        self.driver.switch_to.frame(calFrame)