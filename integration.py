import unittest

class TestStringMethods(unittest.TestCase):
    # Prueba si dos cadenas de textos son la misma
    def test_upper(self):
        self.assertEqual('foX'.upper(), 'FOO')

    # Prueba si una cadena de texto está en mayúsculas
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    # Prueba si la función para seprar ambos falla, al no ser un string
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()