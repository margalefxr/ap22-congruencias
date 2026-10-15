# WORKLOG — AP22

| # | Paso | Resultado |
|---|---|---|
| 1 | Función con los dos criterios de congruencia | 63 ≡ 83 (mod 10) ✅ |
| 2 | Validación de entradas | Texto o `n ≤ 0` → vuelve a preguntar |
| 3 | 4 pruebas con `unittest` | 4/4 OK |

## Dificultades

| Dificultad | Solución |
|---|---|
| `-7 % 5` da `3` en Python y `-2` en C o Java | Con `n > 0` Python da el resto positivo, que es el correcto; hay un test con negativos |
| Si se escribe texto en vez de un número, `int()` falla | `pedir_numero()` repite la pregunta |
