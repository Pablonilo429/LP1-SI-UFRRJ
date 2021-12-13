print("Digite dois numeros: ") 
num1 = int(input())
num2 = int(input())
soma = num1 + num2
sub = num1 - num2
multi = num1 * num2
if num2 == 0:
    print("soma: ",soma)
    print("subtracao: ",sub)
    print("multiplicacao: ",multi)
    print("Nao foi possivel realizar a divisão")    
else:
    div = num1/num2
    print("soma: ",soma)
    print("subtracao: ",sub)
    print("multiplicacao: ",multi)
    print("divisao: ",div)    
