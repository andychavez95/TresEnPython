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
def computer_move(board, shadown):
    computer_number = randint(1, 9)
    rl = room_location(computer_number)

    while shadown[rl[0]][rl[1]]:
        computer_number = randint(1, 9)
        rl = room_location(computer_number)

    # Jugada de la computadora.
    board[rl[0]][rl[1]] = "X"
    shadown[rl[0]][rl[1]] = True

    # Validar si se puede seguir jugando.
    continue_playing(board, shadown, "computer")


# Movimientos del usuario.
def user_move(board, shadown):
    user_number = int(input("Ingrese el número del casillero seleccionado: "))
    rl = room_location(user_number)

    while shadown[rl[0]][rl[1]]:
        user_number = int(input("El casillero seleccionado ya está ocupado. Elija otro: "))
        rl = room_location(user_number)

    # Jugada del usuario.
    board[rl[0]][rl[1]] = "O"
    shadown[rl[0]][rl[1]] = True

    # Validar si se puede seguir jugando.
    continue_playing(board, shadown, "user")


# Validar si se puede seguir jugando.
def continue_playing(board, shadown, player):
    if is_there_a_winner(shadown):
        print("Juego terminado. Tenemos un ganador.")
        display_board(board)
        exit()

    if player == "user":
        computer_move(board, shadown)
    else:
        user_move(board, shadown)


# Valida si existe un ganador.
def is_there_a_winner(shadown):
    if shadown[0][0] and shadown[0][1] and shadown[0][2]:
        return True
    elif shadown[1][0] and shadown[1][1] and shadown[1][2]:
        return True
    elif shadown[2][0] and shadown[2][1] and shadown[2][2]:
        return True
    elif shadown[0][0] and shadown[1][0] and shadown[2][0]:
        return True
    elif shadown[0][1] and shadown[1][1] and shadown[2][1]:
        return True
    elif shadown[0][2] and shadown[1][2] and shadown[2][2]:
        return True
    elif shadown[0][0] and shadown[1][1] and shadown[2][2]:
        return True
    elif shadown[2][0] and shadown[1][1] and shadown[0][2]:
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
    board[1][1] = "X"
    occupied_rooms[1][1] = True

    continue_playing(board, occupied_rooms, "computer")


main()
