import unittest

from Python.Condicionales.Problema3 import imprimir


class MyTestCase(unittest.TestCase):
    def test_imprimir(self):
        self.assertEqual(imprimir("Elkin"), "E"+"n")
        self.assertEqual(imprimir("Armario"), "A"+"o")



if __name__ == '__main__':
    unittest.main()
