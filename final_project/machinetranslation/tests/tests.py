import unittest
from translator import english_to_french, french_to_english, init_translator

translator_instance = init_translator()
class TestEnglishToFrench(unittest.TestCase):
   def test1(self):
       self.assertEqual(english_to_french("Good afternoon",translator_instance), "Bon après-midi")
       self.assertEqual(english_to_french("",translator_instance), "Invalid Text")
class TestFrenchToEnglish(unittest.TestCase):
   def test1(self):
      self.assertEqual(french_to_english("Bon après-midi",translator_instance), "Good afternoon")
      self.assertEqual(french_to_english("", translator_instance), "Invalid Text")
unittest.main()