#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

table = {
    "a": "alpha",
    "b": "bravo",
    "c": "charlie",
    "d": "delta",
    "e": "echo",
    "f": "foxtrot",
    "g": "golf",
    "h": "hotel",
    "i": "india",
    "j": "juliett",
    "k": "kilo",
    "l": "lima",
    "m": "mike",
    "n": "november",
    "o": "oscar",
    "p": "papa",
    "q": "quebec",
    "r": "romeo",
    "s": "sierra",
    "t": "tango",
    "u": "uniform",
    "v": "victor",
    "w": "whiskey",
    "x": "x-ray",
    "y": "yankee",
    "z": "zulu",
    "0": "Nadazero",
    "1": "Unaone",
    "2": "Bissotwo",
    "3": "Terrathree",
    "4": "Kartefour",
    "5": "Pantafive",
    "6": "Soxisix",
    "7": "Setteseven",
    "8": "Oktoeight",
    "9": "Novenine",
}


class IllegalStringSize(Exception):
    def __init__(self, msg):
        super(Exception, self).__init__(msg)


def find_in_table(letter):
    if len(letter) != 1:
        raise IllegalStringSize(
            "The letter parameter should only contains one character"
        )

    if letter in table:
        res = table[letter]
    elif letter.lower() in table:
        res = table[letter.lower()].upper()
    elif not letter or letter.isspace():
        res = ""
    else:
        res = letter
    return res


def convert(orig):
    result = ""
    for letter in orig:
        res = find_in_table(letter)
        if result:
            result = "%s %s" % (result, res)
        else:
            result = res
    return result


if __name__ == '__main__':
    orig = ""
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            orig = orig + arg
    elif not sys.stdin.isatty():
        for arg in sys.stdin.readlines():
            orig = orig + arg
    if orig:
        orig = orig.replace("\n", " ")
        result = convert(orig)

        print(f'{orig}:{result}')
    else:
        print("usage")

# vim: set ts=4 sw=4 expandtab:
