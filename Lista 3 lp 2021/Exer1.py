import math
option = 's'
while option == 's' or 'S':
    a = int(input("Entre com o valor de a: "))
    b = int(input("Entre com o valor de b: "))
    c = int(input("Entre com o valor de c: "))

    delta = math.pow(-b,2)-4*a*c

    if delta < 0:
        print("Valor do delta negativo")
    else:
        x1 = (-b+math.sqrt(delta))/(2*a)
        x2 = (-b-math.sqrt(delta))/(2*a)
        print("x1=", x1, "x2=",x2)
    option = input("Deseja continuar?(S/N): ")        


