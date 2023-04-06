
#Exercício 1
s = 0

while True:
    v = int(input("Digite o numero que você quer somar ou 0 para sair: "))
    if v == 0:
        break
    s = s + v
print(s)
   #reescrevendo utilizando estrutura de repetição aninhada 

s = 0

while True:
    v = int(input("Digite o valor a ser somado ou 0 para sair: "))
    if v == 0:
        break
    if v != 0:
        s = s+v
print("A soma dos valores inseridos é: ", + s)

#-------------------------------------------------------------------
