import unittest

from main import Scrabble, SCRABBLES_SCORES


class MyTestClass(unittest.TestCase):
    def setUp(self):
        self.scrabble = Scrabble(SCRABBLES_SCORES)

    def test_ewa(self):
        self.assertEqual(self.scrabble.count_score('ewa'), 6)

    def test_max(self):
        self.assertEqual(self.scrabble.highest_score('dictionary.txt'), 20)

    def test_word_by_score_does_not_exist(self):
        self.assertEqual(self.scrabble.get_word_by_score(3, 'dictionary.txt'), None)

    def test_word_by_score_one_result(self):
        self.assertEqual(self.scrabble.get_word_by_score(20, 'dictionary.txt'), 'availability')

    def test_word_by_score_many_results(self):
        self.assertIn(self.scrabble.get_word_by_score(6, 'dictionary.txt'), ['ewa', 'ivo', 'eho'])


if __name__ == '__main__':
    unittest.main()
