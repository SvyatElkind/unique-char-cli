""" Module for counting unique characters in a string.

Contains functions that count unique characters from
given string or list of strings, set of strings,
tuple of strings or dict with keys as string.

Functions:
    unique_char_string(string) -> int
    unique_char_in_each_string(Iterable[str]) -> dict
"""
from collections import Counter
from functools import lru_cache
from typing import Iterable

from .constant import CACHE_SIZE, ACCEPTABLE_ITERABLES


@lru_cache(maxsize=CACHE_SIZE)
def unique_char_string(text: str) -> int:
    """Count unique characters in the string

    Return number of unique characters in a given string.

    Args:
        text:
            Any length string.

    Returns:
        A number of unique characters in given string.
        For example:

        "abbbccdf" => 3
    """
    if not isinstance(text, str):
        raise TypeError("Input is not a string")

    # Count all character appearance in the string and
    # then count characters which appears only 1 time
    result = list(Counter(text.strip()).values()).count(1)
    return result


def unique_char_in_each_string(input_strings: Iterable[str]) -> dict:
    """Count unique characters in the strings

    Return number of unique characters in each
    string given in the list, set, tuple, dict keys
    or _io.TextIOWrapper.

    Args:
        input_strings:
            Iterable object with string elements.

    Returns:
        A dictionary where key equals to given string from list and
        value is the number of unique characters in this string.
        For example:

        {"abbbccdf": 3, "collection framework": 9, "aaa": 0}
    """
    # Check if Iterable is acceptable, otherwise raise TypeError.
    if not isinstance(input_strings, ACCEPTABLE_ITERABLES):
        raise TypeError("Unacceptable iterable object:", input_strings)

    result = {}
    for text in input_strings:
        result[text.strip()] = unique_char_string(text)
    return result
