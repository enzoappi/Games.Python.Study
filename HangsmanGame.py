# HANGMAN'S GAME

#Bibliotecas utilizadas:
import os

#Função para o título do game:
def titulo():
    print('-=' * 30)
    print(f'{"JOGO DA FORCA":^60}')
    print('-=' * 30)


#Função do GAME:
def forca():
    #Biblioteca e função para sortear um número:
    from random import randint
    #Base de dados do GAME:
    nomes = ('AOSTA', 'AREZZO', 'BARI', 'BERGAMO', 'BOLOGNA',
    'BRESCIA', 'CAGLIARI', 'CATANIA', 'CHIEVO', 'CROTONE',
    'EMPOLI', 'FIRENZE', 'FROSINONE', 'GENOVA', 'IMOLA',
    'LAZIO', 'LECCE', 'MILANO', 'MODENA', 'MONZA',
    'NAPOLI', 'PALERMO','PARMA', 'PERUGIA', 'PESCARA',
    'PISA', 'POMPEI', 'ROMA', 'SAN MARINO', 'SASSUOLO',
    'SIENA', 'TORINO', 'UDINE', 'VENEZIA', 'VERONA')
    #Execução do sorteio de um número:
    sorteio = randint(0, 34)
    #Varrendo a posição e o valor do elemento na base de dados do GAME:
    for p, n in enumerate(nomes):
        #Teste de igualdade entre o valor sorteado e a posição do elemento:
        if p == sorteio:
            #Alocação do valor e medida do tamanho do elemento da posição sorteada: 
            nome = n
            tam = len(nome)
    #Mascara com o tamanho do elemento sorteado, para alocar os acertos do usuário:
    palavra = '_ ' * tam
    #Criação de espaço entre os caractéres da mascara (Melhor visualização):
    provis = palavra.split()
    #Loop para receber e alocar as tentativas do usuário:
    while palavra != nome:
        titulo()
        print('\n\nA palavra é: ', end='')
        print(f'{" ".join(provis)}')
        letra = str(input('\nDigite uma letra: ').strip().upper())
        for p, v in enumerate(nome):
            if letra == v:
                provis[p] = letra
        palavra = ''.join(provis)
        os.system("clear")
    print(f'\nParabéns!\nVocê acertou!\n\nO nome é {palavra}.')


# Programa principal
forca()