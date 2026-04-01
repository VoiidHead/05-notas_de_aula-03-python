import math

#questão 1
print("Digite  três números reais para ver o menor dentre eles:")
cortisol = float(input(""))
fah = float(input(""))
dih = float(input(""))
Lilo = min(cortisol, fah, dih)
print("O menor número é:", Lilo)

print("------------------------------------------------------")


#questão 2
print("Digite três números reais para ver o maior dentre eles:")
macaco = float(input(""))
batata = float(input(""))
cebolafitra = float(input(""))
gulpy = max(macaco, batata, cebolafitra)
print("O maior número é:", gulpy)

print("------------------------------------------------------")

#questão 3
print("Digite um número real positivo para ver a raiz quadrada dele:")
obamahav = float(input(""))
dihdaratarata = math.sqrt(obamahav)

if obamahav <= 0:
    print("Número inválido. Por favor, digite um número real positivo.")
else:
    print("A raiz quadrada de", obamahav, "é:", dihdaratarata)

print("------------------------------------------------------")


#questão 4
print("Digite um número real para ver seu arredondamento para cima:")
leokennedy = float(input(""))
calcinha = math.ceil(leokennedy)
print("O número arredondado para cima é:", calcinha)

print("------------------------------------------------------")


#questão 5
print("Digite um número real para ver seu arredondamento para baixo:")
leonardo = float(input(""))
calçola = math.floor(leonardo)
print("O número arredondado para baixo é:", calçola)

print("------------------------------------------------------")


#questão 6
print("Digite cinco números reais para ver o maior e o menor entre eles:")
tabarato = float(input(""))
zigzag = float(input(""))
ziraldo = float(input(""))
zonildo = float(input(""))
xutarcomx = float(input(""))
tetano = max(tabarato, zigzag, ziraldo, zonildo, xutarcomx)
aids = min(tabarato, zigzag, ziraldo, zonildo, xutarcomx)
print("O maior número é:", tetano)
print("O menor número é:", aids)

print("------------------------------------------------------")


#questão 7
print("Digite uma área em m² para descobrir quantas caixas de cerâmica de 1.5m² cabem nela:")
area = float(input(""))
caixas = area / 1.5
if caixas - int(caixas) > 0.5:
    caixas = math.ceil(caixas)
elif caixas - int(caixas) < 0.5:
    caixas = math.floor(caixas)

print(f"Cabem {caixas} caixas de cerâmica de 1.5m² nessa área.")

print("------------------------------------------------------")


#questão 8
print("Digite um número real para ver horas e minutos baseado nele")

champchimp = float(input(""))
if champchimp < 0:
	champchimp = champchimp * -1
	print('Número convertido para positivo\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

chimpchompy = math.floor(champchimp)
changachimi = math.floor((champchimp - chimpchompy) * 60)
print(f'Horas: {chimpchompy} \nMinutos: {changachimi}')

print("------------------------------------------------------")


#questão 9
print("Digite valores de catetos de um triângulo retângulo para descobrir a hipotenusa:")
catota1 = float(input(""))
catota2 = float(input(""))
shangtsung = math.hypot(catota1, catota2)
print(f"A hipotenusa é: {shangtsung}")

print("------------------------------------------------------")


#questão 10
print("Digite um número real positivo para ver sua raiz quadrada, a raiz arredondada para cima e a raiz arredondada para baixo:")
nombro = float(input(""))

premium = math.sqrt(nombro)
pro = math.ceil(premium)
plus = math.floor(premium)

print(f"A raiz quadrada: {premium}")
print(f"Raiz arredondada para cima: {pro}")
print(f"Raiz arredondada para baixo: {plus}")
