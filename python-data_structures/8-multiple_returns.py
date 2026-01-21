#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        sentence_len = len(sentence)
        start_ch = None
    else:
        sentence_len = len(sentence)
        start_ch = sentence[0]
    return sentence_len, start_ch
