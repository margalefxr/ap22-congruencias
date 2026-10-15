# Pruebas del AP22
# Ejecutar: python3 -m unittest -v

import unittest
from congruencias import es_congruente


class TestCongruencias(unittest.TestCase):

    def test_ejemplo_leccion(self):
        self.assertTrue(es_congruente(63, 83, 10))

    def test_no_congruentes(self):
        self.assertFalse(es_congruente(63, 84, 10))

    def test_negativos(self):
        # -7 mod 5 = 3 y 3 mod 5 = 3
        self.assertTrue(es_congruente(-7, 3, 5))

    def test_los_dos_criterios_coinciden(self):
        # mismo resto <-> la diferencia es multiplo de n
        for a in range(-20, 21):
            for b in range(-20, 21):
                for n in range(1, 8):
                    self.assertEqual(es_congruente(a, b, n), (a - b) % n == 0)


if __name__ == "__main__":
    unittest.main()
