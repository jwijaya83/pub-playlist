import pytest
from tests.pages.albums_page import AlbumsPage


class TestPlaylistifyUI:

    @pytest.mark.ui
    def test_albums_page_header_presented_on_the_page(self, wd):
        albums_page = AlbumsPage(wd)
        assert albums_page.albums_page_header_presented_on_the_page()

    @pytest.mark.ui
    def test_count_of_playlists_on_the_page(self, expectations, wd):
        albums_page = AlbumsPage(wd)
        assert albums_page.get_count_of_albums_on_the_page() == expectations.get_albums_count()

    @pytest.mark.ui
    def test_artists_names_on_the_page(self, expectations, wd):
        albums_page = AlbumsPage(wd)
        artists_names = expectations.get_list_of_artists()
        for artist in artists_names:
            assert albums_page.artist_name_presented_on_the_page(artist)

    @pytest.mark.ui
    def test_albums_names_on_the_page(self, expectations, wd):
        albums_page = AlbumsPage(wd)
        albums_names = expectations.get_list_of_albums()
        for album in albums_names:
            assert albums_page.artist_name_presented_on_the_page(album)

    @pytest.mark.ui
    def test_check_albums_content(self, expectations, wd):
        albums_page = AlbumsPage(wd)
        albums_names = expectations.get_list_of_albums()
        result_dict = dict()
        for album in albums_names:
            songs_in_album = expectations.get_songs_in_album(album)
            result_dict[album] = True
            if not albums_page.album_name_presented_on_the_page(album):
                result_dict[album] = False
            else:
                albums_page.hover_mouse_over_album(album)
                visible_songs = [albums_page.song_name_presented_on_the_page(song) for song in songs_in_album]
                if False in visible_songs:
                    result_dict[album] = False
        assert False not in result_dict.values(), 'Some of albums not full!\n{}'.format(result_dict)
