from random import randint


# Dibujar cuadro.
def display_board(board):
    print(
        f"""
+-------+-------+-------+
|       |       |       |
|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |
|       |       |       |
+-------+-------+-------+
        """)


# Llenar la matriz con números.
def fill_board(board):
    counter = 1
    for i in range(3):
        for j in range(3):
            board[i][j] = counter + j
        counter += 3


# Movimientos de la computadora.
def computer_move(board, occupied_rooms):
    print("Turno de la computadora...")
    computer_number = randint(1, 9)
    rl = room_location(computer_number)

    while occupied_rooms[rl[0]][rl[1]]:
        computer_number = randint(1, 9)
        rl = room_location(computer_number)

    # Jugada de la computadora.
    board[rl[0]][rl[1]] = "x"
    occupied_rooms[rl[0]][rl[1]] = True

    # Validar si se puede seguir jugando.
    continue_playing(board, occupied_rooms, "computer", "x")


def valid_number(number):
    while number > 9 or number < 1:
        number = int(input("Ingrese una ubicación valida: "))
    return number


# Movimientos del usuario.
def user_move(board, occupied_rooms):
    user_number = int(input("Ingrese el número del casillero seleccionado: "))

    rl = room_location(valid_number(user_number))

    while occupied_rooms[rl[0]][rl[1]]:
        user_number = int(input("El casillero seleccionado ya está ocupado. Elija otro: "))
        rl = room_location(valid_number(user_number))

    # Jugada del usuario.
    board[rl[0]][rl[1]] = "o"
    occupied_rooms[rl[0]][rl[1]] = True

    # Validar si se puede seguir jugando.
    continue_playing(board, occupied_rooms, "user", "o")


# Validar si se puede seguir jugando.
def continue_playing(board, occupied_rooms, player, icon):
    display_board(board)
    if is_there_a_winner(board, icon):
        print(f"Juego terminado. Tenemos un ganador. Ganador {player}")
        exit()

    if full_board(occupied_rooms):
        print("Juego terminado. Es un empate.")
        exit()

    if player == "user":
        computer_move(board, occupied_rooms)
    else:
        user_move(board, occupied_rooms)


# Validar si todo el tablero está lleno.
def full_board(board):
    i = 0
    for row in board:
        for item in row:
            if item:
                i += 1

    if i == 9:
        return True


# Valida si existe un ganador.
def is_there_a_winner(board, icon):
    if board[0][0] == icon and board[0][1] == icon and board[0][2] == icon:
        return True
    elif board[1][0] == icon and board[1][1] == icon and board[1][2] == icon:
        return True
    elif board[2][0] == icon and board[2][1] == icon and board[2][2] == icon:
        return True
    elif board[0][0] == icon and board[1][0] == icon and board[2][0] == icon:
        return True
    elif board[0][1] == icon and board[1][1] == icon and board[2][1] == icon:
        return True
    elif board[0][2] == icon and board[1][2] == icon and board[2][2] == icon:
        return True
    elif board[0][0] == icon and board[1][1] == icon and board[2][2] == icon:
        return True
    elif board[2][0] == icon and board[1][1] == icon and board[0][2] == icon:
        return True
    else:
        return False


# Retorna la fila y columna que representa al casillero seleccionado.
def room_location(number):
    if number == 1:
        return [0, 0]
    elif number == 2:
        return [0, 1]
    elif number == 3:
        return [0, 2]
    elif number == 4:
        return [1, 0]
    elif number == 5:
        return [1, 1]
    elif number == 6:
        return [1, 2]
    elif number == 7:
        return [2, 0]
    elif number == 8:
        return [2, 1]
    else:
        return [2, 2]


def main():
    # Matriz para el juego.
    board = [["" for x in range(3)] for y in range(3)]
    fill_board(board)

    # Casilleros ocupados.
    occupied_rooms = [[False for x in range(3)] for y in range(3)]

    # Primer jugada. La computadora.
    print("Turno de la computadora...")
    board[1][1] = "x"
    occupied_rooms[1][1] = True

    # Continuar el juego.
    continue_playing(board, occupied_rooms, "computer", "x")


main()
