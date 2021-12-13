from typing import _SpecialForm


sal = float(input("Insira o valor do seu salario: "))
if sal <= 2000.00:
    salau = sal + ((sal*50)/100)    
if sal <= 5000.00 and sal > 2000:
    salau = sal + ((sal*40)/100)  
if sal <= 7000.00 and sal > 5000:
    salau = sal + ((sal*20)/100)
if sal > 7000 and sal < 7000:
    salau = sal + ((sal*10)/100)
print("Novo salario:",salau)