"""Pytest module for unique_char functions.

This module have pytest tests for unique_char_string() and
unique_char_in_each_string().

Functions:
    test_not_string()
    test_not_multiple_strings()
    test_char_result_from_string()
    test_char_result_from_list()
"""
import pytest
import unique_char


@pytest.mark.parametrize("input_type", [1,
                                        1.5,
                                        [1, "hello"]])
def test_not_string(input_type):
    """Tests unique_char_string() with invalid input parameters.

    Make sure that unique_char_string() raises TypeError
    if parameter is not a string.

    Args:
        input_type:
            Types (int, float, list) that will be passed to the
            unique_char_string() as argument.
    """
    with pytest.raises(TypeError):
        unique_char.unique_char_string(input_type)


@pytest.mark.parametrize("input_type", [1,
                                        "text",
                                        ["text", 1, "second"]])
def test_not_multiple_strings(input_type):
    """Tests unique_char_in_each_string() with invalid input parameters.

    Make sure that unique_char_in_each_string() raises TypeError
    if parameter is not a list of strings, set of strings,
    tuple of strings or dict with keys as string.

    Args:
        input_type:
            Types (int, str, list of different types) that will
            be passed to the unique_char_in_each_string() as argument.
    """
    with pytest.raises(TypeError):
        unique_char.unique_char_in_each_string(input_type)


@pytest.mark.parametrize("text, expected", [
    ("abbbccdf", 3),
    ("space space", 1),
    ("\n\n", 0),
    ("mM", 2),
    ("", 0),
    ("\na\n", 1)])
def test_char_result_from_string(text: str, expected: int):
    """Tests unique_char_string() result.

    Process string with unique_char_string()
    and compare return value with expected value.

    Args:
        text:
            Any length string.

        expected:
            Number of expected unique characters in the text.
    """
    assert unique_char.unique_char_string(text) == expected


@pytest.mark.parametrize("str_list, expected", [
    (["abbbccdf", "space space\n", "\n\n", "mM", ""],
     {"abbbccdf": 3, "space space": 1, "": 0, "mM": 2})])
def test_char_result_from_list(str_list: list, expected: dict):
    """Tests unique_char_in_each_string() result.

    Process list of strings with unique_char_in_each_string()
    and compare return value with expected value.

    Args:
        str_list:
            Any length list of string.

        expected:
            A dictionary where key equals to given string from list and
            value is the number of unique characters in this string.
    """
    assert unique_char.unique_char_in_each_string(str_list) == expected
