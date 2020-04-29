import pytest
from tests.pages.albums_page import AlbumsPage
from tests.pages.library_page import LibraryPage
from tests.pages.playlists_page import PlaylistsPage


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

    def test_search_area_presented_on_the_page(self, wd):
        library_page = LibraryPage(wd)
        library_page.click_on_library_tab()
        library_page.wait_for_page_is_loaded()
        assert library_page.search_form_presented_on_the_page()

    def test_count_of_songs_on_the_page(self, expectations, wd):
        library_page = LibraryPage(wd)
        library_page.click_on_library_tab()
        library_page.wait_for_page_is_loaded()
        assert library_page.get_count_of_songs_on_the_page() == expectations.get_songs_count()

    def test_check_songs_info_on_the_page(self, expectations, wd):
        library_page = LibraryPage(wd)
        library_page.click_on_library_tab()
        library_page.wait_for_page_is_loaded()
        result_dict = dict()
        for song_id in range(1, expectations.get_songs_count() + 1):
            song_df = expectations.get_song_df_by_id(song_id)
            visible_song = library_page.get_song_info_by_parent_id(song_id)
            result_dict[song_id] = song_df['title'].values[0] == visible_song['name'] and \
                                   song_df['artist'].values[0] == visible_song['artist'] and \
                                   song_df['album'].values[0] == visible_song['album'] and \
                                   song_df['duration'].values[0] == visible_song['duration']
        assert False not in result_dict.values(), 'Some of songs not as expected\n{}'.format(result_dict)

    def test_check_playlists_page_header(self, wd):
        playlists_page = PlaylistsPage(wd)
        playlists_page.click_on_playlists_tab()
        playlists_page.wait_for_page_is_loaded()
        assert playlists_page.playlists_page_header_presented_on_the_page()

    def test_check_add_playlist_button(self, wd):
        playlists_page = PlaylistsPage(wd)
        playlists_page.click_on_playlists_tab()
        playlists_page.wait_for_page_is_loaded()
        assert playlists_page.add_playlist_icon_presented_on_the_page()

    def test_check_count_of_playlists(self, expectations, wd):
        playlists_page = PlaylistsPage(wd)
        playlists_page.click_on_playlists_tab()
        playlists_page.wait_for_page_is_loaded()
        assert playlists_page.get_count_of_playlists_on_the_page() == expectations.get_playlists_count()
