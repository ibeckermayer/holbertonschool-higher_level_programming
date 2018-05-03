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
    toks = []
    beg = 0
    end = 0

    while end < len(text):
        if not text[end] in splitters and not end == len(text) - 1:
            end += 1
            continue
        else:
            end += 1
            toks.append(text[beg:end])
            beg = end

    for i in range(len(toks)):
        tok = toks[i].strip()
        print(tok, end="")
        if tok and tok[-1] in splitters:
            print()
            print()
