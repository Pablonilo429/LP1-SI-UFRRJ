import math
xa = int(input("Entre com o X do ponto 1: "))
xb = int(input("Entre com o X do ponto 2: "))
ya = int(input("Entre com o Y do ponto 1: "))
yb = int(input("Entre com o Y do ponto 2: "))
pontx= (xb-xa) * (xb-xa)
ponty= (yb-ya) * (yb-ya)
dab = pontx + ponty
dist = math.sqrt(dab)
print ("A distancia entre dois pontos e de:", dist)


