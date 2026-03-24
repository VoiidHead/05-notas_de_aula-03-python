# Lista de Exercícios – Python 03

## Informações gerais
**Disciplina**: Introdução à Lógica e Programação  
**Tópicos**:
- funções matemáticas `min`, `max`, `sart`, `ceil`, `floor`

---

## Exercício 1 — Menor entre três números (`min()`)

Escreva um programa que leia três números reais digitados pelo usuário e imprima o menor deles.

**Código:**
```python
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))

menor = min(a, b, c)
print("O menor número é:", menor)
```

**Exemplo de entrada e saída:**
```
Digite o primeiro número: 7.5
Digite o segundo número: 3.2
Digite o terceiro número: 9.0
O menor número é: 3.2
```

---

## Exercício 2 — Maior entre três números (`max()`)

Escreva um programa que leia três números reais digitados pelo usuário e imprima o maior deles.

**Código:**
```python
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))

maior = max(a, b, c)
print("O maior número é:", maior)
```

**Exemplo de entrada e saída:**
```
Digite o primeiro número: 7.5
Digite o segundo número: 3.2
Digite o terceiro número: 9.0
O maior número é: 9.0
```

---

## Exercício 3 — Raiz quadrada de um número (`math.sqrt()`)

Escreva um programa que leia um número real positivo digitado pelo usuário e imprima a sua raiz quadrada.

**Código:**
```python
import math

numero = float(input("Digite um número positivo: "))
raiz = math.sqrt(numero)
print("A raiz quadrada de", numero, "é:", raiz)
```

**Exemplo de entrada e saída:**
```
Digite um número positivo: 25
A raiz quadrada de 25.0 é: 5.0
```

---

## Exercício 4 — Arredondamento para cima (`math.ceil()`)

Escreva um programa que leia um número real digitado pelo usuário e imprima o menor número inteiro maior ou igual a ele (arredondamento para cima).

**Código:**
```python
import math

numero = float(input("Digite um número real: "))
teto = math.ceil(numero)
print("O arredondamento para cima de", numero, "é:", teto)
```

**Exemplo de entrada e saída:**
```
Digite um número real: 4.3
O arredondamento para cima de 4.3 é: 5
```

---

## Exercício 5 — Arredondamento para baixo (`math.floor()`)

Escreva um programa que leia um número real digitado pelo usuário e imprima o maior número inteiro menor ou igual a ele (arredondamento para baixo).

**Código:**
```python
import math

numero = float(input("Digite um número real: "))
piso = math.floor(numero)
print("O arredondamento para baixo de", numero, "é:", piso)
```

**Exemplo de entrada e saída:**
```
Digite um número real: 4.7
O arredondamento para baixo de 4.7 é: 4
```

---

## Exercício 6 — Menor e maior entre cinco números (`min()` e `max()`)

Escreva um programa que leia cinco números inteiros digitados pelo usuário e imprima o menor e o maior deles.

**Código:**
```python
a = int(input("Digite o 1º número: "))
b = int(input("Digite o 2º número: "))
c = int(input("Digite o 3º número: "))
d = int(input("Digite o 4º número: "))
e = int(input("Digite o 5º número: "))

menor = min(a, b, c, d, e)
maior = max(a, b, c, d, e)

print("O menor número é:", menor)
print("O maior número é:", maior)
```

**Exemplo de entrada e saída:**
```
Digite o 1º número: 10
Digite o 2º número: 3
Digite o 3º número: 7
Digite o 4º número: 15
Digite o 5º número: 1
O menor número é: 1
O maior número é: 15
```

---

## Exercício 7 — Quantidade de caixas de cerâmica (`math.ceil()`)

Uma caixa de cerâmica cobre 1,5 m². Escreva um programa que leia a área em metros quadrados que o usuário deseja revestir e informe a quantidade mínima de caixas necessárias.

**Código:**
```python
import math

area = float(input("Digite a área em metros quadrados: "))
caixas = math.ceil(area / 1.5)
print("Quantidade de caixas necessárias:", caixas)
```

**Exemplo de entrada e saída:**
```
Digite a área em metros quadrados: 10
Quantidade de caixas necessárias: 7
```

---

## Exercício 8 — Tempo em horas e minutos (`math.floor()`)

Escreva um programa que leia uma quantidade de tempo em horas (número real) e imprima o tempo separado em horas inteiras e minutos.

**Código:**
```python
import math

tempo = float(input("Digite o tempo em horas: "))
horas = math.floor(tempo)
minutos = math.floor((tempo - horas) * 60)
print("Tempo:", horas, "hora(s) e", minutos, "minuto(s)")
```

**Exemplo de entrada e saída:**
```
Digite o tempo em horas: 2.5
Tempo: 2 hora(s) e 30 minuto(s)
```

---

## Exercício 9 — Hipotenusa de um triângulo retângulo (`math.sqrt()`)

Dado um triângulo retângulo, a hipotenusa pode ser calculada pela fórmula: `h = sqrt(a² + b²)`. Escreva um programa que leia os dois catetos e calcule e imprima a hipotenusa.

**Código:**
```python
import math

a = float(input("Digite o valor do cateto a: "))
b = float(input("Digite o valor do cateto b: "))
hipotenusa = math.sqrt(a**2 + b**2)
print("A hipotenusa é:", hipotenusa)
```

**Exemplo de entrada e saída:**
```
Digite o valor do cateto a: 3
Digite o valor do cateto b: 4
A hipotenusa é: 5.0
```

---

## Exercício 10 — Comparando raiz quadrada com arredondamentos (`math.sqrt()`, `math.ceil()`, `math.floor()`)

Escreva um programa que leia um número real positivo, calcule sua raiz quadrada e exiba: o valor exato da raiz, o arredondamento para baixo e o arredondamento para cima.

**Código:**
```python
import math

numero = float(input("Digite um número positivo: "))
raiz = math.sqrt(numero)
piso = math.floor(raiz)
teto = math.ceil(raiz)

print("Raiz quadrada de", numero, ":", raiz)
print("Arredondamento para baixo:", piso)
print("Arredondamento para cima:", teto)
```

**Exemplo de entrada e saída:**
```
Digite um número positivo: 10
Raiz quadrada de 10.0 : 3.1622776601683795
Arredondamento para baixo: 3
Arredondamento para cima: 4
```
