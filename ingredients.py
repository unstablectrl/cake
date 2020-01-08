import pickle
import sys

import nltk


def buy_ingredients():
    nltk.download('words', download_dir='ingredients')


if __name__ == "__main__":

    if len(sys.argv) == 2:
        action = sys.argv[1]
    else:
        print('Shop closed... no ingredients')
        sys.exit()

    if action == 'buy':
        buy_ingredients()
    else:
        print('No money... no ingredients')
        sys.exit()
