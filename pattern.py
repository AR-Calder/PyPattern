#!/usr/bin/env python3
import sys


def pattern_create(length):
    pattern = ""

    low = ['A', 'a', '0']
    char = low.copy()
    high_char = ['Z', 'z', '9']

    while char != high_char and len(pattern) <= length:
        pattern += ''.join(char)
        char[2] = chr(ord(char[2]) + 1)

        if char[2] == chr(ord(high_char[2]) + 1):
            i = 2
            while i > 0 and char[i] == chr(ord(high_char[i]) + 1):
                char[i] = low[i]
                if i != 0:
                    char[i - 1] = chr(ord(char[i - 1]) + 1)
                i -= 1

    pattern += ''.join(char)
    return pattern


def pattern_reverse(pattern):
    low = ['A', 'a', '0']
    return ("position: %s" % (3 * ((((1 + ord(pattern[0]) - ord(low[0])) * 260) + ((1 + ord(pattern[1]) - ord(low[1])) * 10) + ((1 + ord(pattern[2]) - ord(low[2])) * 1)) - 270)))

def main():
    if len(sys.argv) < 3 or sys.argv[1].lower() not in ['reverse', 'create']:
        print("Usage: %s (reverse | create) <value> " % (sys.argv[0]))
        exit(1)

    arg1 = sys.argv[1].lower()
    arg2 = int(sys.argv[2])

    if arg1 == 'create':
        print(pattern_create(arg2))
    else:
        print(pattern_reverse(arg2))

if __name__ == '__main__':
    main()
