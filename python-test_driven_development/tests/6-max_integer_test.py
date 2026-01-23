#!/usr/bin/python3
import unittest

class TestSomething(unittest.TestCase):
    def test_example(self):
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
def max_integer(list=[]):
    if my_list == []:
        return None
    else:
        val_max = my_list[0]
        for i in my_list:
            if i > val_max:
                val_max = i
    return val_max