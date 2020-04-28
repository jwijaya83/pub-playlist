import pytest
from tests.helpers.api_helper import ApiHelper
from tests.helpers.db_communicator import DBCommunicator
from tests.expectations import PlaylistExpectations


def pytest_addoption(parser):
    parser.addoption("--server", action="store", default="http://localhost")
    parser.addoption("--graphql_port", action="store", default="3000")
    parser.addoption("--ui_port", action="store", default="4000")


@pytest.fixture(scope='class')
def api_communicator(request):
    return ApiHelper('{}:{}'.format(request.config.getoption('--server'), request.config.getoption('--graphql_port')))


@pytest.fixture(scope='class')
def expectations():
    db_communicator = DBCommunicator()
    return PlaylistExpectations(db_communicator.get_songs_list(),
                                db_communicator.get_songs_table_columns_names()[:5],
                                db_communicator.get_playlists_list(),
                                db_communicator.get_playlists_table_columns_names()[:2],
                                db_communicator.get_all_songs_in_playlists(),
                                db_communicator.get_all_songs_in_playlists_columns_names()[2:])
