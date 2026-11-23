"""Programa de pràctica de funcions sense return (TASCA 01 - M0485)."""

from datetime import date


def mostrar_menu():
    """Mostra per pantalla el menú principal del programa."""
    # Imprimeixo el títol i les opcions disponibles amb un separador visual
    print("\n    Funcions 1")
    print("=" * 20)
    print("1. Multiplica")
    print("2. Anys 2000")
    print("3. Gira del revés")
    print("4. Triangle de Pascal")
    print("5. Sortir")


def demanar_enter(missatge, missatge_error="Ha de ser un enter."):
    """Demana un número enter de manera segura fins que l'entrada sigui vàlida."""
    # Faig servir valor_valid = None per controlar el bucle sense usar while True ni break
    valor_valid = None

    while valor_valid is None:
        text = input(missatge)
        # Miro si comença per + o - per acceptar enters positius i negatius
        if text.startswith(("+", "-")):
            es_enter = len(text) > 1 and text[1:].isdigit()
        else:
            es_enter = text.isdigit()

        if es_enter:
            # Ja sé que és segur convertir-lo a int
            valor_valid = int(text)
        else:
            # Si no és un enter vàlid, aviso i el bucle torna a començar
            print(missatge_error)

    return valor_valid


def multiplica(a, b):
    """Rep dos números enters i mostra el resultat de la seva multiplicació."""
    # Aquesta funció no retorna res, només fa el càlcul i l'imprimeix
    resultat = a * b
    print(f"{a} x {b} = {resultat}")


def anys_2000():
    """Demana un any entre el 2000 i l'any actual i mostra quants anys han passat."""
    # Agafem l'any actual directament del sistema perquè no quedi fixat a mà
    any_actual = date.today().year
    any_introduit = 0
    valid = False

    # Repeteixo fins que l'usuari posi un any dins del rang [2000, any_actual]
    while not valid:
        any_introduit = demanar_enter(
            f"Introdueix un any entre 2000 i {any_actual}: ",
            f"L'any ha de ser un número entre 2000 i {any_actual}.",
        )
        if 2000 <= any_introduit <= any_actual:
            valid = True
        else:
            # El número és enter, però està fora de l'interval permès
            print(f"L'any ha de ser un número entre 2000 i {any_actual}.")

    anys_passats = any_introduit - 2000
    print(f"Des del 2000 han passat {anys_passats} anys")


def gira_reves():
    """Demana una cadena de text i la mostra girada del revés caràcter a caràcter."""
    cadena = input("Introdueix una cadena: ")
    girada = ""

    # Començo per l'últim caràcter i vaig retrocedint fins al primer
    index = len(cadena) - 1
    while index >= 0:
        # Només faig servir + i bucles, tal com demana l'enunciat
        girada = girada + cadena[index]
        index = index - 1

    print(girada)


def triangle_pascal():
    """Demana un nombre de files entre 2 i 10 i mostra el triangle de Pascal centrat."""
    n_files = 0
    rang_valid = False

    # Primer asseguro que el nombre de files estigui entre 2 i 10
    while not rang_valid:
        n_files = demanar_enter(
            "Nombre de files (entre 2 i 10): ",
            "Ha de ser un número entre 2 i 10.",
        )
        if 2 <= n_files <= 10:
            rang_valid = True
        else:
            print("Ha de ser un número entre 2 i 10.")

    # Vaig guardant cada fila en una llista per poder calcular la següent
    files = []
    fila_idx = 0
    while fila_idx < n_files:
        fila_actual = []
        col_idx = 0
        while col_idx <= fila_idx:
            # El primer i l'últim element de cada fila sempre són 1
            if col_idx == 0 or col_idx == fila_idx:
                fila_actual.append(1)
            else:
                # La resta d'elements són la suma dels dos que tenen a sobre
                fila_anterior = files[fila_idx - 1]
                suma = fila_anterior[col_idx - 1] + fila_anterior[col_idx]
                fila_actual.append(suma)
            col_idx = col_idx + 1

        files.append(fila_actual)
        fila_idx = fila_idx + 1

    # Calculo quants caràcters té l'última fila (la més llarga) per centrar el triangle
    ultima_fila_text = ""
    i = 0
    while i < len(files[-1]):
        if i > 0:
            ultima_fila_text = ultima_fila_text + " "
        ultima_fila_text = ultima_fila_text + str(files[-1][i])
        i = i + 1
    amplada_maxima = len(ultima_fila_text)

    # Recorro les files i afegeixo els espais necessaris a l'esquerra per centrar-les
    fila_idx = 0
    while fila_idx < len(files):
        text_fila = ""
        col_idx = 0
        while col_idx < len(files[fila_idx]):
            if col_idx > 0:
                text_fila = text_fila + " "
            text_fila = text_fila + str(files[fila_idx][col_idx])
            col_idx = col_idx + 1

        espais_esquerra = (amplada_maxima - len(text_fila)) // 2
        print(" " * espais_esquerra + text_fila)
        fila_idx = fila_idx + 1


def main():
    """Executa el bucle principal del menú fins que l'usuari selecciona sortir."""
    opcio = 0

    # El menú es va repetint mentre no es triï l'opció 5
    while opcio != 5:
        mostrar_menu()
        opcio = demanar_enter(
            "Escull una opció: ",
            "Opció incorrecta. Ha de ser un número de l'1 al 5.",
        )

        if opcio == 1:
            # Demano els dos números aquí fora i després els passo a multiplica()
            primer_num = demanar_enter("Primer número: ")
            segon_num = demanar_enter("Segon número: ")
            multiplica(primer_num, segon_num)
        elif opcio == 2:
            anys_2000()
        elif opcio == 3:
            gira_reves()
        elif opcio == 4:
            triangle_pascal()
        elif opcio == 5:
            print("Fins aviat!")
        else:
            # Si posa un enter que no està entre 1 i 5, l'aviso i torna el menú
            print("Opció incorrecta. Ha de ser un número de l'1 al 5.")


if __name__ == "__main__":
    main()