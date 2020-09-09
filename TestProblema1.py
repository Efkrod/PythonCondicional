import unittest

from Python.Condicionales.Problema1 import edad_2070


class MyTestCase(unittest.TestCase):
    def test_edad_2070(self):
        self.assertEqual(edad_2070(21, 2020),71)
        self.assertEqual(edad_2070(29, 2020),79)

if __name__ == '__main__':
    unittest.main()
