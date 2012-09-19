# reverse test suite

import unittest

from reverse import reverse_str

class TestReverse(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(reverse_str(''), '')

    def test_single(self):
        self.assertEqual(reverse_str('q'), 'q')

    def test_awesome(self):
        self.assertEqual(reverse_str('awesome'), 'emosewa')

    def test_race_car(self):
        self.assertEqual(reverse_str('race car'), 'rac ecar')

    def test_sentence(self):
        self.assertEqual(reverse_str('This is a useful instance '
                                     'of Test-Driven Development.'),
                         '.tnempoleveD nevirD-tseT fo ecnatsni lufesu '
                         'a si sihT')

if __name__ == '__main__':
    unittest.main()
