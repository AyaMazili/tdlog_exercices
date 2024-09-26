import unittest

class Word:
    def __init__(self, word):
        self.word = word

    def solution(self, ending):
        return self.word.endswith(ending)

# Créer les tests unitaires
class TestWordSolution(unittest.TestCase):

    def test_fixed_tests_true(self):
        fixed_tests_True = (
            ("samurai", "ai"),
            ("ninja", "ja"),
            ("sensei", "i"),
            ("abc", "abc"),
            ("abcabc", "bc"),
            ("fails", "ails"),
        )

        for string, ending in fixed_tests_True:
            word_obj = Word(string)
            with self.subTest(f"{string} ends with {ending}"):
                self.assertTrue(word_obj.solution(ending))

    def test_fixed_tests_false(self):
        fixed_tests_False = (
            ("sumo", "omo"),
            ("samurai", "ra"),
            ("abc", "abcd"),
            ("ails", "fails"),
            ("this", "fails"),
            ("spam", "eggs"),
        )

        for string, ending in fixed_tests_False:
            word_obj = Word(string)
            with self.subTest(f"{string} does not end with {ending}"):
                self.assertFalse(word_obj.solution(ending))


# Exécuter les tests
if __name__ == "__main__":
    unittest.main()
