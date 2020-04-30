from .tabs_elements import TabsElements


class LibraryPage(TabsElements):
    SEARCH_FORM_XPATH = "//input[@type='text']"
    LIBRARY_AREA_XPATH = "//*[@class='Library']"
    SONG_ELEMENT_XPATH_TEMPLATE = "//*[@id='Song-{}']"
    SONG_NAME_XPATH_TEMPLATE = "//*[@id='Song-{}']//*[@class='name']"
    SONG_ARTIST_XPATH_TEMPLATE = "//*[@id='Song-{}']//*[@class='artist']"
    SONG_ALBUM_XPATH_TEMPLATE = "//*[@id='Song-{}']//*[@class='album']"
    SONG_DURATION_XPATH_TEMPLATE = "//*[@id='Song-{}']//*[@class='duration']"

    def wait_for_page_is_loaded(self):
        self.wait_for_element_not_presented_by_xpath(self.LOADING_INSCRIPTION_XPATH)

    def search_form_presented_on_the_page(self):
        return self.is_element_presented_by_xpath(self.SEARCH_FORM_XPATH)

    def get_count_of_songs_on_the_page(self):
        return self.get_count_of_child_items_for_parent_element_by_xpath(self.LIBRARY_AREA_XPATH, 'div')

    def get_song_info_by_parent_id(self, id):
        assert self.is_element_presented_by_xpath(self.SONG_ELEMENT_XPATH_TEMPLATE.format(id))
        song_info = dict()
        song_info['name'] = self.get_element_text_by_xpath(self.SONG_NAME_XPATH_TEMPLATE.format(id))
        song_info['artist'] = self.get_element_text_by_xpath(self.SONG_ARTIST_XPATH_TEMPLATE.format(id))
        song_info['album'] = self.get_element_text_by_xpath((self.SONG_ALBUM_XPATH_TEMPLATE.format(id)))
        song_info['duration'] = int(self.get_element_text_by_xpath(self.SONG_DURATION_XPATH_TEMPLATE.format(id)).split()[-1])
        return song_info
