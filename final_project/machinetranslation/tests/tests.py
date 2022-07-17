import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french(''), 'No input')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('Yo'), 'Bonjour')

class TestFrenchToEnglish(unittest.TestCase):
    def test_french_to_english(self):
        self.assertEqual(french_to_english(''), 'No input')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Bonjour'), 'Yo')
        