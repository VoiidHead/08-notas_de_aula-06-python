#1 - Corrija o programa abaixo eliminando o erro de sintaxe:
# nome = input()
# if nome == "Paulo":
# print("Oi, Paulo")
# else:
#    print("Você não está registrado")

nome = input()
if nome == "Paulo":
   print("Oi, Paulo") ##faltava identação
else:
   print("Você não está registrado")


#2 - Modifique o programa abaixo evitando que ocorra um erro de execução quando o usuário informar um divisor com valor zero.
# dividendo = int(input('Digite o dividendo: '))
# divisor = int(input('Digite o divisor: '))
# quociente = dividendo / divisor
# print(f'Quociente: {quociente}')

dividendo = int(input('Digite o dividendo: '))
while True:
   divisor = int(input('Digite o divisor: '))
   
   if divisor != 0:
      break
   else:
      print('Inconsistência: NÃO É POSSÍVEL DIVIDIR POR 0')
      print('por favor, digite outro divisor')
      print(f'Dividendo: {dividendo}')

quociente = dividendo / divisor
print(f'Quociente: {quociente}')


#3 - Corrija o programa abaixo de forma que ele imprima a mensagem correta de acordo com a sua entrada. Comece identificando em que situações o programa apresenta erro.
# numero = int(input('Digite um inteiro: '))
# if numero < 5:
#    print('A entrada é maior do que cinco')
# else:
#    print('A entrada é menor ou igual a cinco')

##O sinal de menor que está no lugar do sinal de menor que, o que faz com que se eu digitar um número menor que 5, o output diga que a entrada é maior, e se eu digitar um número maior ou igual a 5, o output vai dizer que a entrada é menor ou igual a 5

numero = int(input('Digite um inteiro: '))
if numero > 5:
   print('A entrada é maior do que cinco')
else:
   print('A entrada é menor ou igual a cinco')


#4 - Corrija o programa abaixo de forma que ele imprima a mensagem correta de acordo com a sua entrada. Primeiro identifique em que situações o programa apresenta erro. Em seguida, use o depurador para descobrir o erro de código.
# # Programa que informa se a entrada é um múltiplo de 3 e/ou de 5
# n = int(input('Entrada: '))
# if n % 3 == 0:
#    print(f'{n} é múltiplo de 3')
# elif n % 5 == 0:
#    print(f'{n} é múltiplo de 5')
# elif n % 3 == 0 and n % 5 == 0:
#    print(f'{n} é múltiplo de 3 e de 5')
# else:
#    print(f'{n} não é múltiplo nem de 3 nem de 5')

##Se a primeira ou a segunda condição forem verdadeiras, a terceira, que é a junção delas, não será analisada pelo programa devido à ordem das condições. Sendo assim, a terceira condição deve estar no lugar da primeira e vice-versa

n = int(input('Entrada: '))
if n % 3 == 0 and n % 5 == 0:
   print(f'{n} é múltiplo de 3 e de 5')
elif n % 5 == 0:
   print(f'{n} é múltiplo de 5')
elif n % 3 == 0:
   print(f'{n} é múltiplo de 3')
else:
   print(f'{n} não é múltiplo nem de 3 nem de 5')


#5 - Corrija o programa abaixo de forma que ele imprima a mensagem correta de acordo com a sua entrada.
# turno = int(input('Entrada: '))
# if turno == 'V' and turno == 'v':
#    print('Vespertino')
# elif turno == 'M' and turno == 'm':
#    print('Matutino')
# else:
#    print('Valor inválido')

turno = input('Entrada: ') ##Conversão pra inteiro, pae??
if turno == 'V' or turno == 'v': ### 'and' alterado para 'or'
   print('Vespertino')
elif turno == 'M' or turno == 'm': ### 'and' alterado para 'or'
   print('Matutino')
else:
   print('Valor inválido')


#6 - Corrija o programa a seguir de forma que ele sirva como solução do problema apresentado. Problema: Escreva um programa que leia a idade de uma pessoa e classifique-a em uma das seguintes categorias: Criança (0 a 12 anos); Adolescente (13 a 17 anos); Adulto (18 a 59 anos); Idoso (60 anos ou mais).
# idade = int(input("Digite sua idade: "))
#  if idade <= 12:
#     print("Criança")
#  if idade <= 17:
#     print("Adolescente")
#  if idade <= 59:
#     print("Adulto")
#  else:
#     print("Idoso")

idade = int(input("Digite sua idade: "))
if idade <= 12:
   print("Criança")
elif idade <= 17: ### Elif ao invés de if
   print("Adolescente")
elif idade <= 59: ### Elif ao invés de if
   print("Adulto")
else:
   print("Idoso")

#*Problema: um funcionário recebe um salário bruto mensal; sobre esse valor, são aplicados os seguintes descontos: (1) INSS: 11% do salário bruto, (2) Imposto de Renda (IR) (2.a.) se o salário bruto for até R$ 2.000, isento, (2.b.) de R$ 2.000,01 até R$ 5.000, desconto de 15%, e (2.c.) acima de R$ 5.000, desconto de 27,5%; escreva um programa que leia o salário bruto e calcule o salário líquido, aplicando os descontos na ordem correta: primeiro o INSS, depois o IR sobre o valor restante.
#7 - Corrija o programa a seguir de forma que ele sirva como solução do problema do cálculo do salário líquido.
# salario_bruto = float(input("Digite o salário bruto: "))
#
# inss = salario_bruto * 0.11
# 
# if salario_bruto <= 2000:
#    ir = 0
# elif salario_bruto <= 5000:
#    ir = salario_bruto * 0.15
# else:
#    ir = salario_bruto * 0.275
# 
# salario_liquido = salario_bruto - inss - ir
# 
# print(f"Salário líquido: R$ {salario_liquido:.2f}")
#8 - Corrija o programa a seguir de forma que ele sirva como solução do problema do cálculo do salário líquido.
# salario_bruto = float(input("Digite o salário bruto: "))
#
# inss = salario_bruto * 0.11
# salario_pos_inss = salario_bruto - inss
# 
# if salario_bruto <= 2000:
#    ir = 0
# elif salario_bruto <= 5000:
#    ir = salario_pos_inss * 0.10
# else:
#    ir = salario_pos_inss * 0.20
# 
# salario_liquido = salario_pos_inss - ir
# 
# print(f"Salário líquido: R$ {salario_liquido:.2f}")

salario_bruto = float(input("Digite o salário bruto: "))

inss = salario_bruto * 0.11
salario_pos_inss = salario_bruto - inss ## A questão 7 esquece disso e faz o cálculo do IR em cima do salário bruto, e não em cima do salário com o valor do INSS descontado

if salario_bruto <= 2000:
   ir = 0
elif salario_bruto <= 5000:
   ir = salario_pos_inss * 0.15 ## A questão 8 usa 10%, ao invés de 15%
else:
   ir = salario_pos_inss * 0.275 ## A questão 8 usa 20%, ao invés de 27,5%

salario_liquido = salario_pos_inss - ir

print(f"Salário líquido: R$ {salario_liquido:.2f}")


#9 - Corrija o programa abaixo de forma que ele produza as saídas corretas.
# # Programa que calcula as raízes de uma equação do 2º grau
# import math
# a = float(input('Coeficiente de x ao quadrado: '))
# b = float(input('Coeficiente de x: '))
# c = float(input('Coeficiente livre: '))
# delta = b ** 2 - 4 * a * b
# 
# if delta < 0:
#    print('A equação não possui raízes reais.')
# elif delta == 0:
#    x = -b / 2 * a
#    print(f'Raíz: {x:.4f}')
# else:
#    x1 = -b + math.sqrt(delta) / 2 * a
#    x2 = -b - math.sqrt(delta) / 2 * a
#    print(f'Raiz 1: {x1:.4f}')
#    print(f'Raiz 2: {x1:.4f}')

import math
a = float(input('Coeficiente de x ao quadrado: '))
b = float(input('Coeficiente de x: '))
c = float(input('Coeficiente livre: '))
delta = b ** 2 - 4 * a * c ## Na versão errada, é calculado b ** 2 - 4 * a * b, que está errado

if delta < 0:
   print('A equação não possui raízes reais.')
elif delta == 0:
   x = -b / 2 * a
   print(f'Raíz: {x:.4f}')
else:
   x1 = (-b + math.sqrt(delta)) / 2 * a ## Na versão errada, não era calculada a expressão "-b + √Δ" para dividí-la por 2 * a. Era calculado "Δ : 2.a" e feita a soma entre isso e -b
   x2 = (-b - math.sqrt(delta)) / 2 * a ## Na versão errada, não era calculada a expressão "-b + √Δ" para dividí-la por 2 * a. Era calculado "Δ : 2.a" e calculada a diferença entre isso e -b
   print(f'Raiz 1: {x1:.4f}')
   print(f'Raiz 2: {x2:.4f}') ## Na versão errada, x1 se repete nessa segunda f-string
