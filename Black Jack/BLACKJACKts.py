
import random

# ==================================================
# FUNCION PARA DIBUJAR UNA CARTA
# ==================================================

def dibujar_carta(valor, palo):

    print("┌─────────┐")
    print(f"│ {valor:<2}      │")
    print("│         │")
    print(f"│    {palo}    │")
    print("│         │")
    print(f"│      {valor:>2} │")
    print("└─────────┘")


# ==================================================
# FUNCION PARA DIBUJAR UNA CARTA OCULTA
# ==================================================

def dibujar_carta_oculta():

    print("┌─────────┐")
    print("│░░░░░░░░░│")
    print("│░░░░░░░░░│")
    print("│░░░░░░░░░│")
    print("│░░░░░░░░░│")
    print("│░░░░░░░░░│")
    print("└─────────┘")


# ==================================================
# FUNCION PARA MOSTRAR LAS CARTAS
# ==================================================

def mostrar_cartas(jugador, banca, ocultar_segunda=True):

    print("\n" + "=" * 40)

    print("\nCartas del jugador:\n")

    for valor, palo in jugador:

        dibujar_carta(valor, palo)

    print("\nCartas de la banca:\n")

    for i, (valor, palo) in enumerate(banca):

        if ocultar_segunda and i == 1:

            dibujar_carta_oculta()

        else:

            dibujar_carta(valor, palo)

    print("=" * 40)


# ==================================================
# FUNCION PARA CALCULAR PUNTOS
# ==================================================

def calcular_puntos(mano):

    puntos = 0
    ases = 0

    for valor, palo in mano:

        if valor == "A":

            puntos += 11
            ases += 1

        elif valor in ("J", "Q", "K"):

            puntos += 10

        else:

            puntos += int(valor)

    # Convertir ases de 11 a 1 cuando sea necesario.
    while puntos > 21 and ases > 0:

        puntos -= 10
        ases -= 1

    return puntos


# ==================================================
# FUNCION PARA REPARTIR UNA CARTA
# ==================================================

def pedir_carta(baraja, mano):

    carta = baraja.pop()

    mano.append(carta)


# ==================================================
# FUNCION PARA VALIDAR LA APUESTA
# ==================================================

def validar_apuesta(saldo):

    while True:

        entrada = input(
            "\n¿Cuánto quieres apostar?: "
        ).strip()

        try:

            apuesta = int(entrada)

        except ValueError:

            print(
                "\nValor inválido: debes ingresar un número "
                "entero positivo."
            )

            print(
                "Ejemplos válidos: 50, 100, 250."
            )

            print(
                "No puedes ingresar letras, decimales "
                "ni dejar la entrada vacía."
            )

            continue

        if apuesta <= 0:

            print(
                "\nValor inválido: la apuesta debe ser "
                "mayor que cero."
            )

            print(
                "Ingresa una cantidad como 50, 100 o 200."
            )

            continue

        if apuesta > saldo:

            print(
                f"\nValor inválido: intentaste apostar "
                f"${apuesta}, pero solamente tienes "
                f"${saldo}."
            )

            print(
                "Debes ingresar una apuesta que no "
                "supere tu saldo."
            )

            continue

        return apuesta


# ==================================================
# FUNCION PARA VALIDAR LA RESPUESTA
# ==================================================

def validar_respuesta(mensaje):

    while True:

        respuesta = input(mensaje).strip().lower()

        if respuesta == "s":

            return "s"

        elif respuesta == "n":

            return "n"

        else:

            print(
                "\nValor inválido: solamente puedes "
                "ingresar 's' o 'n'."
            )

            print(
                "'s' significa sí y 'n' significa no."
            )


# ==================================================
# JUEGO PRINCIPAL
# ==================================================

valores = [
    "A", "2", "3", "4", "5", "6", "7",
    "8", "9", "10", "J", "Q", "K"
]

palos = ["♥", "♦", "♣", "♠"]

saldo = 1000


print("=" * 40)
print("          BLACKJACK")
print("=" * 40)

print("\nTu saldo inicial es:", saldo)


# ==================================================
# CICLO PRINCIPAL DEL JUEGO
# ==================================================

while saldo > 0:

    # ----------------------------------------------
    # CREAR BARAJA
    # ----------------------------------------------

    baraja = [
        [valor, palo]
        for palo in palos
        for valor in valores
    ]

    random.shuffle(baraja)

    jugador = []
    banca = []

    # ----------------------------------------------
    # VALIDAR APUESTA
    # ----------------------------------------------

    apuesta = validar_apuesta(saldo)

    saldo -= apuesta

    print("\nApuesta realizada:", apuesta)

    print("Saldo restante:", saldo)

    # ----------------------------------------------
    # REPARTIR CARTAS
    # ----------------------------------------------

    pedir_carta(baraja, jugador)

    pedir_carta(baraja, banca)

    pedir_carta(baraja, jugador)

    pedir_carta(baraja, banca)

    # ----------------------------------------------
    # MOSTRAR CARTAS INICIALES
    # ----------------------------------------------

    mostrar_cartas(
        jugador,
        banca,
        ocultar_segunda=True
    )

    # ----------------------------------------------
    # TURNO DEL JUGADOR
    # ----------------------------------------------

    while True:

        puntos_jugador = calcular_puntos(jugador)

        print(
            "\nPuntos del jugador:",
            puntos_jugador
        )

        # Comprobar si supera 21.
        if puntos_jugador > 21:

            print(
                "\nPerdiste: tu puntuación supera "
                "los 21 puntos."
            )

            break

        # Comprobar si llega a 21.
        if puntos_jugador == 21:

            print(
                "\nLlegaste a 21 puntos."
            )

            break

        # Preguntar si quiere otra carta.
        respuesta = validar_respuesta(
            "\n¿Quieres pedir otra carta? [s/n]: "
        )

        if respuesta == "s":

            pedir_carta(
                baraja,
                jugador
            )

            mostrar_cartas(
                jugador,
                banca,
                ocultar_segunda=True
            )

        else:

            print(
                "\nDecidiste plantarte."
            )

            break

    # ----------------------------------------------
    # TURNO DE LA BANCA
    # ----------------------------------------------

    puntos_jugador = calcular_puntos(jugador)

    if puntos_jugador <= 21:

        print(
            "\nTurno de la IA..."
        )

        while calcular_puntos(banca) < 17:

            pedir_carta(
                baraja,
                banca
            )

            print(
                "\nLa IA pidió otra carta."
            )

    # ----------------------------------------------
    # MOSTRAR CARTAS FINALES
    # ----------------------------------------------

    mostrar_cartas(
        jugador,
        banca,
        ocultar_segunda=False
    )

    # ----------------------------------------------
    # CALCULAR PUNTUACIONES
    # ----------------------------------------------

    puntos_jugador = calcular_puntos(
        jugador
    )

    puntos_banca = calcular_puntos(
        banca
    )

    print(
        "\nPuntos del jugador:",
        puntos_jugador
    )

    print(
        "Puntos de la IA:",
        puntos_banca
    )

    # ----------------------------------------------
    # DETERMINAR GANADOR
    # ----------------------------------------------

    if puntos_jugador > 21:

        print(
            "\nPERDISTE: te pasaste de 21."
        )

    elif puntos_banca > 21:

        print(
            "\n¡GANASTE! La IA se pasó de 21."
        )

        saldo += apuesta * 2

    elif puntos_jugador > puntos_banca:

        print(
            "\n¡GANASTE! Tienes más puntos que la IA."
        )

        saldo += apuesta * 2

    elif puntos_jugador < puntos_banca:

        print(
            "\nPERDISTE: la IA tiene más puntos."
        )

    else:

        print(
            "\nEMPATE: recuperaste tu apuesta."
        )

        saldo += apuesta

    # ----------------------------------------------
    # MOSTRAR SALDO
    # ----------------------------------------------

    print(
        "\nSaldo actual:",
        saldo
    )

    # ----------------------------------------------
    # COMPROBAR SI TIENE DINERO
    # ----------------------------------------------

    if saldo <= 0:

        print(
            "\nTe quedaste sin dinero."
        )

        break

    # ----------------------------------------------
    # PREGUNTAR SI QUIERE CONTINUAR
    # ----------------------------------------------

    respuesta = validar_respuesta(
        "\n¿Quieres volver a jugar? [s/n]: "
    )

    if respuesta == "n":

        break


# ==================================================
# FINAL DEL JUEGO
# ==================================================

print("\n" + "=" * 40)

print("Gracias por jugar Blackjack.")

print("Saldo final:", saldo)

print("=" * 40)
