#------Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro a idade uma pessoa, retornando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(idade):
    if idade >= 18:
        print('voto obrigatório')
    elif idade < 16:
        print('voto negado')
    elif idade == 16 or idade == 17:
        print('voto opicional')

idade = int(input('Digite a idade:'))
voto(idade)