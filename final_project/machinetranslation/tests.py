import unittest
import translator

from translator import englishToFrench, frenchToEnglish
from translator import englishText, frenchText

class Tests(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(englishToFrench(englishText),'Hope you are having a good day')

    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish(frenchText),"J'espère que tu passes une bonne journée"
)

if __name__=='__main__':
    unittest.main()