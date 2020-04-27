import string
import random


def generate_random_name(length):
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for elem in range(length)])


def get_random_sequence_of_numbers(count, val_range, is_unique=False):
    if is_unique:
        values = set()
        while len(values) != count:
            values.add(random.randint(1, val_range))
        return [str(x) for x in values]
    return [str(random.randint(1, val_range)) for e in range(count)]
