import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import datetime


class WebDriverBase:
    def __init__(self, driver):
        self.driver = driver

    def click_element_by_xpath(self, path):
        print('Click on element with xpath "{}"'.format(path))
        self.driver.find_element_by_xpath(path).click()

    def wait_for_text_presented_on_the_page(self, expected_text):
        finish = time.time() + 30
        while time.time() <= finish and not self.is_text_presented_on_the_page(expected_text):
            print("Element with text '{}' still not loaded. Try again in 1 second...".format(expected_text))
            time.sleep(1)
        result = self.is_text_presented_on_the_page(expected_text)
        if not result:
            raise AssertionError("Element with text: '{}' not present".format(expected_text))

    def is_text_presented_on_the_page(self, expected_text):
        try:
            print('Trying to find "{}" on the page'.format(expected_text))
            return expected_text in self.driver.find_element_by_css_selector("html>body").text
        except:
            print("Text: '{}' not presented".format(expected_text))
            return False

    def wait_for_element_presented_by_xpath(self, xpath):
        finish = time.time() + 30
        while time.time() <= finish and not self.is_element_presented_by_xpath(xpath):
            print("Element with xpath '{}' still not loaded. Try again in 1 second...".format(xpath))
            time.sleep(1)
        result = self.is_element_presented_by_xpath(xpath)
        if not result:
            raise AssertionError('Element with xpath {} not presented, but expected'.format(xpath))

    def is_element_presented_by_xpath(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
            print("check if Element by xpath is present: '{}'".format(xpath))
            return True
        except:
            print("Element by xpath: '{}' is not present".format(xpath))
            return False

    def get_count_of_child_items_for_parent_element_by_xpath(self, parent_el_xpath, child_el_tag):
        assert self.is_element_presented_by_xpath(parent_el_xpath)
        return len(self.driver.find_elements_by_xpath('{}/{}'.format(parent_el_xpath, child_el_tag)))

    def get_texts_of_child_items_for_parent_element_by_xpath(self, parent_el_xpath, child_el_xpath):
        if self.get_count_of_child_items_for_parent_element_by_xpath(parent_el_xpath, 'div') != 0:
            songs = self.driver.find_elements_by_xpath('{}{}'.format(parent_el_xpath, child_el_xpath))
            return [song.get_attribute('title') for song in songs]
        return []

    def js_mouse_hover(self, element):
        """
        Calls mouse hover event using Java Script
        :param element - Web Element
        """
        self.driver.execute_async_script(self.driver, "doFireEvent", element, "mouseover")

    def get_element_class_by_id(self, id):
        """
        get element by id
        :param id
        """
        print("click on id {}".format(id))
        ele_class = self.driver.find_element_by_id(id).get_attribute("class")
        return ele_class

    def get_elements_by_css_selector_manydays(self, css_selector):
        """
        get element by class many-days
        :param none
        """
        element_dict = {}
        elements = self.driver.find_elements_by_css_selector(css_selector)
        for element in elements:
            print(element.get_attribute("class"))
            print(element.get_attribute("id"))
            if element.get_attribute("class") == "source-item many-days":
                element_dict[element.get_attribute("id")] = element.get_attribute("class")
        return element_dict

    def get_elements_by_css_selector_twodays(self, css_selector):
        """"
        get element by class two-days
        :param none
        """
        element_dict = {}
        elements = self.driver.find_elements_by_css_selector(css_selector)
        for element in elements:
            print(element.get_attribute("class"))
            print(element.get_attribute("id"))
            if element.get_attribute("class") == "source-item two-days":
                element_dict[element.get_attribute("id")] = element.get_attribute("class")
        return element_dict

    def js_mouse_down(self, element):
        """
        Calls mouse down event using Java Script
        :param element - Web Element
        """
        self.driver.execute_async_script(self.driver, "doFireEvent", element, "mousedown")

    def js_mouse_up(self, element):
        """
        Calls mouse up event using Java Script
        :param element - Web Element
        """
        self.driver.execute_async_script(self.driver, "doFireEvent", element, "mouseup")

    def mouse_hover(self, element):
        """
        Calls mouse hover using actions
        :param element - Web Element
        """
        actionChains = ActionChains(self.driver)
        actionChains.move_to_element(element)
        actionChains.perform()

    def mouse_hover_by_css_selector(self, css_selector):
        """
        Calls mouse hover by Css
        :param element - Web Element
        """
        element = self.driver.find_element_by_css_selector(css_selector)
        self.mouse_hover(element)

    def mouse_hover_by_id(self, id):
        """
        Calls mouse hover by Id
        :param element - Web Element
        """
        element = self.driver.find_element_by_id(id)
        self.mouse_hover(element)

    def mouse_hover_by_xpath(self, xpath):
        """
        Calls mouse hover by Id
        :param element - Web Element
        """
        element = self.driver.find_element_by_xpath(xpath)
        self.mouse_hover(element)

    def type_text_by_css_selector(self, text, css_selector, clear = None):
        """
        Type Text
        :param element - text, locator
        """
        element = self.driver.find_element_by_css_selector(css_selector)
        element.click()
        if clear != False:
            element.clear()
        element.send_keys(text)

    def type_text_by_xpath(self, text, locator, clear = None):
        """
        Type Text
        :param element - text, locator
        """
        element = self.driver.find_element_by_xpath(locator)
        element.click()
        if clear != False:
            element.clear()
        element.send_keys(text)

    def type_text_by(self, text, byCriteria, value):
        """
        Type Text by criteria
        :param element - text, locator
        """
        element = self.driver.find_element(by=byCriteria, value=value)
        self.filling_text_to_element(element, text)

    def filling_text_to_element(self, element, text):
        """
        Filling text to selected element
        :param element: selected element
        :param text: text for inserting
        :return:
        """
        element.click()
        element.clear()
        element.send_keys(text)

    def type_text_by_id(self, text, elementId):
        """
        Type Text by id
        :param element - text, id
        """
        element = self.driver.find_element_by_id(elementId)
        self.filling_text_to_element(element, text)

    def type_text_by_name(self, text, elementName):
        """
        Type Text
        :param element - text, name
        """
        element = self.driver.find_element_by_name(elementName)
        self.filling_text_to_element(element, text)

    def search_text_by_css_selector(self, text, css_selector, clear = None):
        """
        Search Text
        :param element - text, id
        """
        element = self.driver.find_element_by_css_selector(css_selector)
        element.click()
        if clear != False:
            element.clear()
        element.send_keys(text, Keys.RETURN)

    def click_element_by_css_selector(self, css_selector):
        """
        Click Element
        :param element - text, locator
        """
        self.driver.find_element_by_css_selector(css_selector).click()

    def click_element_by_id(self, id):
        """
        Click Element
        :param element - id
        """
        print('Click on element with id {}'.format(id))
        self.driver.find_element_by_id(id).click()

    def click_element_by_name(self, name):
        """
        Click Element by name
        :param element - name
        """
        self.driver.find_element_by_name(name).click()

    def click_element_by_link_text(self, text):
        """
        Click button by text
        :param element - link-text
        """
        self.driver.find_element_by_link_text(text).click()

    def click_element_by_xpath(self, path):
        """
        Click button by xpath
        :param element - xpath
        """
        print('Click on element with xpath "{}"'.format(path))
        self.driver.find_element_by_xpath(path).click()

    def open_url(self, url):
        """
        Open URL
        :param- URL
        """
        self.driver.get(url)

    def close_alert(self):
        """
        lose alert if present when open URL
        :param - none
        """
        try:
            alert = self.driver.switch_to.alert()
            alert.accept()
        except:
            pass

    def click_text_by_css_selector(self, textExpected, css_selector):
        """
        clicks certain element. It can be button, radio button and so on.
        :param- text, locator
        """
        webElements = self.driver.find_elements_by_css_selector(css_selector)
        for element in webElements:
            if element.text == textExpected:
                element.click()
                return

    def click_text_by_id(self, textExpected, id):
        """
        clicks certain element. It can be button, radio button and so on.
        :param- text, id
        """
        webElements = self.driver.find_elements_by_id(id)
        for element in webElements:
            if element.text == textExpected:
                element.click()
                return

    def double_click_on_element(self, webElement):
        """
        Double click on element
        :param - element
        """
        ActionChains(self.driver).double_click(webElement).perform()

    def double_click_on_element_by_id(self, elementId):
        """
        Double click element by Id
        :param - elementId
        """
        self.double_click_on_element(self.driver.find_element_by_id(elementId))

    def double_click_on_element_by_css_selector(self, css_selector):
        """
        Double click element by Id
        :param - locator
        """
        self.double_click_on_element(self.driver.find_element_by_css_selector(css_selector))

    def select_checkbox_by_css_selector(self, css_selector):
        """
        Checkbox - check/uncheck
        :param - locator
        """
        checkBox = self.driver.find_element_by_css_selector(css_selector)
        checkBox.click()

    def select_checkbox_by_id(self, elementId):
        """
        Checkbox - check/uncheck by Id
        :param - locator
        """
        checkBox = self.driver.find_element_by_id(elementId)
        checkBox.click()

    def verify_element_text_by_css_selector(self, expectedText, css_selector):
        """
       Verify element text
       :param - text, locator
       """
        element = self.driver.find_element_by_css_selector(css_selector)
        assert expectedText == element.text, 'Element has text {}, but expected {}.'.format(element.text, expectedText)

    def get_element_text_by_css_selector(self, css_selector):
        """
        get element text
       :param -  locator
       """
        element = self.driver.find_element_by_css_selector(css_selector)
        return element.text

    def get_element_text_by_id(self, id):
        """
        get element text by id
       :param -  id
       """
        element = self.driver.find_element_by_id(id)
        return element.text

    def get_element_text_by_xpath(self, xpath):
        """
        get element text by XPATH
       :param -  xpath
       """
        element = self.driver.find_element_by_xpath(xpath)
        return element.text

    def get_element_property_value_by_xpath(self, xpath, property):
        """
        Get element property value
        :param xpath: xpath to element
        :param property: needed property
        :return: property value
        """
        return self.driver.find_element_by_xpath(xpath).get_property(property)

    def get_element_attribute_by_css_selector(self, css_selector, attribute):
        """
       Verify element attribute
       :param - attribute
       """
        try:
            element = self.driver.find_element_by_css_selector(css_selector)
            elementAttribute = element.get_attribute(attribute)
            return elementAttribute
        except:
            return "Attribute not found"

    def select_drop_down_item_by_css_selector(self, item, css_selector):
        """
       Select Drop Down Item
       :param - item, locator
       """
        oSingleSelection = Select(self.driver.find_element_by_css_selector(css_selector))
        oSingleSelection.select_by_visible_text(item)

    def get_selected_drop_down_item(self, locator):
        """
       get Selected Drop Down Item
       :param - locator
       """
        try:
            oSingleSelection = Select(self.driver.find_element_by_css_selector(locator))
            return oSingleSelection.first_selected_option.text
        except:
            return "selected drop down item not found"

    def upload(self, locator, fileLocation):
        """
       upload a file
       :param - locator, filelocation
       """
        self.driver.find_element_by_css_selector(locator).send_keys(fileLocation)

    def upload_by_element_id(self, id, fileLocation):
        """
       upload a file
       :param - id, filelocation
       """
        print('Start uploading file with path {}'.format(fileLocation))
        self.driver.find_element_by_id(id).send_keys(fileLocation)

    def select_value_from_list(self, css_selector, value):
        """
       select a item in a list
       :param - locator, value
       """
        webElement = self.driver.find_element_by_css_selector(css_selector)
        webElementsList = webElement.find_elements_by_tag_name("option")

        for element in webElementsList:
            if element.text == value:
                element.click()
                return

    def refresh(self):
        """
       refresh page
       :param - none
       """
        self.driver.refresh()

    def delete_cookies(self, name):
        """
       refresh page
       :param - none
       """
        self.driver.delete_cookie(name)

    def take_screenshot(self, filename, save_location):
        """
        Save a screenshot of the current page.
        :param filename The name of the file to save
        :param save_location Where to save the screenshot
        """
        time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        self.driver.get_screenshot_as_file(save_location + '//' + time + '_' + filename + '.png')

    def scroll_down(self, locator):
        # self.driver.find_element_by_css_selector(locator).send_keys(Keys.END)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

    def get_opened_url(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        opened_url = self.driver.current_url
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        return opened_url

    def wait_for_element_not_presented_by_xpath(self, xpath):
        finish = time.time() + 30
        while time.time() <= finish and self.is_element_presented_by_xpath(xpath):
            print("Element with xpath '{}' still visible. Try again in 1 second...".format(xpath))
            time.sleep(1)
        result = not self.is_element_presented_by_xpath(xpath)
        if not result:
            raise AssertionError('Element with xpath {} presented, but not expected'.format(xpath))
