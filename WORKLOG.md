# WORKLOG — AP22 Comprobador de congruencias

## Pasos

| # | Paso | Resultado |
|---|---|---|
| 1 | Leer la lección de aritmética modular | Dos criterios equivalentes: mismo resto y diferencia múltiplo de `n` |
| 2 | Función `comprobar_congruencia()` con los dos criterios | 63 ≡ 83 (mod 10) ✅ |
| 3 | Validación de entradas (no numérico, `n ≤ 0`) | Repite la pregunta en vez de fallar |
| 4 | Pruebas con `unittest` | 5/5 OK |

## Decisiones (por qué A y no B)

| Decisión | Elegido (A) | Descartado (B) | Motivo |
|---|---|---|---|
| Criterio | Mostrar los dos (restos y diferencia) | Solo uno | Son las dos definiciones de la lección; enseñarlas demuestra que coinciden |
| Módulo | Solo `n > 0` | Aceptar `n ≤ 0` | `n = 0` no está definido; `n` negativo no aporta nada |
| Dependencias | Solo librería estándar | Librerías externas | No hacen falta: menos superficie de supply chain |
| Estructura | Lógica en funciones, `input()` solo en `main()` | Todo dentro del `input()` | Permite probar la lógica sin teclado |

## Dificultades

| ID | Dificultad | Solución |
|---|---|---|
| D-01 | En Python `-7 % 5` da `3` y en otros lenguajes (C, Java) `-2` | Con `n > 0`, Python siempre da el resto positivo, que es el matemáticamente correcto; hay un test con negativos |
| D-02 | Un `input()` que recibe texto en vez de número hace que el programa falle | `leer_entero()` vuelve a preguntar hasta recibir un entero |
