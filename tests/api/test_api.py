import pytest
from random import randint
from tests.helpers.data_generator import DataGenerator as dg
from time import sleep


class TestAPI:

    @pytest.mark.api
    def test_count_of_songs(self, api_communicator, expectations):
        response = api_communicator.send_query_request(schema='libraries',
                                                       values=['id', 'album', 'duration', 'title', 'artist'],
                                                       code=200)
        assert len(response['data']['libraries']) == expectations.get_songs_count()

    @pytest.mark.api
    def test_count_of_playlists(self, api_communicator, expectations):
        response = api_communicator.send_query_request(schema='playlists', values=['id', 'name'], code=200)
        assert type(response['data']['playlists']) is list
        assert len(response['data']['playlists']) == expectations.get_playlists_count()

    @pytest.mark.api
    def test_count_of_playlists_with_songs_parameter(self, api_communicator, expectations):
        response = api_communicator.send_query_request(schema='playlists',
                                                       values=['id', 'name', 'songs {\nid\nartist}'],
                                                       code=200)
        assert type(response['data']['playlists']) is list
        assert len(response['data']['playlists']) == expectations.get_playlists_count()

    @pytest.mark.api
    def test_check_playlists_low_boundary(self, api_communicator):
        response = api_communicator.send_query_request(schema='playlist(id: 1)',
                                                       values=['id', 'name'], code=200)
        assert response['data']['playlist'] is not None

    @pytest.mark.api
    def test_check_playlists_out_of_low_boundary(self, api_communicator):
        response = api_communicator.send_query_request(schema='playlist(id: 0)',
                                                       values=['id', 'name'], code=200)
        assert response['data']['playlist'] is None

    @pytest.mark.api
    def test_check_playlists_high_boundary(self, api_communicator, expectations):
        response = api_communicator.send_query_request(schema='playlist(id: {})'.format(expectations.get_highest_playlist_id()),
                                                       values=['id', 'name'], code=200)
        assert response['data']['playlist'] is not None

    @pytest.mark.api
    def test_check_playlists_out_of_high_boundary(self, api_communicator, expectations):
        response = api_communicator.send_query_request(schema='playlist(id: {})'.format(expectations.get_highest_playlist_id() + 1),
                                                       values=['id', 'name'], code=200)
        assert response['data']['playlist'] is None

    @pytest.mark.api
    def test_get_correct_random_song(self, api_communicator, expectations):
        song_id = randint(1, expectations.get_songs_count())
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
            schema='library(id: {})'.format(expectations.get_songs_count()),
            values=['id', 'album', 'duration', 'title', 'artist'],
            code=200)
        assert response['data']['library'] is not None
        assert response['data']['library'] == expectations.get_song_by_id(expectations.get_songs_count()).to_dict()

    @pytest.mark.api
    def test_get_song_out_of_high_boundary(self, api_communicator, expectations):
        response = api_communicator.send_query_request(
            schema='library(id: {})'.format(expectations.get_songs_count() + 1),
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
        assert response['data']['createPlaylist'] is not None, print(response['data'])
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
        assert response['data']['createPlaylist'] is None
        expectations.update_playlists_df()
        assert count_of_playlists == expectations.get_playlists_count()

    @pytest.mark.api
    def test_create_empty_playlist_with_existing_name(self, api_communicator, expectations):
        expectations.update_playlists_df()
        count_of_playlists = expectations.get_playlists_count()
        response = api_communicator.send_mutation_request(
            func='createPlaylist(name: "{}")'.format(expectations.get_playlist_name_by_id(randint(1, count_of_playlists))),
            values=['id'],
            code=400)
        assert response['data']['createPlaylist'] is None
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
        count_of_songs_in_playlists = expectations.get_count_of_songs_in_playlists()

        response = api_communicator.send_mutation_request(
            func='createPlaylist(name: "{}", songs: [{}])'.format(dg.generate_random_name(8),
                                                                  expectations.get_songs_count() + 1),
            values=['id'],
            code=200)
        assert response['data']['createPlaylist'] is not None
        expectations.update_playlists_df()
        assert count_of_playlists + 1 == expectations.get_playlists_count()
        assert count_of_songs_in_playlists == expectations.get_count_of_songs_in_playlists()

    @pytest.mark.api
    def test_create_playlist_with_all_songs(self, api_communicator, expectations):
        expectations.update_playlists_df()
        count_of_playlists = expectations.get_playlists_count()
        count_of_songs_in_playlists = expectations.get_count_of_songs_in_playlists()
        count_of_songs = expectations.get_songs_count()

        response = api_communicator.send_mutation_request(
            func='createPlaylist(name: "{}", songs: {})'.format(dg.generate_random_name(8),
                                                                str([x for x in range(1, count_of_songs + 1)])),
            values=['id'],
            code=200)
        assert response['data']['createPlaylist'] is not None
        sleep(0.3)
        expectations.update_playlists_df()
        assert count_of_playlists + 1 == expectations.get_playlists_count()
        assert count_of_songs_in_playlists + count_of_songs == expectations.get_count_of_songs_in_playlists()

    @pytest.mark.api
    def test_change_playlist_name_to_new_name(self, api_communicator, expectations):
        expectations.update_playlists_df()
        count_of_playlists = expectations.get_playlists_count()
        id_playlist_for_change = randint(1, count_of_playlists)
        new_name = dg.generate_random_name(8)

        response = api_communicator.send_mutation_request(
            func='editPlaylist(id: {}, name: "{}")'.format(id_playlist_for_change, new_name),
            values=['id'],
            code=200)
        assert response['data']['editPlaylist'] is not None
        expectations.update_playlists_df()
        assert count_of_playlists == expectations.get_playlists_count()
        assert expectations.get_playlist_name_by_id(id_playlist_for_change) == new_name

    @pytest.mark.api
    def test_change_playlist_name_to_the_same_name(self, api_communicator, expectations):
        expectations.update_playlists_df()
        count_of_playlists = expectations.get_playlists_count()
        id_playlist_for_change = randint(1, count_of_playlists)
        name = expectations.get_playlist_name_by_id(id_playlist_for_change)

        response = api_communicator.send_mutation_request(
            func='editPlaylist(id: {}, name: "{}")'.format(id_playlist_for_change, name),
            values=['id'],
            code=200)
        assert response['data']['editPlaylist'] is not None
        expectations.update_playlists_df()
        assert count_of_playlists == expectations.get_playlists_count()
        assert expectations.get_playlist_name_by_id(id_playlist_for_change) == name

    @pytest.mark.api
    def test_change_playlist_name_to_the_empty_name(self, api_communicator, expectations):
        expectations.update_playlists_df()
        count_of_playlists = expectations.get_playlists_count()
        id_playlist_for_change = randint(1, count_of_playlists)
        name = expectations.get_playlist_name_by_id(id_playlist_for_change)

        response = api_communicator.send_mutation_request(
            func='editPlaylist(id: {}, name: "")'.format(id_playlist_for_change),
            values=['id'],
            code=400)
        assert response['data']['editPlaylist'] is not None
        expectations.update_playlists_df()
        assert count_of_playlists == expectations.get_playlists_count()
        assert expectations.get_playlist_name_by_id(id_playlist_for_change) == name

    @pytest.mark.api
    def test_add_correct_song_to_playlist(self, api_communicator, expectations):
        expectations.update_playlists_df()
        count_of_playlists = expectations.get_playlists_count()
        playlists_with_songs = expectations.get_playlists_with_songs(not_full=True)
        id_playlist_for_change = playlists_with_songs[randint(0, len(playlists_with_songs) - 1)]
        songs = expectations.get_songs_from_playlist_by_id(id_playlist_for_change)
        songs_for_update = sorted(dg.add_random_songs_to_list(randint(1, 4), songs, expectations.get_songs_count()))

        response = api_communicator.send_mutation_request(
            func='editPlaylist(id: {}, songs: {})'.format(id_playlist_for_change, songs_for_update),
            values=['id'],
            code=200)
        assert response['data']['editPlaylist'] is not None
        sleep(0.3)
        expectations.update_playlists_df()
        assert count_of_playlists == expectations.get_playlists_count()
        assert sorted(list(expectations.get_songs_from_playlist_by_id(id_playlist_for_change))) == songs_for_update

    @pytest.mark.api
    def test_add_incorrect_song_to_playlist(self, api_communicator, expectations):
        expectations.update_playlists_df()
        count_of_playlists = expectations.get_playlists_count()
        playlists_with_songs = expectations.get_playlists_with_songs(not_full=True)
        id_playlist_for_change = playlists_with_songs[randint(0, len(playlists_with_songs) - 1)]
        songs = list(expectations.get_songs_from_playlist_by_id(id_playlist_for_change))

        response = api_communicator.send_mutation_request(
            func='editPlaylist(id: {}, songs: {})'.format(id_playlist_for_change, songs + [randint(700, 1000)]),
            values=['id'],
            code=200)
        assert response['data']['editPlaylist'] is not None
        sleep(0.3)
        expectations.update_playlists_df()
        assert count_of_playlists == expectations.get_playlists_count()
        assert sorted(list(expectations.get_songs_from_playlist_by_id(id_playlist_for_change))) == sorted(songs)

    @pytest.mark.api
    def test_remove_song_from_playlist(self, api_communicator, expectations):
        expectations.update_playlists_df()
        count_of_playlists = expectations.get_playlists_count()
        playlists_with_songs = expectations.get_playlists_with_songs(not_full=False, not_one=True)
        id_playlist_for_change = playlists_with_songs[randint(0, len(playlists_with_songs) - 1)]
        songs = list(expectations.get_songs_from_playlist_by_id(id_playlist_for_change))
        songs_for_update = sorted(dg.remove_random_songs_from_list(songs))

        response = api_communicator.send_mutation_request(
            func='editPlaylist(id: {}, songs: {})'.format(id_playlist_for_change, songs_for_update),
            values=['id'],
            code=200)
        assert response['data']['editPlaylist'] is not None
        sleep(0.3)
        expectations.update_playlists_df()
        assert count_of_playlists == expectations.get_playlists_count()
        assert sorted(list(expectations.get_songs_from_playlist_by_id(id_playlist_for_change))) == songs_for_update

    @pytest.mark.api
    def test_no_changes_in_playlist(self, api_communicator, expectations):
        expectations.update_playlists_df()
        count_of_playlists = expectations.get_playlists_count()
        playlists_with_songs = expectations.get_playlists_with_songs(not_full=False)
        id_playlist_for_change = playlists_with_songs[randint(0, len(playlists_with_songs) - 1)]
        songs = list(expectations.get_songs_from_playlist_by_id(id_playlist_for_change))

        response = api_communicator.send_mutation_request(
            func='editPlaylist(id: {}, songs: {})'.format(id_playlist_for_change, songs),
            values=['id'],
            code=200)
        assert response['data']['editPlaylist'] is not None
        sleep(0.3)
        expectations.update_playlists_df()
        assert count_of_playlists == expectations.get_playlists_count()
        assert sorted(list(expectations.get_songs_from_playlist_by_id(id_playlist_for_change))) == sorted(songs)

    @pytest.mark.api
    def test_add_all_songs_playlist(self, api_communicator, expectations):
        expectations.update_playlists_df()
        count_of_playlists = expectations.get_playlists_count()
        playlists_with_songs = expectations.get_playlists_with_songs(not_full=True)
        id_playlist_for_change = playlists_with_songs[randint(0, len(playlists_with_songs) - 1)]
        songs = [x for x in range(1, expectations.get_songs_count() + 1)]

        response = api_communicator.send_mutation_request(
            func='editPlaylist(id: {}, songs: {})'.format(id_playlist_for_change, songs),
            values=['id'],
            code=200)
        assert response['data']['editPlaylist'] is not None
        sleep(0.3)
        expectations.update_playlists_df()
        assert count_of_playlists == expectations.get_playlists_count()
        assert sorted(list(expectations.get_songs_from_playlist_by_id(id_playlist_for_change))) == sorted(songs)

    @pytest.mark.api
    def test_add_song_to_full_playlist(self, api_communicator, expectations):
        expectations.update_playlists_df()
        count_of_playlists = expectations.get_playlists_count()
        playlists_with_songs = expectations.get_playlists_with_songs(not_full=False, only_full=True)
        id_playlist_for_change = playlists_with_songs[randint(0, len(playlists_with_songs) - 1)]
        songs = [randint(1, expectations.get_songs_count())]

        response = api_communicator.send_mutation_request(
            func='editPlaylist(id: {}, songs: {})'.format(id_playlist_for_change, songs),
            values=['id'],
            code=200)
        assert response['data']['editPlaylist'] is not None
        sleep(0.3)
        expectations.update_playlists_df()
        assert count_of_playlists == expectations.get_playlists_count()
        assert sorted(list(expectations.get_songs_from_playlist_by_id(id_playlist_for_change))) == sorted(songs)

    @pytest.mark.api
    def test_remove_all_songs_from_playlist(self, api_communicator, expectations):
        expectations.update_playlists_df()
        count_of_playlists = expectations.get_playlists_count()
        playlists_with_songs = expectations.get_playlists_with_songs(not_full=False)
        id_playlist_for_change = playlists_with_songs[randint(0, len(playlists_with_songs) - 1)]

        response = api_communicator.send_mutation_request(
            func='editPlaylist(id: {}, songs: [])'.format(id_playlist_for_change),
            values=['id'],
            code=200)
        assert response['data']['editPlaylist'] is not None
        sleep(0.3)
        expectations.update_playlists_df()
        assert count_of_playlists == expectations.get_playlists_count()
        assert id_playlist_for_change not in expectations.get_playlists_with_songs(not_full=False)

    @pytest.mark.api
    def test_delete_correct_playlist(self, api_communicator, expectations):
        expectations.update_playlists_df()
        count_of_playlists = expectations.get_playlists_count()

        response = api_communicator.send_mutation_request(
            func='deletePlaylist(id: {})'.format(randint(1, count_of_playlists)),
            values=['id'],
            code=200)
        assert response['data']['deletePlaylist'] is not None
        sleep(0.3)
        expectations.update_playlists_df()
        assert count_of_playlists - 1 == expectations.get_playlists_count()
        assert response['data']['deletePlaylist']['id'] not in expectations.get_playlists_list()
        assert response['data']['deletePlaylist']['id'] not in expectations.get_playlists_with_songs(not_full=False)

    @pytest.mark.api
    def test_delete_incorrect_playlist(self, api_communicator, expectations):
        expectations.update_playlists_df()
        count_of_playlists = expectations.get_playlists_count()

        response = api_communicator.send_mutation_request(
            func='deletePlaylist(id: {})'.format(expectations.get_highest_playlist_id() + 1),
            values=['id'],
            code=200)
        assert response['data']['deletePlaylist'] is not None
        sleep(0.3)
        expectations.update_playlists_df()
        assert count_of_playlists == expectations.get_playlists_count()
