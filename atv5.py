#--Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente

def ficha(nome,gols):
    return f'O jogador {nome} marcou {gols} gol(s)'

nome = input('Digite o nome do jogador: ')
gols = int(input('Digite a quantidade de gols:'))
print(ficha(nome,gols))
