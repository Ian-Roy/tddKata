import unittest

def add(numbers):
    if numbers == '':
        return 0 
    numberList = numbers.split(',')
    sum = 0
    for x in numberList:
        sum += float(x)
    return sum


class Tests(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(add(''),0)

    def test_one_value(self):
        self.assertEqual(add('1'),1)

    def test_two_values(self):
        self.assertEqual(add('1,2'),3)
    

if __name__ == '__main__':
    unittest.main()
