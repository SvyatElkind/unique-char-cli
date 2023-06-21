# unique-char

## Overview

The Unique Char provides command-line interface to
count unique characters (characters that appears only once) in:
* user provided string;
* each line of the text file.

**_NOTE:_** Only .txt files can be used

## System Requirements

Unique Char is written for Python 3. The following
sub-versions are supported:

* Python 3.8
* Python 3.9
* Python 3.10

## Install

`pip install unique-char`

## CLI Usage Example

```
# More information about usage
> pyhton -m unique_char.collect_framework -h
# or 
> pyhton -m unique_char.collect_framework -help
```

### Input with string parameter


*Command-line:*
```
# Unique characters in the string
> python -m unique_char.collect_framework -s hello
# or
> python -m unique_char.collect_framework -string hello
```

*Output:*

```"Hello": 3```

### Input with file parameter

*Content of my_file.txt:*
```
This is 
my file
```

*Command-line:*
```
# Unique characters in each line of the file
> python -m unique_char.collect_framework -f path/to/my_file.txt
# or
> python -m unique_char.collect_framework -file path/to/my_file.txt
```

*Output:*

`{"This is": 3, "my file": 7}`

---
**_NOTE:_** 

If two parameters are passed, the parameter '--file' 
will have higher priority. That means that string will be ignored.
---

## Additional

You can use functions in your project:

```python
from unique_char.unique_char import unique_char_string, unique_char_in_each_string
unique_char_string("hello") # Return 3
unique_char_in_each_string(["Hello", "world"]) # Return {"Hello": 3, "world": 5}
```