from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution
        from random import randint

        fpath = './files/testfile.txt'
        n = randint(1,5)
        res = solution(fpath, n)

        self.assertEqual(res[-1], 'This is the last line.')
        self.assertEqual(len(res), n)
        self.assertIsInstance(res, list)