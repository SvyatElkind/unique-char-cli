"""Tests for CLI.

Tests for collect_framework(),
result_from_file() and validate_extension().
"""
from unittest.mock import patch, mock_open, MagicMock

import pytest

from unique_char.collect_framework import validate_extension, result_from_file, \
    collect_framework


class TestFileExtension:
    """Tests for input file extension."""

    def test_invalid_file_extension(self):
        """Input file with invalid extension."""
        with pytest.raises(UserWarning):
            validate_extension("test.csv")

    def test_valid_file_extension(self):
        """Input file with valid extension."""
        assert validate_extension("test.txt") is None


class TestOutput:
    """Tests for CLI output."""

    def test_output_no_argument(self, capsys):
        """Call with no argument

        Args:
            capsys:
                pytest fixture.
        """
        # Call function without any arguments
        with patch("sys.argv", ["collect_framework.py"]):
            collect_framework()
        output = capsys.readouterr().out.rstrip()
        assert "usage: collect_framework.py [-h] [-s STRING] [-f FILE]" \
               in output

    @patch("unique_char.collect_framework.unique_char_string", return_value=3)
    @pytest.mark.parametrize("option",
                             [["collect_framework.py", "-s", "Hello"],
                              ["collect_framework.py", "--string", "Hello"]])
    def test_output_string_argument(self, mock_unique_char_string: MagicMock,
                                    capsys, option: list):
        """Call with sting argument.

        Args:
            mock_unique_char_string:
                patched unique_char_string in mian.collect_framework.
            capsys:
                pytest fixture.
            option:
                arguments to pass to collect_framework(option).
        """
        with patch("sys.argv", option):
            collect_framework()
        output = capsys.readouterr().out.rstrip()
        assert output == "\"Hello\": 3"

    @patch("unique_char.collect_framework.result_from_file",
           return_value={"hello world": 6, "hi": 2, "test": 2})
    @pytest.mark.parametrize("option",
                             [["collect_framework.py", "-f", "test.txt"],
                              ["collect_framework.py", "--file", "test.txt"]])
    def test_output_file_argument(self, mock_result_from_file: MagicMock,
                                  capsys, option: list):
        """Call with file argument.

        Args:
            mock_result_from_file:
                patched result_from_file in mian.collect_framework.
            capsys:
                pytest fixture.
            option:
                arguments to pass to collect_framework(option).
        """
        with patch("sys.argv", option):
            collect_framework()
        output = capsys.readouterr().out.rstrip()
        assert output == "{'hello world': 6, 'hi': 2, 'test': 2}"

    @patch("unique_char.collect_framework.result_from_file",
           return_value={"hello world": 6, "hi": 2, "test": 2})
    def test_output_mixed_arguments(self, mock_result_from_file: MagicMock,
                                    capsys):
        """Call with mixed arguments.

        Args:
            mock_result_from_file:
                patched result_from_file in mian.collect_framework().
            capsys: pytest fixture.
        """
        with patch("sys.argv", ["collect_framework.py",
                                "--string", "Hello",
                                "--file", "test.txt"]):
            collect_framework()
        output = capsys.readouterr().out.rstrip()
        assert output == "{'hello world': 6, 'hi': 2, 'test': 2}"


class TestFileOpener:
    """Tests for results from file"""

    @patch("unique_char.collect_framework.unique_char_in_each_string",
           return_value={"first line": 8, "second line": 7,
                         "": 0, "fourth line": 11})
    def test_result_from_file_without_error(self, mock_unique_char_in_each_string: MagicMock):
        """Return valid result from file.

        Args:
            mock_unique_char_in_each_string:
                patched unique_char_in_each_string
                in mian.collect_framework."""
        # Mock file content
        read_data = "first line\nsecond line\n\nfourth line\n"
        with patch("builtins.open", mock_open(read_data=read_data)):
            result = result_from_file("file.txt")
        assert {"first line": 8, "second line": 7, "": 0, "fourth line": 11} \
               == result

    def test_result_from_file_with_error(self, capsys):
        """OSError when try to open file.

        Args:
            capsys: pytest fixture.
        """
        with patch("builtins.open", mock_open()) as mock_file:
            # Mock error when open file
            mock_file.side_effect = OSError
            result_from_file("file.txt")
            output = capsys.readouterr().out.rstrip()
            assert "Couldn't open file:" in output
