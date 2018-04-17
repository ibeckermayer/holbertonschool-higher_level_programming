#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is not None:
        if not sentence:
            return (0, None)
        else:
            return (len(sentence), sentence[0])
