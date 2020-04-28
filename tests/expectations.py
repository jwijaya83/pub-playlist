import pandas as pd
from tests.helpers.db_communicator import DBCommunicator


class PlaylistExpectations:
    def __init__(self, songs: list, songs_col_names: list, playlists: list, playlists_col_names: list,
                 songs_in_playlists: list, sip_names: list):
        self.songs_df = pd.DataFrame(data=songs, columns=songs_col_names)
        self.songs_df['name'] = self.songs_df['id']
        self.songs_df.set_index('name', inplace=True)
        self.playlists_df = pd.DataFrame(data=playlists, columns=playlists_col_names)
        self.songs_in_playlists_table_df = pd.DataFrame(data=songs_in_playlists, columns=sip_names)

    def get_songs_count(self):
        return self.songs_df.iloc[-1].name

    def get_song_by_id(self, id):
        return self.songs_df.iloc[id - 1]

    def get_playlists_count(self):
        return self.playlists_df['id'].count()

    def get_playlist_name_by_id(self, id):
        return self.playlists_df[self.playlists_df['id'] == id]['name']

    def get_count_of_songs_in_playlists(self):
        return self.songs_in_playlists_table_df['song_id'].count()

    def update_playlists_df(self):
        db_communicator = DBCommunicator()
        self.playlists_df = pd.DataFrame(data=db_communicator.get_playlists_list(),
                                         columns=db_communicator.get_playlists_table_columns_names())
        self.songs_in_playlists_table_df = pd.DataFrame(data=db_communicator.get_all_songs_in_playlists(),
                                                        columns=db_communicator.get_all_songs_in_playlists_columns_names())
        db_communicator.__del__()
