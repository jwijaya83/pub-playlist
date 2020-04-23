import pytest
from tests.constants import PlaylistConstants as const


class TestAPI:

    @pytest.mark.api
    def test_count_of_songs(self, api_communicator):
        response = api_communicator.send_query_request(schema='libraries', values=['id'], code=200)
        assert len(response['data']['libraries']) == const.DEFAULT_COUNT_OF_SONGS

    @pytest.mark.api
    def test_count_of_playlists(self, api_communicator):
        response = api_communicator.send_query_request(schema='playlists', values=['id'], code=200)
        assert response['data']['playlists'] is None
