import unittest

def add(numbers):
    delim=','
    if numbers[:2]=='//':
        delim = numbers[numbers.index('//')+2 : numbers.index('\n')]
        numbers = numbers[numbers.index('\n')+1:]
        
    if numbers == '':
        return 0
    
    if '\n' in numbers:
        numbers = numbers.replace('\n' , delim)
        
    if delim in numbers:
        numberList = numbers.split(delim)
        
    else:
        numberList=[numbers]
        
    sum = 0
    for x in numberList:
        sum += float(x)
    return sum


class Tests(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(add(''),0)
class TestStringMethods(unittest.TestCase):
    def test_one_value(self):
        self.assertEqual(add('1'),1)

    def test_one_big_value(self):
        self.assertEqual(add('123'),123)

    def test_two_values(self):
        self.assertEqual(add('1,2'),3)

    def test_many_float_values(self):
        self.assertAlmostEqual(add('1,2.5,3.4'),6.9)

    def test_add_many(self):
        self.assertEqual(add('1,2,3,4,5'),15)

    def test_mix_delimiters(self):
        self.assertEqual(add('1,2,3\n4\n5'),15)

    def test_all_new_line(self):
        self.assertEqual(add('1\n2\n3\n4\n5'),15)

    def test_new_delimiter(self):
        self.assertEqual(add('//;\n1;2;3;4;5'),15)

    def test_long_delimiter(self):
        self.assertEqual(add('//;;;\n1;;;2;;;3;;;4;;;5'),15)

if __name__ == '__main__':
    unittest.main()
