# Notas de aula de 2026.1.05 - Python 03

## Informações gerais

- **Público alvo**: alunos da disciplina de **Introdução a lógica e programação** do curso de [Infoweb (Técnico Integrado em Informática para Internet)](https://diatinf.ifrn.edu.br/cursos/tecnico-em-informatica-para-internet/) na [DIATINF (Diretoria Acadêmica de Gestão e Tecnologia da Informação)](https://diatinf.ifrn.edu.br/) no [CNAT-IFRN (Instituto Federal de Educação, Ciência e Tecnologia do Rio Grande do Norte - Campus Natal-Central)](https://portal.ifrn.edu.br/campus/natalcentral/)
- **Professor**: [L A Minora](https://github.com/leonardo-minora/)
- **Objetivo**:
  1. Conhecer algumas das funções matemáticas do python

---
## Notas de aula [slides pdf](/03-Funções_matemáticas.pdf)
1. definições de:
   - **função** é um bloco de código reutilizável que executa uma tarefa específica sempre que é chamado pelo seu nome.
   - **biblioteca de funções** é uma coleção de funções prontas que você pode importar para o seu programa para resolver tarefas comuns sem precisar escrever todo o código do zero. Bibliotecas de funções comuns em python [datetime](https://docs.python.org/pt-br/3.14/library/datetime.html), [math](https://docs.python.org/pt-br/3.14/library/math.html), [random](https://docs.python.org/pt-br/3.14/library/random.html) e [statistics](https://docs.python.org/pt-br/3.14/library/statistics.html).
2. Anatomia de uma função - nome, argumentos ou parâmetros, retorno ou valor de retorno
   - input("bem vindo") -> nome `input`; argumento `"bem vindo"`; e valor de retorno será o texto digitado
3. Algumas funções matemáticas
   - `min()` -> menor valor, exemplo `min(3, 10, 1, 5, 6)` com resultado de `1`.
   - `max()` -> maior valor, exemplo `max(3, 10, 1, 5, 6)` com resultado de `10`.
   - `math.sqrt()` -> raiz quadrada de um número, exemplo `math.sqrt(100)` com resultado de `10`.
   - `math.ceil()` -> dado um valor real, retorna o próximo número inteiro, exemplo `ceil(6.2)` com resultado de `7`.
   - `math.floor()` -> dado um valor real, retorna o próximo número inteiro, exemplo `floor(6.2)` com resultado de `6`.

---
## Exercícios
[Respostas dos Exercícios do PDF](/asma.py)
1. Escreva um programa que tem como entrada 3 números reais e imprime o menor destes números.
2. Escreva um programa que tem como entrada um número real positivo e maior do que zero e que calcula e imprime: (a) o quadrado do número; (b) a raiz quadrada do número; (c) a raiz cúbica do número.
3. Escreva um programa que tem como entrada cinco números inteiros, ignora o menor número e o maior número, e que calcula a média aritmética dos três número restantes.
4. Escreva um programa que tem como entrada um número real representando uma quantidade de tempo em horas e que imprime o tempo em horas e minutos.
5. Escreva um programa que tem como entrada um valor de área em metros quadrados e que informa a quantidade de caixas de cerâmica necessárias para revestir a área informada, sabendo que uma caixa contém 1,5 m2 de cerâmica.

[Lista de exercícios](/lista.md)

[Respostas da lista de exercícios:](https://github.com/VoiidHead/05-notas_de_aula-03-python/blob/main/Lista%20de%20Exerc%C3%ADcios/taste.py)
