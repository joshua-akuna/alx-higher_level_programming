#!/usr/bin/python3
def multiple_returns(sentence):
    size = 0 if len(sentence) == 0 else len(sentence)
    first = None if len(sentence) == 0 else sentence[0]
    return (size, first)
