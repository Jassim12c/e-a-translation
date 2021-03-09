import unittest
import main

class TestMain(unittest.TestCase):

    def test_change_two_letters(self):
        arg = 'sh'
        self.assertIn(arg, main.digraphs)
        self.assertIsInstance(arg, str)
