#!/usr/bin/python3
def text_indentation(text):
    """prints a text with 2 new lines after each of these characters
       : ., ? and :

    Args:
       text (str): the text to be indented

    Raises:
        TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    splitters = [".", "?", ":"]
    for splitter in splitters:
        if splitter == ".":
            split = text.split(".")
        else:
            split = [t.split(splitter) for t in split]
            split = [item for sublist in split for item in sublist]
    for i in range(len(split)):
        print(split[i].strip(), end="")
        if i < len(split) - 1:
            print()
            print()
