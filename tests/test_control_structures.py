import unittest

from control_structures.first import categorize_age
from control_structures.second import collect_numbers


class TestConditionalConstructions(unittest.TestCase):
    def test_categorize_age_child(self):
        self.assertEqual(categorize_age(10), "Ребенок")
    
    def test_categorize_age_teen(self):
        self.assertEqual(categorize_age(15), "Подросток")
    
    def test_categorize_age_adult(self):
        self.assertEqual(categorize_age(30), "Взрослый")
    
    def test_categorize_age_elder(self):
        self.assertEqual(categorize_age(70), "Пожилой человек")
    
    def test_categorize_age_invalid(self):
        self.assertEqual(categorize_age(-5), "Некорректный возраст")

class TestWhileLoop(unittest.TestCase):
    def test_collect_numbers(self):
        with unittest.mock.patch('builtins.input', side_effect=[1, 2, 3, 0]):
            result = collect_numbers()
            self.assertEqual(result[0], [1, 2, 3])
            self.assertEqual(result[1], 6)
            self.assertEqual(result[2], 2.0)
            self.assertEqual(result[3], 3)
            self.assertEqual(result[4], 1)
            self.assertEqual(result[5], 2)
            self.assertEqual(result[6], 1)
            self.assertEqual(result[7], 3)
            self.assertEqual(result[8], 0)

    def test_collect_numbers_empty(self):
        with unittest.mock.patch('builtins.input', side_effect=[0]):
            result = collect_numbers()
            self.assertEqual(result, ([], 0, 0, None, None, 0, 0, 0, 0))

if __name__ == '__main__':
    unittest.main()
