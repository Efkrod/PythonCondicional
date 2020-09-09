import unittest

from Python.Condicionales.Problema2 import par


class MyTestCase(unittest.TestCase):
    def test_par(self):
        self.assertEqual(par(2), True)
        self.assertEqual(par(7), False)


if __name__ == '__main__':
    unittest.main()
