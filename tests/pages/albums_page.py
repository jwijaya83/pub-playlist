from .tabs_elements import TabsElements


class AlbumsPage(TabsElements):
    ALBUMS_AREA_XPATH = "//*[@class='albums']"
    ALBUMS_HEADER_TEXT = "Top Albums"

    def get_count_of_albums_on_the_page(self):
        return self.get_count_of_child_items_for_parent_element_by_xpath(self.ALBUMS_AREA_XPATH, 'div')

    def artist_name_presented_on_the_page(self, name):
        return self.is_text_presented_on_the_page(name)

    def album_name_presented_on_the_page(self, name):
        return self.is_text_presented_on_the_page(name)

    def hover_mouse_over_album(self, name: str):
        self.mouse_hover_by_xpath('//*[text()="{}" and @class="name"]'.format(name))

    def song_name_presented_on_the_page(self, name: str):
        return self.is_text_presented_on_the_page(name)

    def albums_page_header_presented_on_the_page(self):
        return self.is_text_presented_on_the_page(self.ALBUMS_HEADER_TEXT)

    def wait_for_page_is_loaded(self):
        self.wait_for_element_not_presented_by_xpath(self.LOADING_INSCRIPTION_XPATH)
