import pytest
from random import randint
import tests.helpers.data_generator as dg


class TestAPI:

    @pytest.mark.api
    def test_count_of_songs(self, api_communicator, expectations):
        response = api_communicator.send_query_request(schema='libraries',
                                                       values=['id', 'album', 'duration', 'title', 'artist'],
                                                       code=200)
        assert len(response['data']['libraries']) == expectations.get_count_of_songs()

    @pytest.mark.api
    def test_count_of_playlists(self, api_communicator):
        response = api_communicator.send_query_request(schema='playlists', values=['id', 'name'], code=200)
        assert type(response['data']['playlists']) is list
        assert len(response['data']['playlists']) is 0

    @pytest.mark.api
    def test_count_of_playlists_with_songs_parameter(self, api_communicator):
        response = api_communicator.send_query_request(schema='playlists',
                                                       values=['id', 'name', 'songs {\nid\nartist}'],
                                                       code=200)
        assert type(response['data']['playlists']) is list
        assert len(response['data']['playlists']) is 0

    @pytest.mark.api
    def test_get_the_first_playlist(self, api_communicator):
        response = api_communicator.send_query_request(schema='playlist(id: 0)',
                                                       values=['id', 'name'], code=200)
        assert response['data']['playlist'] is None

    @pytest.mark.api
    def test_get_correct_random_song(self, api_communicator, expectations):
        song_id = randint(1, expectations.get_count_of_songs())
        response = api_communicator.send_query_request(
            schema='library(id: {})'.format(song_id),
            values=['id', 'album', 'duration', 'title', 'artist'],
            code=200)
        assert response['data']['library'] is not None
        assert response['data']['library'] == expectations.get_song_by_id(song_id).to_dict()

    @pytest.mark.api
    def test_get_song_low_boundary(self, api_communicator, expectations):
        response = api_communicator.send_query_request(
            schema='library(id: 1)', values=['id', 'album', 'duration', 'title', 'artist'], code=200)
        assert response['data']['library'] is not None
        assert response['data']['library'] == expectations.get_song_by_id(id=1).to_dict()

    @pytest.mark.api
    def test_get_song_out_of_low_boundary(self, api_communicator):
        response = api_communicator.send_query_request(
            schema='library(id: 0)', values=['id', 'album', 'duration', 'title', 'artist'], code=200)
        assert response['data']['library'] is None

    @pytest.mark.api
    def test_get_song_high_boundary(self, api_communicator, expectations):
        response = api_communicator.send_query_request(
            schema='library(id: {})'.format(expectations.get_count_of_songs()),
            values=['id', 'album', 'duration', 'title', 'artist'],
            code=200)
        assert response['data']['library'] is not None
        assert response['data']['library'] == expectations.get_song_by_id(expectations.get_count_of_songs()).to_dict()

    @pytest.mark.api
    def test_get_song_out_of_high_boundary(self, api_communicator, expectations):
        response = api_communicator.send_query_request(
            schema='library(id: {})'.format(expectations.get_count_of_songs() + 1),
            values=['id', 'album', 'duration', 'title', 'artist'],
            code=200)
        assert response['data']['library'] is None

    @pytest.mark.api
    def test_create_correct_empty_playlist(self, api_communicator, expectations):
        expectations.update_playlists_df()
        count_of_playlists = expectations.get_playlists_count()
        response = api_communicator.send_mutation_request(
            func='createPlaylist(name: "{}")'.format(dg.generate_random_name(8)),
            values=['id'],
            code=200)
        assert response['data']['createPlaylist'] is not None
        expectations.update_playlists_df()
        assert count_of_playlists + 1 == expectations.get_playlists_count()

    @pytest.mark.api
    def test_create_empty_playlist_with_empty_name(self, api_communicator, expectations):
        expectations.update_playlists_df()
        count_of_playlists = expectations.get_playlists_count()
        response = api_communicator.send_mutation_request(
            func='createPlaylist(name: "")',
            values=['id'],
            code=400)
        expectations.update_playlists_df()
        assert count_of_playlists == expectations.get_playlists_count()

    @pytest.mark.api
    def test_create_correct_empty_playlist_with_long_name(self, api_communicator, expectations):
        expectations.update_playlists_df()
        count_of_playlists = expectations.get_playlists_count()
        response = api_communicator.send_mutation_request(
            func='createPlaylist(name: "{}")'.format(dg.generate_random_name(129)),
            values=['id'],
            code=200)
        assert response['data']['createPlaylist'] is not None
        expectations.update_playlists_df()
        assert count_of_playlists + 1 == expectations.get_playlists_count()

    @pytest.mark.api
    def test_create_correct_playlist_with_songs(self, api_communicator, expectations):
        expectations.update_playlists_df()
        count_of_playlists = expectations.get_playlists_count()
        songs_for_attaching = dg.get_random_sequence_of_numbers(4, expectations.songs_df['id'].count())

        response = api_communicator.send_mutation_request(
            func='createPlaylist(name: "{}", songs: [{}])'.format(dg.generate_random_name(8),
                                                                  ', '.join(songs_for_attaching)),
            values=['id'],
            code=200)
        assert response['data']['createPlaylist'] is not None
        expectations.update_playlists_df()
        assert count_of_playlists + 1 == expectations.get_playlists_count()
        created_playlist = response['data']['createPlaylist']['id']

        response = api_communicator.send_query_request(
            schema='playlist(id: {})'.format(created_playlist),
            values=['id', 'name', 'songs {\nid }'],
            code=200)
        assert response['data']['playlist'] is not None
        assert sorted([x['id'] for x in response['data']['playlist']['songs']]) == sorted([int(x) for x in songs_for_attaching])

    @pytest.mark.api
    def test_create_playlist_with_incorrect_songs(self, api_communicator, expectations):
        expectations.update_playlists_df()
        count_of_playlists = expectations.get_playlists_count()

        response = api_communicator.send_mutation_request(
            func='createPlaylist(name: "{}", songs: [{}])'.format(dg.generate_random_name(8),
                                                                  expectations.get_count_of_songs() + 10),
            values=['id'],
            code=400)
        assert response['data']['createPlaylist'] is not None
