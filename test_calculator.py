import unittest
from calculator import divide

class TestCalculator(unittest.TestCase):
    def test_normal_division(self):
        """测试正常的除法运算"""
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(15, 3), 5)
        self.assertEqual(divide(8, 4), 2)
        
    def test_float_division(self):
        """测试浮点数除法"""
        self.assertAlmostEqual(divide(5.0, 2.0), 2.5)
        self.assertAlmostEqual(divide(7.5, 2.5), 3.0)
        
    def test_negative_numbers(self):
        """测试负数除法"""
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(10, -2), -5)
        self.assertEqual(divide(-10, -2), 5)
        
    def test_zero_division(self):
        """测试除以零的情况"""
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)
            
    def test_invalid_input(self):
        """测试无效输入"""
        with self.assertRaises(TypeError):
            divide("10", 2)
        with self.assertRaises(TypeError):
            divide(10, "2")
            
if __name__ == '__main__':
    unittest.main() 