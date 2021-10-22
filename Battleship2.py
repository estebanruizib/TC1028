#%%
fo = open('battleship.txt','r')
board = []
battleship = fo.read()
fo.close()
lista_battle = battleship.split()
print(lista_battle)
#%%
fo = open("battleship.txt", "r")
board = []

while True :
    linea = fo.readline()
    if (not linea):
        break
    linea = linea.strip('\n')
    lista = linea.split(' ')
    board.append(lista)

fo.close()
#%%
fo = open('control.txt','r')
battleship = fo.read()
fo.close()
lista_battle = battleship.split()
print(lista_battle)
#%%
import random

board = []

for i in range(0,7):
  board.append(["0"] * 7)

def printboard(board):
  for fila in board:
    print (" ".join(fila))

print("Vamos a jugar al barolshi")
print("Somos Esteban y Javi, buenas tardes")

jugador1 = input("Pon el nombre del primer jugador: ")
jugador2 = input("Pon el nombre del segundo jugador: ")
jugadores = [jugador1, jugador2]

def jugadoral(jugadores):
    return random.choice(jugadores)

def filaal(board):
  return random.randint(0,len(board)-1)

def randomcol(board):
  return random.randint(0,len(board[0])-1)

if jugadoral(jugadores) == jugador1:
  print(jugador1, "empieza.")
else:
  print(jugador2, "empieza.")
  
navefila1 = filaal(board)
navecol1 = randomcol(board)

navefila2 = filaal(board)
navecol2 = randomcol(board)

navefila3 = filaal(board)
navecol3 = randomcol(board)

navefila4 = filaal(board)
navecol4 = randomcol(board)

printboard(board)

jugemp = jugadoral(jugadores)

hit_count = 0

for turn in range(4):
     adivinafila = int(input("Adivina la fila con valores entre (0-6): "))
     adivinacol = int(input("Adivina la columna con valores entre (0-6) "))

     if (adivinafila == navefila1 and adivinacol == navecol1) or (adivinafila == navefila2 and adivinacol == navecol2) or (adivinafila == navefila3 and adivinacol == navecol3) or (adivinafila == navefila4 and adivinacol == navecol4):
            hit_count = hit_count + 1
            board[adivinafila][adivinacol] = "%"
            print ("Felicidades brou! ")
            if hit_count == 1:
                   print("Le diste a la navee!") 
            elif hit_count == 2:
                   print("Le diste a 2 naves! Ganastee!")
                   printboard(board)
                   break
     else:
            if (adivinafila < 0 or adivinafila > 6)  or (adivinacol < 0 or adivinacol > 6):
                   print ("Ni de cerca cabezon.")
            elif(board[adivinafila][adivinacol] == "X"):
                   print ("Ya le diste a esa. ")
            else:
                 print ("No le diste a mi nave jaja q menso!")
                 board[adivinafila][adivinacol] = "X"
            print ("llevas", turn + 1, "turno(s)")
     printboard(board)
print ("La nave 1 estaba en:")    
print (navefila1)
print (navecol1)

print ("La nave 2 estaba en:")    
print (navefila2)
print (navecol2)

print ("La nave 3 estaba en:")    
print (navefila3)
print (navecol3)

print ("La nave 4 estaba en:")    
print (navefila4)
print (navecol4)
3
# %%
