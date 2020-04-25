import pandas as pd


class PlaylistExpectations:
    def __init__(self, songs: list, songs_col_names: list, playlists: list, playlists_col_names: list):
        self.songs_df = pd.DataFrame(data=songs, columns=songs_col_names)
        self.songs_df['name'] = self.songs_df['id']
        self.songs_df.set_index('name', inplace=True)
        self.playlists_df = pd.DataFrame(data=playlists, columns=playlists_col_names)

    def get_count_of_songs(self):
        return self.songs_df.iloc[-1].name

    def get_song_by_id(self, id):
        return self.songs_df.iloc[id - 1]
