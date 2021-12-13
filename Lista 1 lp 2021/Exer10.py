print("Entre com dois numeros:")
num1 = int(input())
num2 = int(input())
if num1 > num2:
    maior = num1
    menor = num2
else:
    maior = num2
    menor = num1

soma = maior + menor
sub = maior - menor
multi = maior * menor
if menor == 0:
    print("soma: ",soma)
    print("subtracao: ",sub)
    print("multiplicacao: ",multi)
    print("Nao foi possivel realizar a divisão")    
else:
    div = maior/menor
    print("soma: ",soma)
    print("subtracao: ",sub)
    print("multiplicacao: ",multi)
    print("divisao: ",div)    
