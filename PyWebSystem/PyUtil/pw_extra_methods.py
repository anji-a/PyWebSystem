import string
import random


def id_generator(size=6, prefix="", suffix="", chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    genstring = ''.join(random.choice(chars) for _ in range(size))
    return prefix+genstring+suffix
