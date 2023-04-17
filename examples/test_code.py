import unittest

class TestBasic(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(1, 1)        
    
    def test_false(self):
        self.assertFalse(1 == 2)
    
    def test_true(self):
        self.assertTrue("Bank" == "Bank")

if __name__ == '__main__':
    unittest.main()