# ! /usr/bin/env python
from random import randint

SCRABBLES_SCORES = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                    (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
ACTION_ONE_WORD = 1
ACTION_MAX = 2
ACTION_WORD_FROM_FILE = 3


class Scrabble:
    def __init__(self, scrabbles_scores):
        self.letter_scores = {
            letter: score for score, letters in scrabbles_scores for letter in letters.split()
    }

    def _get_file_content(self, file_path):
        with open(file_path, 'r') as dictionary_file:
            file_content = dictionary_file.read()
        word_list = file_content.strip().split('\n')
        return word_list

    def count_score(self, word):
        score = 0
        for letter in word:
            try:
                score += self.letter_scores[letter.upper()]
            except KeyError:
                raise KeyError('Wrong input value')
        return score

    def _count_many(self, word_list):
        scores = {}
        for word in word_list:
            score = self.count_score(word)
            scores.setdefault(score, [])
            scores[score].append(word)
        return scores

    def _get_scores_from_file(self, file_path):
        word_list = self._get_file_content(file_path)
        scores = self._count_many(word_list)
        return scores

    def highest_score(self, file_path):
        return max(self._get_scores_from_file(file_path))

    def get_word_by_score(self, score, file_path):
        scores = self._get_scores_from_file(file_path)
        if score in scores:
            length = len(scores[score])
            if length > 1:
                index = randint(0, length - 1)
                return scores[score][index]
            else:
                return scores[score][0]


def run():
    scrabble = Scrabble(SCRABBLES_SCORES)
    print('Available options:\n 1 count score for word\n 2 return maximum score in file\n 3 display word for given score\n')

    try:
        action = int(input())
    except ValueError:
        raise ValueError('Wrong input value. Correct value should be integer between 1 and 3')

    if action == ACTION_ONE_WORD:
        input_word = input('Please enter word:')
        print('Your word score is: {}'.format(scrabble.count_score(input_word)))
    elif action == ACTION_MAX:
        file_path = input('Enter file path')
        print('The highest score in file is: {}'.format(scrabble.highest_score(file_path)))
    elif action == ACTION_WORD_FROM_FILE:
        file_path = input('Enter file path')
        score = int(input('Enter score'))
        result = scrabble.get_word_by_score(score, file_path)
        if result:
            print(result)
    else:
        raise ValueError('Value out of range.')


if __name__ == '__main__':
    run()

