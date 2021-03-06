import pandas as pd
from tests.helpers.db_communicator import DBCommunicator


class PlaylistExpectations:
    def __init__(self, songs: list, songs_col_names: list, playlists: list, playlists_col_names: list,
                 songs_in_playlists: list, sip_names: list):
        self.songs_df = pd.DataFrame(data=songs, columns=songs_col_names)
        self.songs_df['name'] = self.songs_df['id']
        self.songs_df.set_index('name', inplace=True)
        self.playlists_df = pd.DataFrame(data=playlists, columns=playlists_col_names)
        self.songs_in_playlists_df = pd.DataFrame(data=songs_in_playlists, columns=sip_names)

    def get_songs_count(self):
        return self.songs_df.iloc[-1].name

    def get_song_by_id(self, id):
        return self.songs_df.iloc[id - 1]

    def get_song_df_by_id(self, id):
        return self.songs_df[self.songs_df['id'] == id]

    def get_playlists_count(self):
        return self.playlists_df['id'].count()

    def get_albums_count(self):
        return self.songs_df['album'].nunique()

    def get_highest_playlist_id(self):
        return self.playlists_df['id'].values.max()

    def get_playlists_list(self):
        return self.playlists_df['id'].values

    def get_playlist_name_by_id(self, id):
        return self.playlists_df[self.playlists_df['id'] == id]['name'].values[0]

    def get_playlist_name_by_iloc(self, iloc_id):
        return self.playlists_df.iloc[iloc_id-1]['name']

    def get_playlists_names(self, id_exclude=None):
        if id_exclude:
            return self.playlists_df[self.playlists_df['id'] != id_exclude]['name'].values
        return self.playlists_df['name'].values

    def get_songs_from_playlist_by_id(self, id):
        return self.songs_in_playlists_df[self.songs_in_playlists_df['playlist_id'] == id]['song_id'].values

    def get_playlists_with_songs(self, not_full=True, not_one=False, only_full=False):
        list_of_playlists_with_songs = sorted(self.songs_in_playlists_df['playlist_id'].unique())
        if not_full:
            list_of_playlists_with_songs = self.__remove_full_playlists(list_of_playlists_with_songs, self.get_songs_count())
        if not_one:
            list_of_playlists_with_songs = self.__remove_ones_playlists(list_of_playlists_with_songs)
        if only_full:
            list_of_playlists_with_songs = self.__remove_not_full_playlists(list_of_playlists_with_songs, self.get_songs_count())
        return list_of_playlists_with_songs

    def __remove_full_playlists(self, list_of_playlists, songs_count):
        new_list = []
        for e in list_of_playlists:
            if self.songs_in_playlists_df[self.songs_in_playlists_df['playlist_id'] == e]['song_id'].count() != songs_count:
                new_list.append(e)
        return new_list

    def __remove_not_full_playlists(self, list_of_playlists, songs_count):
        new_list = []
        for e in list_of_playlists:
            if self.songs_in_playlists_df[self.songs_in_playlists_df['playlist_id'] == e]['song_id'].count() == songs_count:
                new_list.append(e)
        return new_list

    def __remove_ones_playlists(self, list_of_playlists):
        new_list = []
        for e in list_of_playlists:
            if self.songs_in_playlists_df[self.songs_in_playlists_df['playlist_id'] == e]['song_id'].count() != 1:
                new_list.append(e)
        return new_list

    def get_playlist_by_id(self, id):
        return self.playlists_df[self.playlists_df['id'] == id]

    def get_count_of_songs_in_playlists(self):
        return self.songs_in_playlists_df['song_id'].count()

    def get_list_of_artists(self):
        return self.songs_df['artist'].unique()

    def get_list_of_albums(self):
        return self.songs_df['album'].unique()

    def get_songs_in_album(self, album_name):
        return self.songs_df[self.songs_df['album'] == album_name]['title'].values

    def get_songs_in_playlist_by_playlist_id(self, playlist_id):
        res_dict = dict()
        pl_name = self.playlists_df[self.playlists_df['id'] == playlist_id]['name'].values[0]
        songs_ids = self.songs_in_playlists_df[self.songs_in_playlists_df['playlist_id'] == playlist_id]['song_id'].values
        res_dict['name'] = pl_name
        if songs_ids.size == 0:
            res_dict['songs'] = []
            return res_dict
        res_dict['songs'] = [
            self.songs_df[self.songs_df['id'] == song_id]['title'].values[0] for song_id in songs_ids
        ]
        return res_dict

    def update_playlists_df(self):
        db_communicator = DBCommunicator()
        self.playlists_df = pd.DataFrame(data=db_communicator.get_playlists_list(),
                                         columns=db_communicator.get_playlists_table_columns_names()[:2])
        self.songs_in_playlists_df = pd.DataFrame(data=db_communicator.get_all_songs_in_playlists(),
                                                  columns=db_communicator.get_all_songs_in_playlists_columns_names()[2:])
        db_communicator.__del__()
