player1 = input('Jugador 1: ')
player2 = input('Jugador 2: ')

game = True

gaps = 0

board = (" " * 9)# tablero con 9 casillas

def placeToken(token): # coloca la ficha en el tablero
    print('Dime la posicion de la ficha')
    while True:
        row = int(input('Fila: '))
        column = int(input('Columna: '))
        box = row*3+column # porque mi tablero es 3*3
        if board[box] != " ":
            print("La casilla esta cubierta")   
        else:
            board[box] = token
            return
    

while game:   
    placeToken("X" if (gaps&1) else "O")
    gaps += 1

    if gaps == 9: # termina el juego si estan todos los huecos cubiertos
        game = False

    # board()

    # checkWin()

    # changePlayer()

