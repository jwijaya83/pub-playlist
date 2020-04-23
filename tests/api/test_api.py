import pytest
from tests.constants import PlaylistConstants as const
from random import randint


class TestAPI:

    @pytest.mark.api
    def test_count_of_songs(self, api_communicator):
        response = api_communicator.send_query_request(schema='libraries', values=['id'], code=200)
        assert len(response['data']['libraries']) == const.DEFAULT_COUNT_OF_SONGS

    @pytest.mark.api
    def test_count_of_playlists(self, api_communicator):
        response = api_communicator.send_query_request(schema='playlists', values=['id'], code=200)
        assert response['data']['playlists'] is None

    @pytest.mark.api
    def test_get_correct_random_song(self, api_communicator):
        response = api_communicator.send_query_request(
            schema='library(id: {})'.format(randint(0, const.DEFAULT_COUNT_OF_SONGS)),
            values=['id', 'album', 'duration', 'title', 'artist'],
            code=200)
        assert response['data']['library'] is not None

    @pytest.mark.api
    def test_get_song_low_boundary(self, api_communicator):
        response = api_communicator.send_query_request(
            schema='library(id: 0)', values=['id', 'album', 'duration', 'title', 'artist'], code=200)
        assert response['data']['library'] is not None

    @pytest.mark.api
    def test_get_song_out_of_low_boundary(self, api_communicator):
        response = api_communicator.send_query_request(
            schema='library(id: -1)', values=['id', 'album', 'duration', 'title', 'artist'], code=200)
        assert response['data']['library'] is None

    @pytest.mark.api
    def test_get_song_high_boundary(self, api_communicator):
        response = api_communicator.send_query_request(
            schema='library(id: {})'.format(const.DEFAULT_COUNT_OF_SONGS - 1),
            values=['id', 'album', 'duration', 'title', 'artist'],
            code=200)
        assert response['data']['library'] is not None

    @pytest.mark.api
    def test_get_song_out_of_high_boundary(self, api_communicator):
        response = api_communicator.send_query_request(
            schema='library(id: {})'.format(const.DEFAULT_COUNT_OF_SONGS),
            values=['id', 'album', 'duration', 'title', 'artist'],
            code=200)
        assert response['data']['library'] is None
