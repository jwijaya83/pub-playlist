from tests.helpers.webdriver_base import WebDriverBase


class TabsElements(WebDriverBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.ALBUMS_TAB_XPATH = "//*[text()='Albums']"
        self.PLAYLISTS_TAB_XPATH = "//*[text()='Playlists']"
        self.LIBRARY_TAB_XPATH = "//*[text()='Library']"
        self.LOADING_INSCRIPTION_XPATH = "//*[text()='Loading...']"

    def click_on_albums_tab(self):
        self.wait_for_element_not_presented_by_xpath(self.LOADING_INSCRIPTION_XPATH)
        self.click_element_by_xpath(self.ALBUMS_TAB_XPATH)
        self.wait_for_element_not_presented_by_xpath(self.LOADING_INSCRIPTION_XPATH)

    def click_on_playlists_tab(self):
        self.wait_for_element_not_presented_by_xpath(self.LOADING_INSCRIPTION_XPATH)
        self.click_element_by_xpath(self.PLAYLISTS_TAB_XPATH)
        self.wait_for_element_not_presented_by_xpath(self.LOADING_INSCRIPTION_XPATH)

    def click_on_library_tab(self):
        self.wait_for_element_not_presented_by_xpath(self.LOADING_INSCRIPTION_XPATH)
        self.click_element_by_xpath(self.LIBRARY_TAB_XPATH)
        self.wait_for_element_not_presented_by_xpath(self.LOADING_INSCRIPTION_XPATH)

    def albums_tab_presented_on_the_page(self):
        return self.is_element_presented_by_xpath(self.ALBUMS_TAB_XPATH)

    def playlists_tab_presented_on_the_page(self):
        return self.is_element_presented_by_xpath(self.PLAYLISTS_TAB_XPATH)

    def library_tab_presented_on_the_page(self):
        return self.is_element_presented_by_xpath(self.LIBRARY_TAB_XPATH)
