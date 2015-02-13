import hiker
import unittest

class TestHiker(unittest.TestCase):

    def test_life_the_universe_and_everything(self):
        '''simple example to start you off'''
        douglas = hiker.Hiker()
        self.assertEqual(1, douglas.answer(1))        
        self.assertEqual(2, douglas.answer(2))
        self.assertEqual('fizz', douglas.answer(3))
        self.assertEqual('buzz', douglas.answer(5))
        self.assertEqual('fizzbuzz', douglas.answer(30))

if __name__ == '__main__':
    unittest.main()