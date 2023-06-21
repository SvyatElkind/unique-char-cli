"""Basic constants for application"""

from _io import TextIOWrapper


# Size of cache for unique_char_string()
CACHE_SIZE = 16
# Iterables acceptable by unique_char_in_each_string()
ACCEPTABLE_ITERABLES = (list, set, tuple, dict, TextIOWrapper)
# File extensions to be processed
FILE_EXTENSIONS = (".txt",)
