
#1) Faça um programa que peça dois números inteiros e imprima a soma desses dois números

n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
soma = n1 + n2
print('A soma entre', n1, '+', n2, 'é', soma)

#--------------------------------------------------------------------------------------------------------------

#2) Escreva um programa que leia um valor em metros e o exiba convertido em milímetros

m = float(input('Digite uma metragem: '))
mm = m * 1000
print('A metragem convertida para mimlímetros é: {}'.format(mm))

#--------------------------------------------------------------------------------------------------------------

#3) Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.

d = int(input('Digite a quantidade de dias: '))
h = int(input('Digite a hora: '))
m = int(input('Digite os minutos: '))
s = int(input('Digite os segundos: '))
demseg = d * 86400
hemseg = h * 3600
memseg = m * 60
print('O resultado total em segundos é: {} '.format(demseg + hemseg + memseg + s))

#--------------------------------------------------------------------------------------------------------------

#4) Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário

sal = float(input('Digite o salário inicial: '))
acresc = float(input('Digite a porcentagem do aumento: '))
valor_acresc = (sal * acresc / 100)
novosal = sal + valor_acresc
print(f'O valor do acréscimo é de R${valor_acresc:.2f} e o valor do novo salário é R${novosal:.2f}')

#--------------------------------------------------------------------------------------------------------------

#5) Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.

preço = float(input('Insira o valor da mercadoria: '))
per = float(input('Insira o precentual de desconto: '))
desc = preço * per / 100
preço_final = preço - desc
print(f'O valor do desconto é R${desc:.2f} e o valor final à pagar é R${preço_final:.2f}')

#--------------------------------------------------------------------------------------------------------------

#6) Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

km = float(input('Insira a distância a percorrer: '))
vel_media = float(input('Insira a velocidade média: '))
h = km / vel_media
print('O tempo da viagem de carro será de {} horas'.format(h))

#--------------------------------------------------------------------------------------------------------------

#7) Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32

c = float(input('Insira a temperatura em ºC: '))
f = 9 * c / 5 + 32
print('A temperatura em Celsius digitada convertida para Fahrenheit é: {}'.format(f))

#--------------------------------------------------------------------------------------------------------------

#8) Faça agora o contrário, de Fahrenheit para Celsius.

f = float(input('Insira a temperatura em F: '))
c = (5 * f - 160) / 9
print('A temperatura em Fahrenheit digitada convertida para Celsius é: {}'.format(c))

#--------------------------------------------------------------------------------------------------------------

#9) Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

km = float(input('Insira a quantidade de km percorrido pelo veículo: '))
aluguel_dia = int(input('Insira a quantidade de dias de aluguel do veículo: '))
valor_km_dia = 0.15
valor_aluguel_dia = 60.00
valor_km = valor_km_dia * km
valor_aluguel = valor_aluguel_dia * aluguel_dia
preço_final = valor_km + valor_aluguel
print(f'O valor total a pagar pelo aluguel do veículo é de R${preço_final:.2f}')

#--------------------------------------------------------------------------------------------------------------

#10) Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total de dias.

consumo_dia = int(input('Insira a quantidade de cigarros consumidos por dia: '))
anos_fumante = int(input('Insira o tempo em anos como fumante: '))
total_cigarros_consumidos = consumo_dia * anos_fumante * 365
total_minutos = total_cigarros_consumidos * 10
total_horas = total_minutos / 60
total_dias = total_horas / 24
print(f'O furmante perderá no total {total_dias:.2f} dias')

#--------------------------------------------------------------------------------------------------------------

#11) Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado a um milhão.

print('O numero 2 elevado a um milhão é composto de ', len(str(2 ** 1000000)), 'digitos')
