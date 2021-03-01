#Lista de Exercícios II
#1- Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser um
# triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print('ESCALENO!')
    else:
        print('ISÓCELES')
else:
    print('Os segmentos acima NÂO PODEM FORMAR triângulo')

print('-='*20) #Apenas para separar os exercícios
#2- Determine se um ano é bissexto.

year = int(input('Que ano você quer analisar? '))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print('O ano {} é BISSEXTO'.format(year))
else:
    print('O ano {} NÃO é BISSEXTO'.format(year))

print('-='*20)
#3- João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca doestado de São Paulo
# (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a
# variável peso (peso de peixes) e verifique se há excesso. Se houver, gravar na variável excesso e na variável multa o
# valor da multa que João deverá pagar. Caso contrário mostrar tais variáveis com o conteúdo ZERO.

peso = float(input('Qual o peso da pesca? '))
excesso = 0
multa = 0
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
print(f'O execesso foi de {excesso}Kg e a multa a ser paga é de R$ {multa:.2f}')

print('-='*20)
#4- Faça um Programa que leia três números e mostre o maior deles.

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

if n1 >= n2 and n1 >= n3:
    print(f'O maior número é {n1}')
elif n2 >= n1 and n2 >= n3:
    print(f'O maior número é {n2}')
else:
    print(f'O maior número é {n3}')

print('-='*20)
#4- Faça um Programa que leia três números e mostre o maior e menor deles.

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

if n1 >= n2 and n1 >= n3:
    maior = n1
elif n2 >= n1 and n2 >= n3:
    maior = n2
else:
    maior = n3
if n1 <= n2 and n1 <= n3:
    menor = n1
elif n2 <= n1 and n2 <= n3:
    menor = n2
else:
    menor = n3
print('O maior número é {} e o menor número é {}'.format(maior, menor))

print('-='*20)
#5- Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre
# o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,8% para o INSS e
# 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS, quanto pagou ao sindicato e
# o salário líquido. Observe que Salário Bruto-Descontos = Salário Líquido. Calcule os descontos e o salário líquido

salário_hora = float(input('Quanto você ganha por hora? '))
horas_trabalho_mês = float(input('Quantas horas você trabalhou no mês? '))
salário_bruto = salário_hora * horas_trabalho_mês
ir = salário_bruto * 0.11
inss = salário_bruto * 0.08
sindicato = salário_bruto * 0.05
salário_liq = salário_bruto - ir -inss - sindicato
print('+ Salário Bruto: R${:.2f} \n- IR (11%): R${:.2f} \n- INSS (8%): R${:.2f} \n- Sindicato (5%) R${:.2f} \n='
      ' Salário Líquido: R${:.2f}'.format(salário_bruto, ir, inss, sindicato, salário_liq))

print('-='*20)
#6- Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
# pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em
# latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o
# preço total. Obs.: somente são vendidos um número inteiro de latas.

área = int(input('Insira a metragem a ser pintada: '))
if área % 54 == 0:
    latas = área / 54
else:
    latas = área // 54 + 1
print('Você deverá comprar {} lata(s) e o preço a ser pago é R${:.2f}'.format(latas, 80*latas))