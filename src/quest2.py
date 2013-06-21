#!/usr/bin/python -tt

from collections import Counter

def parse():
    chars_found = []
    valid_chars = list("abcdefghijklmnopqrstuvwxyz")
    with open("../data/quest2_data.txt", "r") as f:
        for line in f.readlines():
            chars_found.extend((Counter(list(line)) & Counter(valid_chars)).elements())
    print chars_found

if __name__ == "__main__":
    parse()
