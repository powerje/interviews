#!/usr/bin/env python3

__author__ = 'jep'


class WordProvider:

    def __init__(self, words):
        self._words = words

    def get_word_at_position(self, position):
        if position < len(self._words):
            return self._words[position]
        return None


def is_word_in_dictionary_naive(provider, word):
    i = 0
    current = provider.get_word_at_position(i)
    if current == word:
        return True
    while current != None:
        i = i + 1
        current = provider.get_word_at_position(i)
        if current == word:
            return True
    return False

def is_word_in_dictionary(provider, word):
    if provider.get_word_at_position(0) == word:
        return True
    if provider.get_word_at_position(1) == word:
        return True
    lower = 2
    upper = None
    guess = lower
    while True:
        current = provider.get_word_at_position(guess)
        if current == word:
            return True
        elif upper == None:
            if current == None:
                upper = guess
            else:
                guess = guess * 2
            continue
        elif lower >= upper:
            return False
        elif current == None or current > word: # move to the left, between bounds, set upper limit
            upper = guess - 1
        elif current < word: # move to the right
            lower = guess + 1
        guess = int(lower + (upper - lower) / 2)


if __name__ == '__main__':
    words = []
    with open('words.txt') as f:
        for word in f:
            words.append(word.rstrip().lower())
    provider = WordProvider(words)
    print(is_word_in_dictionary(provider, 'pseudofarcy'))

