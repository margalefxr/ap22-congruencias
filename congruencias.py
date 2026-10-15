# AP22 - Comprobador de congruencias
# Xavier Margalef Riestra
#
# Pide a, b y n y dice si a es congruente con b modulo n (a ≡ b mod n)


def es_congruente(a, b, n):
    # Son congruentes si dan el mismo resto al dividir entre n
    return a % n == b % n


def pedir_numero(texto):
    # Vuelve a preguntar si no se mete un numero entero
    while True:
        try:
            return int(input(texto))
        except ValueError:
            print("Eso no es un numero entero, prueba otra vez")


if __name__ == "__main__":
    print("Comprobador de congruencias: a ≡ b (mod n)")

    a = pedir_numero("a: ")
    b = pedir_numero("b: ")
    n = pedir_numero("n: ")
    while n <= 0:
        print("n tiene que ser mayor que 0")
        n = pedir_numero("n: ")

    print()
    print(a, "mod", n, "=", a % n)
    print(b, "mod", n, "=", b % n)
    print(a, "-", b, "=", a - b)

    if es_congruente(a, b, n):
        print(a - b, "es multiplo de", n)
        print("Resultado:", a, "≡", b, "(mod", str(n) + ") -> SON congruentes")
    else:
        print(a - b, "no es multiplo de", n)
        print("Resultado:", a, "≢", b, "(mod", str(n) + ") -> NO son congruentes")
