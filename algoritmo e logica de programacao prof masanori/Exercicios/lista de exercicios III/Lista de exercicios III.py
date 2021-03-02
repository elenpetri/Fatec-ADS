# 1- Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue
# pedindo até que o usuário informe um valor válido.

n = float(input('Insira a nota de 0 a 10: '))
while n < 0 or n > 10:
    print(f'O valor inserido é inválido. Por favor digite um número de 0 a 10')
    n = float(input('Insira a nota de 0 a 10: '))

print('='*20)

#2-Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao
#nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
    username = str(input('Insira um nome de usuário: '))
    password = str(input('Insira uma senha: '))
    if username != password:
        print('Login criado com sucesso!')
        break
    print('O username não pode ser igual ao password!')

print('='*20)
#3-Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa
#anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de
# crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos
# necessários para que a população do país A ultrapasse ou iguale a população do país B,
# mantidas as taxas de crescimento
a = 80000
taxa_anual_cresc_a = 0.03
b = 200000
taxa_anual_cresc_b = 0.015
cont = 0
while a < b:
    a = taxa_anual_cresc_a * a + a
    cont = cont + 1
    b = taxa_anual_cresc_b * b + b
print('Serão necessários {} anos para que a população do país A iguale ou ultrapasse a população B.'.format(cont))

print('='*20)

#4. A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de
# formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a
# soma dos dois anteriores. Faça um algoritmo que leia um número inteiro calcule o seu número
# de Fibonacci. F1 = 1, F2 = 1, F3 = 2, etc.

n = int(input('Digite um número: '))
f1, f2 = 1, 1
f3 = 1
cont = 3
while cont <= n:
    f3 = f1 + f2
    f1 = f2
    f2 = f3
    cont += 1
print(f3)

#Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando
# o algoritmo de Euclides.

print('='*20)
n1 = (int(input('Digite o primeiro número inteiro: ')))
n2 = (int(input('Digite o segundo número inteiro: ')))
resto_divisão = n1 % n2
while resto_divisão != 0:
    n1 = n2
    n2 = resto_divisão
    resto_divisão = n1 % n2

print('O mdc dos números inseridos é {}'.format(n2))