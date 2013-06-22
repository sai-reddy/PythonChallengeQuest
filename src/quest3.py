#!/usr/bin/python -tt

import re

def parse():
    """
    Potential loophole is that what if the pattern is present in the
    boundary for a line.
    """
    secrets = []
    txt = ""
    with open("../data/quest3_data.txt") as f:
        for line in f.readlines():
            match = re.search(r"[a-z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][a-z]", line.strip())
            if match:
                secrets.append(match.group())
    # Extract the small element
    for i,secret in enumerate(secrets):
        secrets[i] = secret[4]
    print secrets
    print ''.join(secrets)

if __name__ == "__main__":
    parse()
