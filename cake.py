import random
import sys

import nltk
from nltk.corpus import words


def make_cake(ingredients, secret_ingredient):
    random.seed(secret_ingredient)
    return random.sample(ingredients, k=4)


if __name__ == "__main__":

    if len(sys.argv) == 2:
        secret_ingredient = sys.argv[1]
    else:
        print('The Cake is a lie!')
        sys.exit()

    nltk.data.path.append('ingredients')
    ingredients = words.words()

    cake = make_cake(ingredients, secret_ingredient)

    print(f'The Cake is real?\n{cake}')
