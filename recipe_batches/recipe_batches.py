#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    batch = None
    if recipe.keys() == ingredients.keys():
        for i in ingredients:
            if ingredients[i] > recipe[i]:
                if batch:
                    if (ingredients[i] // recipe[i]) < batch:
                        batch = (ingredients[i] // recipe[i])
                else:
                    batch = (ingredients[i] // recipe[i])
    else:
        return 0

    return batch

    # batch = 0
    # more = True  # keep track of extra ingredients

    # while more:
    #     for k, v in ingredients.items():
    #         if ingredients[k] == recipe[k]:
    #             if v - recipe[k] < 0:
    #                 return batch
    #             else:
    #                 v -= recipe[k]
    #                 if v - recipe[k] < 0:
    #                     more = False
    #         else:
    #             return batch

    #     batch += 1

    # return batch


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 1332, 'butter': 503, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
