import psycopg2


class DBCommunicator:
    def __init__(self):
        self.__dbname = 'playlist'
        self.__username = 'postgres'
        self.__password = 'postgres'
        self.__port = '5432'
        self.__conn = psycopg2.connect("dbname={} user={} password={} port={}".format(
            self.__dbname, self.__username, self.__password, self.__port))
        self.__cursor = self.__conn.cursor()

    def __del__(self):
        self.__cursor.close()
        self.__conn.close()

    def get_songs_list(self):
        self.__cursor.execute("SELECT id, album, duration, title, artist FROM songs ORDER BY id ASC;")
        return self.__cursor.fetchall()

    def get_songs_table_columns_names(self):
        self.__cursor.execute("SELECT * FROM songs;")
        return [el.name for el in self.__cursor.description]

    def get_playlists_list(self):
        self.__cursor.execute("SELECT id, name FROM playlists ORDER BY id ASC;")
        return self.__cursor.fetchall()

    def get_playlists_table_columns_names(self):
        self.__cursor.execute("SELECT * FROM playlists;")
        return [el.name for el in self.__cursor.description]

    def get_all_songs_in_playlists(self):
        self.__cursor.execute("SELECT playlist_id, song_id FROM songs_in_playlist;")
        return self.__cursor.fetchall()

    def get_all_songs_in_playlists_columns_names(self):
        self.__cursor.execute("SELECT * FROM songs_in_playlist;")
        return [el.name for el in self.__cursor.description]
