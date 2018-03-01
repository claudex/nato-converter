#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import sys


table_default = {
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
    "9": "Novenine"
    }

table_elephant = {
    "a": "animal",
    "b": "babar",
    "c": "cornac",
    "d": "défense",
    "e": "éléphant",
    "f": "forêt",
    "g": "gris",
    "h": "harde",
    "i": "ivoire",
    "j": "Jérakine",
    "k": "Kamba",
    "l": "longévité",
    "m": "mémoire",
    "n": "nuifs",
    "o": "oreilles",
    "p": "pachyderme",
    "q": "queue",
    "r": "roi",
    "s": "souris",
    "t": "trompe",
    "u": "unknown",
    "v": "voltage",
    "x": "léon X",
    "y": "yazdgard",
    "z": "zoo",
    }

class IllegalStringSize(Exception):
    def __init__(self, msg):
        super(Exception, self).__init__(msg)

def find_in_table(letter, table):
    if len(letter) != 1:
        raise IllegalStringSize(
            "The letter parameter should only contains one character")

    if letter in table:
        res =  table[letter]
    elif letter.lower() in table:
        res = table[letter.lower()].upper()
    elif not letter or letter.isspace():
        res = ""
    else:
        res = letter
    return res

def convert(orig, table):
    result = ""
    for letter in orig:
        res = find_in_table(letter, table)
        if result:
            result = "%s %s" % (result, res)
        else:
            result = res
    return result


def main():
    parser = argparse.ArgumentParser(prog='nato_converter', usage='%(prog)s [options]')
    parser.add_argument("-e", "--elephant", action="store_true", help="Activate elephant mode")
    parser.add_argument('passwords', type=str, nargs='+',
                        help='the string to convert')
    #TODO parse stdin
    args = parser.parse_args()
    passwords = args.passwords
    orig = ", ".join(passwords)
    orig = orig.replace("\n", " ")
    if args.elephant:
        table = table_elephant
    else:
        table = table_default
    result = convert(orig, table)

    print("%s: %s"% (orig, result))


if __name__ == '__main__':
    main()

# vim: set ts=4 sw=4 expandtab:
