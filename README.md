# AP22 — Comprobador de congruencias

**Autor:** Xavier Margalef Riestra · **Módulo:** MF0489 Semana 2 · **Fecha:** 15/10/2026

Programa en Python que pide `a`, `b` y `n` y comprueba si `a ≡ b (mod n)`.

## Cómo lo comprueba

Con los dos criterios de la lección, que son equivalentes:

| Criterio | Cálculo | Ejemplo 63, 83, mod 10 |
|---|---|---|
| Mismo resto | `a mod n == b mod n` | 3 = 3 ✅ |
| Diferencia múltiplo de n | `(a − b) mod n == 0` | −20 = 10 · (−2) ✅ |

```
63 mod 10 = 3
83 mod 10 = 3
63 - 83 = -20 = 10 * (-2)  -> multiplo de 10

Resultado: 63 ≡ 83 (mod 10)  -> SON congruentes
```

## Decisiones

| Decisión | Por qué |
|---|---|
| Validar entradas (no numérico o `n ≤ 0` → se vuelve a pedir) | `n = 0` no está definido; validar la entrada es básico en codificación segura (ISO 27001 A.8.28, OWASP) |
| Solo librería estándar | Sin dependencias, sin riesgo de supply chain |
| Lógica separada del `input()` | Se puede probar sin teclado (5 tests) |

La aritmética modular es la base de RSA y Diffie-Hellman (`A = gᵃ mod p`).

## Ejecutar

```bash
python3 congruencias.py
python3 -m unittest -v
```

Dificultades encontradas en [`WORKLOG.md`](WORKLOG.md).
