from tests.helpers.webdriver_base import WebDriverBase


class TabsElements(WebDriverBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.ALBUMS_TAB_XPATH = "//*[text()='Albums']"
        self.PLAYLISTS_TAB_XPATH = "//*[text()='Playlists']"
        self.LIBRARY_TAB_XPATH = "//*[text()='Library']"

    def click_on_albums_tab(self):
        self.click_element_by_xpath(self.ALBUMS_TAB_XPATH)

    def click_on_playlists_tab(self):
        self.click_element_by_xpath(self.PLAYLISTS_TAB_XPATH)

    def click_on_library_tab(self):
        self.click_element_by_xpath(self.LIBRARY_TAB_XPATH)
