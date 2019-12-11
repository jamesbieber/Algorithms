#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    batch = 0
    more = True  # keep track of extra ingredients

    while more:
        for k, v in ingredients.items():
            if v - recipe[k] < 0:
                return batch
            else:
                v -= recipe[k]
                if v - recipe[k] < 0:
                    more = False

        batch += 1

    return batch


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
