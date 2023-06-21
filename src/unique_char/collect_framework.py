"""Command-line interface for unique character application"


Functions:
    collect_framework()
    result_from_file(str) -> dict:
    validate_extension(str) -> None
"""
import argparse
import pprint

from .unique_char import unique_char_string, unique_char_in_each_string
from .constant import FILE_EXTENSIONS


def validate_extension(file_path: str):
    """Validate file extension

    Validate if file can be processed by checking
    if file extension is in FILE_EXTENSION tuple

    Args:
        file_path:
            File path string.

    Raises:
        Exception: if validation didn't pass.
    """
    if not file_path.endswith(FILE_EXTENSIONS):
        raise UserWarning(f"You selected file with the unsupported extension, "
                          f"the allowed ones are: {FILE_EXTENSIONS}")


def result_from_file(file_path: str) -> dict:
    """Open file


    Opens and reads file line by line and pass each line from the file to
    unique_char_string() to count the number of unique characters
    in the line.

    Args:
        file_path:
            File path string.

    Returns:
        Result of unique_char_string()
        For example:

        {"abbbccdf": 3, "collection framework": 9, "aaa": 0}

    Raises:
        OSError: An error occurs when file is not found,
        or you don't have permission to read it
    """
    # Check if file can be processed
    validate_extension(file_path)
    try:
        with open(file_path) as input_file:
            result = unique_char_in_each_string(input_file)
            return result
    except OSError:
        print("Couldn't open file:"
              "Make sure that file exists or/and you have access to it:",
              file_path)


def collect_framework():
    """Implement command-line interface

    Use argparse to get input from command-line
    and print according result.
    """
    parser = argparse.ArgumentParser(
        description="""Count unique char in a string or a file.
        If two parameters are passed, the parameter '--file' 
        will have higher priority.
        That means that string will be ignored.""")

    parser.add_argument(
        "-s", "--string",
        help="a string in which to count the unique characters")

    parser.add_argument(
        "-f", "--file",
        help="""a file in which to count
        the unique characters of each line.
        Allowed file extensions: .txt""")

    args = parser.parse_args()

    # Return result only from file if both parameters are specified
    if args.file:
        # Print result from file
        result = result_from_file(args.file)
        pprint.pprint(result)
    elif args.string:
        # Print result from string
        result = unique_char_string(args.string)
        print(f"\"{args.string}\": {result}")
    else:
        # Print usage of CLI if no action is requested
        parser.print_usage()


if __name__ == "__main__":
    collect_framework()
