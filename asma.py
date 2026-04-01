import math

#1
print("Digite três números para ver o menor entre eles.")

ajedrez = input()
yak = input()
Eifer = input()

nul = min(ajedrez, yak, Eifer)

print(f"Menor: {nul}")

#2
print("Digite um número positivo para ver a raiz quadrada dele")
laiala = int(input())

if laiala <= 0:
	laiala = 1
	print("Número inválido, substituído por 1")


Alice = math.sqrt(laiala)
print(f'Raiz Quadrada: {Alice}')

#3
print("Digite cinco números inteiros para ver a média aritmética entre os que não forem o maior ou o menor dentre eles.")
lirililarila = int(input())
bonekaambalabu = int(input())
tralalerotralala = int(input())
ballerinacapuccina = int(input())
capuccinobabuino = int(input())

nimbus = [lirililarila, bonekaambalabu, tralalerotralala, ballerinacapuccina, capuccinobabuino]
nimbus.sort()

nimbus = nimbus[1:4]

limonada = sum(nimbus) / len(nimbus)

print(f"Média Aritmética: {limonada}")


#4
print("Digite um número real para ver horas e minutos baseado nele")

chimpchamp = float(input(""))
if chimpchamp < 0:
	chimpchamp = chimpchamp * -1
	print('Número convertido para positivo\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

chompychimp = math.floor(chimpchamp)
chimichanga = math.floor((chimpchamp - chompychimp) * 60)
print(f'Horas: {chompychimp} \nMinutos: {chimichanga}')

#5
print("Digite um valor de área em m² para saber qual o máximo de caixas de 1,5m² que podem ser postas na área")
comunismo = float(input(""))
if comunismo < 0:
	comunismo = comunismo * -1
	print('Área convertida para número positivo\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

holodomor = comunismo / 1.5
pessoas_com_fome = math.ceil(holodomor)
if holodomor - int(holodomor) < 0.5:
	pessoas_com_fome = math.floor(holodomor)

print(f"Numa área de {comunismo}m², o máximo de caixas de 1,5m² que podem ser postas na área é de {pessoas_com_fome}.")
