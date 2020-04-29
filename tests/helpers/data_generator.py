import string
import random


class DataGenerator:

    @classmethod
    def generate_random_name(cls, length):
        symbols = string.ascii_letters + string.digits
        return "".join([random.choice(symbols) for elem in range(length)])

    @classmethod
    def get_random_sequence_of_numbers(cls, count, val_range, is_unique=False):
        if is_unique:
            values = set()
            while len(values) != count:
                values.add(random.randint(1, val_range))
            return [str(x) for x in values]
        return [str(random.randint(1, val_range)) for e in range(count)]

    @classmethod
    def add_random_songs_to_list(cls, count, songs_list, max_value):
        songs_set = {song for song in songs_list}
        while len(songs_set) != len(songs_list) + count:
            songs_set.add(random.randint(1, max_value))
        return [song for song in songs_set]

    @classmethod
    def remove_random_songs_from_list(cls, songs_list):
        random.shuffle(songs_list)
        if len(songs_list) <= 3:
            return songs_list[:1]
        elif len(songs_list) <= 10:
            return songs_list[:random.randint(1, 3) * -1]
        return songs_list[:random.randint(5, 8) * -1]
