"""Pruebas del AP22. Ejecutar desde esta carpeta: python -m unittest -v"""

import unittest

from congruencias import comprobar_congruencia


class TestCongruencias(unittest.TestCase):

    def test_ejemplo_de_la_leccion(self):
        r = comprobar_congruencia(63, 83, 10)
        self.assertTrue(r["congruentes"])
        self.assertEqual((r["resto_a"], r["resto_b"], r["diferencia"]), (3, 3, -20))

    def test_no_congruentes(self):
        self.assertFalse(comprobar_congruencia(63, 84, 10)["congruentes"])

    def test_negativos(self):
        # -7 mod 5 = 3 y 3 mod 5 = 3 -> congruentes; -7 - 3 = -10 es multiplo de 5
        self.assertTrue(comprobar_congruencia(-7, 3, 5)["congruentes"])

    def test_ambos_criterios_coinciden(self):
        for a in range(-20, 21):
            for b in range(-20, 21):
                for n in range(1, 8):
                    r = comprobar_congruencia(a, b, n)
                    self.assertEqual(r["congruentes"], (a - b) % n == 0)

    def test_modulo_no_valido(self):
        for n in (0, -3):
            with self.assertRaises(ValueError):
                comprobar_congruencia(1, 2, n)


if __name__ == "__main__":
    unittest.main()
