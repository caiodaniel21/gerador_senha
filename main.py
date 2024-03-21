from random import choice

caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

senha = []

n_caracteres = 8
n_letra = 6
n_digitos = 2

for i in range(n_letra):
  ch = choice(caracteres)
  while not ch.isalpha():
    ch = choice(caracteres)
  senha += ch

for i in range(n_digitos):
  ch = choice(caracteres)
  while not ch.isdigit():
    ch = choice(caracteres)
  senha += ch

senha_string = ''.join(senha)

print (senha_string)

nome_arquivo = input('Digite o nome o arquivo para salvar a senha')

with open(nome_arquivo, 'a', enconding='utf-8') as arquivo:
  arquivo.write(f'{senha_string}\n')
