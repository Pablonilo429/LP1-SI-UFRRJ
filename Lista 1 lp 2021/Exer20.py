print("Entre com as suas notas:")
not1 = float(input())
not2 = float(input())
not3 = float(input())
not4 = float(input())
med = (not1+not2+not3+not4)/4
if med < 6:
    print("Aluno reprovado")
else:
    print("Aluno aprovado")
