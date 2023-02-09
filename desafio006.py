# Crie um algoritmo que leia um número que leia um número e mostre o seu dobro, triplo e raiz quadrada

numero = float(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
raizQuadrada = numero ** (1/2)

print('O dobro de {} é igual a: {}'.format(numero, dobro))
print('O triplo de {} é igual a: {}'.format(numero, triplo))
print('A raiz quadrada de {} é igual a: {}'.format(numero, raizQuadrada))

## Exemplo com menos variáveis e formatação do print

numero = float(input('Digite um número: '))

print('O dobro de {} é igual a: {}. \nO triplo de {} é igual a: {}. \nA raiz quadrada de {} é igual a: {}'.format(numero, (numero * 2), numero, (numero * 3), numero, (numero ** (1/2))))

# \n pula linha passando o conteúdo para a linha de baixo

## Exemplo de raiz quadrada com a função pow(n, n)

numero = int(input('Digite um número '))
print('A raiz quadrada de {} é igual a: {}'.format(numero, pow(numero, (1/2))))