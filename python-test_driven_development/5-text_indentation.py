#!/usr/bin/python3
def text_indentation(text):
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
