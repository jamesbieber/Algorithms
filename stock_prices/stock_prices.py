#!/usr/bin/python

import argparse


def find_max_profit(prices):
    smallest = prices[0]
    biggest = prices[1] - prices[0]

    for i in range(1, len(prices)):
        if prices[i] < smallest:
            smallest = prices[i]
        elif prices[i] - smallest > biggest:
            biggest = prices[i] - smallest

    return biggest


if __name__ == '__main__':
        # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
