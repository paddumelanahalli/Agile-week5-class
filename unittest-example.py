import unittest

class TestSomething(unittest.TestCase):

    def test_example(self):
        self.assertEqual(1 + 1, 2)

if __name__ == "__main__":
    unittest.main()

''' output
============================= test session starts =============================
collecting ... collected 1 item

unittest-example.py::TestSomething::test_example PASSED                  [100%]

============================== 1 passed in 0.01s ==============================

Process finished with exit code 0
'''
