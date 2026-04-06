# Notas de aula de 2026.1.08 - Python 06

## Informações gerais

- **Público alvo**: alunos da disciplina de **Introdução a lógica e programação** do curso de [Infoweb](https://diatinf.ifrn.edu.br/cursos/tecnico-em-informatica-para-internet/) na [DIATINF](https://diatinf.ifrn.edu.br/) no [CNAT-IFRN](https://portal.ifrn.edu.br/campus/natalcentral/)
- **Professor**: [L A Minora](https://github.com/leonardo-minora/)
- **Objetivo**:
  1. Apresentar definição de erro de sintaxe, semântica e de execução
  2. Mostrar a **depuração** como alternativa para corrigir erros de semântica e de execução

---
## Notas de aula [slides pdf](/06_Depuracao.pdf)
1. **Depuração** ou _debug_ é o processo sistemático para encontrar, analisar e corrigir erros (_bugs_) em um programa.
2. **Erro de sintaxe** ou **erro sintático** ocorre quando o programador escreve um código que viola as regras gramaticais e estruturais da linguagem de programação.
3. **Erro de semântica**, **erro semântico** ou **erro de programação** ocorre quando o código está escrito corretamente do ponto de vista gramatical (sem erros de sintaxe), mas a lógica aplicada não produz o resultado esperado.
4. **Erro de execução** (_runtime error_ ou _exception_) ocorre quando o programa já passou pela verificação de sintaxe e está executando normalmente, mas encontra uma instrução que é impossível de realizar no momento.


---
## Exercícios 
1. Corrija o programa abaixo eliminando o erro de sintaxe.

```python
nome = input()
if nome == "Paulo":
   print("Oi, Paulo")
else:
   print("Você não está registrado")
```

2. Modifique o programa abaixo evitando que ocorra um erro de execução quando o usuário informar um divisor com valor zero.

```python
dividendo = int(input('Digite o dividendo: '))
divisor = int(input('Digite o divisor: '))
quociente = dividendo / divisor
print(f'Quociente: {quociente}')

```

3. Corrija o programa abaixo de forma que ele imprima a mensagem correta de acordo com a sua entrada. Comece identificando em que situações o programa apresenta erro.

```python
numero = int(input('Digite um inteiro: '))
if numero < 5:
   print('A entrada é maior do que cinco')
else:
   print('A entrada é menor ou igual a cinco')

```

4. Corrija o programa abaixo de forma que ele imprima a mensagem correta de acordo com a sua entrada. Primeiro identifique em que situações o programa apresenta erro. Em seguida, use o depurador para descobrir o erro de código.

```python
# Programa que informa se a entrada é um múltiplo de 3 e/ou de 5
n = int(input('Entrada: '))
if n % 3 == 0:
   print(f'{n} é múltiplo de 3')
elif n % 5 == 0:
   print(f'{n} é múltiplo de 5')
elif n % 3 == 0 and n % 5 == 0:
   print(f'{n} é múltiplo de 3 e de 5')
else:
   print(f'{n} não é múltiplo nem de 3 nem de 5')

```

5. Corrija o programa abaixo de forma que ele imprima a mensagem correta de acordo com a sua entrada.

```python
turno = int(input('Entrada: '))
if turno == 'V' and turno == 'v':
   print('Vespertino')
elif turno == 'M' and turno == 'm':
   print('Matutino')
else:
   print('Valor inválido')

```

6. Corrija o programa a seguir de forma que ele sirva como solução do problema apresentado. **Problema**: Escreva um programa que leia a idade de uma pessoa e classifique-a em uma das seguintes categorias: Criança (0 a 12 anos); Adolescente (13 a 17 anos); Adulto (18 a 59 anos); Idoso (60 anos ou mais).

```python
idade = int(input("Digite sua idade: "))
if idade <= 12:
   print("Criança")
if idade <= 17:
   print("Adolescente")
if idade <= 59:
   print("Adulto")
else:
   print("Idoso")

```

7. Corrija o programa a seguir de forma que ele sirva como solução do problema do cálculo do salário líquido. **Problema** um funcionário recebe um salário bruto mensal; sobre esse valor, são aplicados os seguintes descontos: (1) INSS: 11% do salário bruto, (2) Imposto de Renda (IR) (2.a.) se o salário bruto for até R$ 2.000, isento, (2.b.) de R$ 2.000,01 até R$ 5.000, desconto de 15%, e (2.c.) acima de R$ 5.000, desconto de 27,5%; escreva um programa que leia o salário bruto e calcule o salário líquido, aplicando os descontos na ordem correta: primeiro o INSS, depois o IR sobre o valor restante.

| Salário Bruto | INSS | IR | Salário Líquido |
| ----- | ------ | -------- | -------- |
| 6.000 | 660,00 | 1.468,50 | 3.871,50 |
| 1.800 | 198,00 | 0,00     | 1.602,00 |
| 3.000 | 330,00 | 400,50   | 2.269,50 |

```python
salario_bruto = float(input("Digite o salário bruto: "))

inss = salario_bruto * 0.11

if salario_bruto <= 2000:
   ir = 0
elif salario_bruto <= 5000:
   ir = salario_bruto * 0.15
else:
   ir = salario_bruto * 0.275

salario_liquido = salario_bruto - inss - ir

print(f"Salário líquido: R$ {salario_liquido:.2f}")

```

8. Corrija o programa a seguir de forma que ele sirva como solução do problema do cálculo do salário líquido da questão anterior.

```python
salario_bruto = float(input("Digite o salário bruto: "))

inss = salario_bruto * 0.11
salario_pos_inss = salario_bruto - inss

if salario_bruto <= 2000:
   ir = 0
elif salario_bruto <= 5000:
   ir = salario_pos_inss * 0.10
else:
   ir = salario_pos_inss * 0.20

salario_liquido = salario_pos_inss - ir

print(f"Salário líquido: R$ {salario_liquido:.2f}")

```

9. Corrija o programa abaixo de forma que ele produza as saídas corretas.

```python
# Programa que calcula as raízes de uma equação do 2º grau
import math
a = float(input('Coeficiente de x ao quadrado: '))
b = float(input('Coeficiente de x: '))
c = float(input('Coeficiente livre: '))
delta = b ** 2 - 4 * a * b

if delta < 0:
   print('A equação não possui raízes reais.')
elif delta == 0:
   x = -b / 2 * a
   print(f'Raíz: {x:.4f}')
else:
   x1 = -b + math.sqrt(delta) / 2 * a
   x2 = -b - math.sqrt(delta) / 2 * a
   print(f'Raiz 1: {x1:.4f}')
   print(f'Raiz 2: {x1:.4f}')

```
