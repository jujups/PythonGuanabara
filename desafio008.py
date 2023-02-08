# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input('Quantos metros: '))

print('{} m em centímetros é igual a {} cm'.format(metros, metros * 100))
print('{} m em milímetros é igual a {} mm'.format(metros, metros * 1000))