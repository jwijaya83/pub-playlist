from .tabs_elements import TabsElements


class PlaylistsPage(TabsElements):
    PLAYLISTS_HEADER_TEXT = 'My Playlists'
    ADD_PLAYLIST_ICON_XPATH = "//span[@class='material-icons' and text()='add']"
    PLAYLISTS_AREA_XPATH = "//*[@class='playlists']"
    PLAYLIST_XPATH_TEMPLATE = "//*[@id='playlist-{}']"
    PLAYLIST_NAME_XPATH_TEMPLATE = "//*[@id='playlist-{}']//*[@class='name']"
    PLAYLIST_SONGS_ROOT_XPATH_TEMPLATE = "//*[@id='playlist-{}']//*[@class='songs']"

    def get_count_of_playlists_on_the_page(self):
        return self.get_count_of_child_items_for_parent_element_by_xpath(self.PLAYLISTS_AREA_XPATH, 'div')

    def playlists_page_header_presented_on_the_page(self):
        return self.is_text_presented_on_the_page(self.PLAYLISTS_HEADER_TEXT)

    def add_playlist_icon_presented_on_the_page(self):
        return self.is_element_presented_by_xpath(self.ADD_PLAYLIST_ICON_XPATH)

    def wait_for_page_is_loaded(self):
        self.wait_for_element_not_presented_by_xpath(self.LOADING_INSCRIPTION_XPATH)

    def get_playlist_name_by_id(self, id):
        assert self.is_element_presented_by_xpath(self.PLAYLIST_XPATH_TEMPLATE.format(id))
        res_dict = dict()
        res_dict['name'] = self.get_element_text_by_xpath(self.PLAYLIST_NAME_XPATH_TEMPLATE.format(id))
        res_dict['songs'] = self.get_texts_of_child_items_for_parent_element_by_xpath(self.PLAYLIST_SONGS_ROOT_XPATH_TEMPLATE.format(id),
                                                                                      "//*[@class='playlist-track-title']")
        return res_dict
