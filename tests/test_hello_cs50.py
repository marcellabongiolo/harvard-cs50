import unittest

from hello_cs50 import saudar


class TestSaudacao(unittest.TestCase):
    def test_nome(self):
        self.assertEqual(saudar("Marcella"), "Olá, Marcella!")

    def test_remove_espacos_externos(self):
        self.assertEqual(saudar("  João  "), "Olá, João!")

    def test_rejeita_nome_vazio(self):
        with self.assertRaises(ValueError):
            saudar("  ")

    def test_rejeita_tipo_invalido(self):
        with self.assertRaises(TypeError):
            saudar(123)


if __name__ == "__main__":
    unittest.main()
