#!/usr/bin/python3
"""a function that prints a text with 2 new lines after
each of these characters: ., ? and : text must be a string,
otherwise raise a TypeError exception with the message text
must be a string. There should be no space at the beginning
or at the end of each printed line"""


def text_indentation(text):
    """a function that prints a text with 2 new lines after
    each of these characters: ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new_line = ""
    for i in text:
        new_line += i
        if i in {'.', '?', ':'}:
            clean = new_line.strip()
            if clean:
                print("{}".format(clean), end="\n\n")
            new_line = ""
    if new_line.strip():
        print(new_line.strip(), end="")
