# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.

nota1 = int(input('Insira sua nota: '))
nota2 = int(input('Insira sua nota: '))

print('Sua média é: {}'.format((nota1 + nota2) / 2))

## Exemplo com mais variáveis

nota1 = float(input('Digite sua primera nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
print('Essa é a sua média final: {}'.format(media))

## Exemplo em que mesmo que a nota seja um "número quebrado" seja printada só com o primeiro número (pode ser o primero, segundo, terceiro)

nota1 = float(input('Digite sua primeria nota: '))
nota2 = float(input('Digite sua segunda nota: '))

print('A média entre {:.0f} e {:.0f} é igual a: {:.0f}'.format(nota1, nota2, (nota1 + nota2) / 2))

# :.0 significa depois do ponto flutuante quero que tenham apenas zero números