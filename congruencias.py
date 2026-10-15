"""
AP22 - Comprobador de congruencias
Autor: Xavier Margalef Riestra

Pide tres enteros (a, b, n) y comprueba si a ≡ b (mod n).
Dos criterios equivalentes, ambos mostrados:
  1. a mod n == b mod n          (mismo resto)
  2. (a - b) es multiplo de n    (la diferencia es divisible por n)

Solo libreria estandar: sin dependencias externas.
"""


def leer_entero(mensaje: str) -> int:
    """Pide un entero y repite hasta que el usuario introduce uno valido."""
    while True:
        valor = input(mensaje).strip()
        try:
            return int(valor)
        except ValueError:
            print(f"  '{valor}' no es un entero. Prueba otra vez.")


def comprobar_congruencia(a: int, b: int, n: int) -> dict:
    """
    Devuelve los datos del calculo y si a ≡ b (mod n).
    n debe ser un entero positivo: el modulo 0 no esta definido y un modulo
    negativo da la misma relacion que su valor absoluto.
    """
    if n <= 0:
        raise ValueError("El modulo n debe ser un entero positivo (n > 0)")
    resto_a = a % n          # en Python el resto con n > 0 siempre es >= 0, tambien con a negativo
    resto_b = b % n
    diferencia = a - b
    return {
        "resto_a": resto_a,
        "resto_b": resto_b,
        "diferencia": diferencia,
        "cociente": diferencia // n,
        "congruentes": resto_a == resto_b,
    }


def main() -> None:
    print("== Comprobador de congruencias: a ≡ b (mod n) ==")
    a = leer_entero("a: ")
    b = leer_entero("b: ")
    n = leer_entero("n (modulo, > 0): ")
    while n <= 0:
        print("  El modulo debe ser mayor que 0.")
        n = leer_entero("n (modulo, > 0): ")

    r = comprobar_congruencia(a, b, n)
    print(f"\n{a} mod {n} = {r['resto_a']}")
    print(f"{b} mod {n} = {r['resto_b']}")
    print(f"{a} - {b} = {r['diferencia']}", end="")
    if r["congruentes"]:
        print(f" = {n} * ({r['cociente']})  -> multiplo de {n}")
        print(f"\nResultado: {a} ≡ {b} (mod {n})  -> SON congruentes")
    else:
        print(f"  -> no es multiplo de {n}")
        print(f"\nResultado: {a} ≢ {b} (mod {n})  -> NO son congruentes")


if __name__ == "__main__":
    main()
