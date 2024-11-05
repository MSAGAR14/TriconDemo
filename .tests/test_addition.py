import unittest

# Define the addition function for testing purposes
def add(num1, num2):
    return num1 + num2

class TestAddition(unittest.TestCase):
    
    def test_positive_numbers(self):
        """Test addition with positive numbers"""
        result = add(5, 10)
        self.assertEqual(result, 15, "Should be 15")

    def test_with_zero(self):
        """Test addition with zero"""
        result = add(0, 0)
        self.assertEqual(result, 0, "Should be 0")
    
    def test_negative_numbers(self):
        """Test addition with negative numbers"""
        result = add(-3, -7)
        self.assertEqual(result, -10, "Should be -10")
    
    def test_mixed_sign_numbers(self):
        """Test addition with one positive and one negative number"""
        result = add(8, -2)
        self.assertEqual(result, 6, "Should be 6")
    
    def test_large_numbers(self):
        """Test addition with large numbers"""
        result = add(1000000, 2000000)
        self.assertEqual(result, 3000000, "Should be 3000000")

if __name__ == '__main__':
    unittest.main()
