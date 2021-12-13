import re
nome = input("Digite seu nome: ")
def verificadorcaracter(v):
     return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
                   lambda mo: mo.group(0).capitalize(),v)                 
print(verificadorcaracter(nome))                 

