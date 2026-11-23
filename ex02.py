"""Programa de pràctica de funcions amb return (TASCA 02 - M0485)."""


def mostrar_menu():
    """Mostra per pantalla el menú principal d'opcions."""
    # Imprimeixo el menú tal com surt a l'exemple, amb l'opció 0 per sortir
    print("\n    Funcions 2")
    print("=" * 20)
    print("1. Comptar majúscules i minúscules")
    print("2. Any de traspàs")
    print("3. Dies del mes")
    print("4. Número perfecte")
    print("5. Números perfectes fins a 10000  (repte)")
    print("0. Sortir")


def introduir_int_segur(missatge, minim=None, maxim=None):
    """
    Demana a l'usuari un número enter de forma segura.

    Args:
        missatge (str): Text a mostrar a l'usuari
        minim (int, opcional): Valor mínim acceptat
        maxim (int, opcional): Valor màxim acceptat

    Returns:
        int: Número enter vàlid introduït per l'usuari

    Exemple:
        >>> introduir_int_segur("Introdueix la teva edat: ", 0, 120)
        Introdueix la teva edat: 25
        25
    """
    # Utilitzo una bandera booleana per controlar el bucle sense while True ni break
    entrada_valida = False
    valor = 0

    while not entrada_valida:
        text = input(missatge)

        # Comprovo si és un enter positiu amb isdigit() tal com indica l'enunciat
        if not text.isdigit():
            print("Has d'introduir un número enter.")
        else:
            candidat = int(text)
            # Reviso primer el límit mínim si s'ha especificat
            if minim is not None and candidat < minim:
                print(f"El número ha de ser més gran o igual que {minim}.")
            # Després reviso el límit màxim si s'ha especificat
            elif maxim is not None and candidat > maxim:
                print(f"El número ha de ser més petit o igual que {maxim}.")
            else:
                valor = candidat
                entrada_valida = True

    return valor


def comptar_majuscules_minuscules(cadena):
    """
    Compta les lletres majúscules i minúscules d'una cadena.

    Args:
        cadena (str): Cadena de text a analitzar

    Returns:
        tuple: (majúscules, minúscules)

    Exemple:
        >>> comptar_majuscules_minuscules('Una Cadena De Prova')
        (4, 12)
    """
    majuscules = 0
    minuscules = 0
    index = 0

    # Recorro cada caràcter de la cadena i només sumo si és lletra majúscula o minúscula
    while index < len(cadena):
        caracter = cadena[index]
        if caracter.isupper():
            majuscules = majuscules + 1
        elif caracter.islower():
            minuscules = minuscules + 1
        index = index + 1

    return (majuscules, minuscules)


def es_any_traspas(a):
    """
    Determina si un any és de traspàs.

    Regles:
    - Divisible per 4, però no per 100,
    - excepte si és divisible per 400.

    Args:
        a (int): Any a comprovar

    Returns:
        bool: True si és any de traspàs, False en cas contrari

    Exemples:
        >>> es_any_traspas(2000)
        True
        >>> es_any_traspas(1900)
        False
        >>> es_any_traspas(2024)
        True
    """
    # Els múltiples de 400 sempre són de traspàs; els altres múltiples de 100 no ho són
    if a % 400 == 0:
        resultat = True
    elif a % 100 == 0:
        resultat = False
    elif a % 4 == 0:
        resultat = True
    else:
        resultat = False

    return resultat


def comptar_dies_mes(mes, a):
    """
    Retorna el nombre de dies d'un mes en un any determinat.

    Args:
        mes (int): Número del mes (1-12)
        a (int): Any a considerar

    Returns:
        int: Nombre de dies del mes

    Exemples:
        >>> comptar_dies_mes(2, 2024)    # Febrer en any de traspàs
        29
        >>> comptar_dies_mes(2, 2023)    # Febrer en any normal
        28
        >>> comptar_dies_mes(4, 2023)    # Abril
        30

    Nota: Utilitza la funció es_any_traspas() per al febrer.
    """
    # Guardo els dies estàndard de cada mes en una llista (índex 0 per al gener, etc.)
    dies_per_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dies = dies_per_mes[mes - 1]

    # Si és febrer (mes 2) i l'any és de traspàs, passa a tenir 29 dies
    if mes == 2 and es_any_traspas(a):
        dies = 29

    return dies


def es_num_perfecte(numero):
    """
    Comprova si un número és perfecte.

    Un número perfecte és igual a la suma dels seus divisors
    positius propis (excloent el número mateix).

    Args:
        numero (int): Número a comprovar (enter positiu)

    Returns:
        bool: True si és perfecte, False en cas contrari

    Exemples:
        >>> es_num_perfecte(6)     # 1+2+3 = 6
        True
        >>> es_num_perfecte(28)    # 1+2+4+7+14 = 28
        True
        >>> es_num_perfecte(12)
        False
    """
    # Un número menor o igual que 1 no pot tenir divisors propis positius que sumen el mateix valor
    if numero <= 1:
        es_perfecte = False
    else:
        suma_divisors = 0
        divisor = 1

        # Només cal revisar divisors fins a la meitat del número (cap divisor propi pot superar numero // 2)
        while divisor <= numero // 2:
            if numero % divisor == 0:
                suma_divisors = suma_divisors + divisor
            divisor = divisor + 1

        es_perfecte = suma_divisors == numero

    return es_perfecte


def main():
    """Controla el flux principal del programa i mostra els resultats de cada opció."""
    opcio = -1

    # Repeteixo el menú fins que l'usuari seleccioni 0
    while opcio != 0:
        mostrar_menu()
        opcio = introduir_int_segur("Escull una opció: ", 0, 5)

        if opcio == 1:
            text = input("Introdueix una cadena: ")
            maj, min_count = comptar_majuscules_minuscules(text)
            print(f"Majúscules: {maj}, Minúscules: {min_count}")

        elif opcio == 2:
            any_usuari = introduir_int_segur("Introdueix un any: ", 1)
            if es_any_traspas(any_usuari):
                print(f"L'any {any_usuari} és de traspàs.")
            else:
                print(f"L'any {any_usuari} no és de traspàs.")

        elif opcio == 3:
            any_usuari = introduir_int_segur("Introdueix un any: ", 1)
            mes_usuari = introduir_int_segur("Mes (1-12): ", 1, 12)
            dies = comptar_dies_mes(mes_usuari, any_usuari)
            print(f"El mes {mes_usuari} de l'any {any_usuari} té {dies} dies.")

        elif opcio == 4:
            num_usuari = introduir_int_segur("Introdueix un número enter positiu: ", 1)
            if es_num_perfecte(num_usuari):
                print(f"El {num_usuari} és un número perfecte.")
            else:
                print(f"El {num_usuari} no és un número perfecte.")

        elif opcio == 5:
            # Repte: busco tots els números perfectes entre 1 i 10000 amb es_num_perfecte()
            perfectes = []
            candidat = 1
            while candidat <= 10000:
                if es_num_perfecte(candidat):
                    perfectes.append(str(candidat))
                candidat = candidat + 1
            print("Números perfectes fins a 10000:", ", ".join(perfectes))

        elif opcio == 0:
            print("Fins aviat!")


if __name__ == "__main__":
    main()