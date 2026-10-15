# AP22 — Comprobador de congruencias

**Autor:** Xavier Margalef Riestra · **Módulo:** MF0489 Semana 2 · **Fecha:** 15/10/2026

Programa en Python que pide `a`, `b` y `n` y dice si `a ≡ b (mod n)`.

## Funcionamiento

Uso los dos criterios de la lección, que dan el mismo resultado:

| Criterio | Cálculo | 63, 83, mod 10 |
|---|---|---|
| Mismo resto | `a mod n == b mod n` | 3 = 3 ✅ |
| Diferencia múltiplo de n | `(a − b) mod n == 0` | −20 = 10 · (−2) ✅ |

```
63 mod 10 = 3
83 mod 10 = 3
63 - 83 = -20
-20 es multiplo de 10
Resultado: 63 ≡ 83 (mod 10) -> SON congruentes
```

## Decisiones

| Decisión | Motivo |
|---|---|
| Validar entradas: si no es un número o `n ≤ 0`, lo vuelve a pedir | `n = 0` no está definido. Validar la entrada es codificación segura básica (ISO 27001 A.8.28, OWASP) |
| Solo librería estándar | Sin dependencias, sin riesgo de supply chain |
| Lógica separada del `input()` | Para poder probarla sin teclado (4 tests) |

La aritmética modular es la base de RSA y Diffie-Hellman (`A = gᵃ mod p`).

## Ejecución

```bash
python3 congruencias.py
python3 -m unittest -v
```

Dificultades en [`WORKLOG.md`](WORKLOG.md).
