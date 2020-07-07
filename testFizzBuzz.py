import unittest
import fizzBuzz


class TestFizzBuzz(unittest.TestCase):
    def test_getResult_returnFizz(self):
        self.assertEqual(fizzBuzz.main(3), 'Fizz')

    def test_getResult_returnBuzz(self):
        self.assertEqual(fizzBuzz.main(5), 'Buzz')      
        self.assertEqual(fizzBuzz.main('5'), 'Buzz')   

    def test_getResult_returnEmpty(self):
        self.assertEqual(fizzBuzz.main(2), '')       
        self.assertEqual(fizzBuzz.main('a'), '') 
            

    def test_getResult_returnFizzBuzz(self):
        self.assertEqual(fizzBuzz.main(15), 'FizzBuzz')      
        self.assertEqual(fizzBuzz.main('15'), 'FizzBuzz')    