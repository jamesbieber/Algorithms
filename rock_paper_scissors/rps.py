#!/usr/bin/python

import sys


def recurse(prev, n, all_results):
    if n == 0:
        all_results.append(prev)
        return
    recurse(prev + ['rock'], n - 1, all_results)
    recurse(prev + ['paper'], n - 1, all_results)
    recurse(prev + ['scissors'], n - 1, all_results)


def rock_paper_scissors(n):
    results = []
    recurse([], n, results)

    return results


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
