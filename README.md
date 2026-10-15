# AP22 — Comprobador de congruencias

**Autor:** Xavier Margalef Riestra · **Módulo:** MF0489 Semana 2 · **Fecha:** 15/10/2026

## Resumen

| | |
|---|---|
| **Objetivo** | Programa en Python que pide tres datos y dice si hay congruencia entre ellos |
| **Qué comprueba** | `a ≡ b (mod n)` |
| **Resultado** | Completado. 5/5 pruebas OK, incluido el ejemplo de la lección (63 ≡ 83 mod 10) |

## Qué hace el programa

**¿Qué datos pide?** Tres enteros: `a`, `b` y el módulo `n` (mayor que 0).

**¿Cómo decide si son congruentes?** Con la definición de la lección, comprobando los dos criterios equivalentes y mostrándolos:

| Criterio | Cálculo | 63, 83, mod 10 |
|---|---|---|
| Mismo resto | `a mod n == b mod n` | 3 = 3 ✅ |
| Diferencia múltiplo de n | `(a − b) mod n == 0` | −20 = 10 · (−2) ✅ |

Ejemplo de ejecución:

```
a: 63
b: 83
n (modulo, > 0): 10

63 mod 10 = 3
83 mod 10 = 3
63 - 83 = -20 = 10 * (-2)  -> multiplo de 10

Resultado: 63 ≡ 83 (mod 10)  -> SON congruentes
```

## Validación de entradas

| Caso | Qué hace | Por qué |
|---|---|---|
| Texto que no es un número | Lo vuelve a pedir | Evita que el programa se cierre con un error |
| `n = 0` | Lo vuelve a pedir | El módulo 0 no está definido (sería dividir entre 0) |
| `n` negativo | Lo vuelve a pedir | Se trabaja con `n > 0`, que es la convención habitual |
| `a` o `b` negativos | Se aceptan | En Python `-7 % 5 = 3` (resto siempre ≥ 0 con `n > 0`), así que el resultado es correcto |

Validar todo lo que entra por teclado es la base de la codificación segura (ISO 27001 A.8.28, OWASP *Input Validation*). Aquí es un ejercicio de mates, pero el hábito es el mismo.

## Por qué importa en ciberseguridad

La aritmética modular es la base de la criptografía asimétrica:

| Algoritmo | Dónde entra el módulo |
|---|---|
| Diffie-Hellman | `A = gᵃ mod p` (lo usé en la PE 89.1) |
| RSA | `c = mᵉ mod n` y `m = cᵈ mod n` |
| ChaCha20 / AES | Sumas módulo 2³² y operaciones en GF(2⁸) |

## Pruebas

| Prueba | Qué comprueba |
|---|---|
| `test_ejemplo_de_la_leccion` | 63 ≡ 83 (mod 10): restos 3 y 3, diferencia −20 |
| `test_no_congruentes` | 63 y 84 (mod 10) no son congruentes |
| `test_negativos` | −7 ≡ 3 (mod 5) |
| `test_ambos_criterios_coinciden` | Los dos criterios dan lo mismo para 11.767 combinaciones |
| `test_modulo_no_valido` | `n = 0` y `n < 0` se rechazan |

## Cómo ejecutarlo

Solo librería estándar, no hace falta instalar nada:

```bash
python3 congruencias.py        # programa interactivo
python3 -m unittest -v         # 5 pruebas
```

Proceso, decisiones y dificultades en [`WORKLOG.md`](WORKLOG.md).

```
ap22-congruencias/
├── README.md
├── WORKLOG.md
├── congruencias.py
└── test_congruencias.py
```
