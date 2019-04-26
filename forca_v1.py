# -*- coding: utf-8 -*-

#Jogo da Forca

#import
import random

board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

 +---+
 |   |
     |
     |
     |
     |
=========''','''

 +---+
 |   |
 0   |
     |
     |
     |
=========
''','''

 +---+
 |   |
 0   |
 |   |
     |
     |
=========
''','''

 +---+
 |   |
 0   |
/|   |
     |
     |
=========
''','''

 +---+
 |   |
 0   |
/|\  |
     |
     |
=========
''','''

 +---+
 |   |
 0   |
/|\  |
/    |
     |
=========
''','''

 +---+
 |   |
 0   |
/|\  |
/ \  |
     |
=========''']

#Classe
class Forca:

    #construtor
    def __init__(self,palavra,status):
        self.palavra = palavra
        self.status = status

    #adivinhar a letra
    def adivinhar(self, letra):
        pos=[]
        cont = self.palavra.count(letra)
        x = 0
        while x < cont:
            y = 0
            while y < len(self.palavra):
                if self.palavra[y] == letra:
                    pos.append(y)
                    x += 1
                y += 1
        return pos
        #self.palavra.find(letra)
        #return self.palavra.count(letra)

    #verificar se o jogo terminou
    def terminou_forca(self, palavra):
        return self.status == 7 or self.palavra == palavra

    #verificar se o jogador venceu
    def venceu_forca(self, palavra):
        return self.palavra == palavra

    #checar o status do game e printar o board na tela
    def print_status_jogo(self):
        #print(board[self.status])
        return board[self.status]

#lê uma palavra aletória do arquivo
def rand_palavra():
    with open("palavras.txt","rt") as f:
        bank = f.readlines()
    return bank[random.randint(0,len(bank)-1)].strip()

#main
def main():
    #objeto
    game = Forca(rand_palavra(),0)

    #status = 0
    letrasErradas = ''
    letrasCorretas = ''
    palavraAux = []
    for x in game.palavra:
        palavraAux.append('_')
    teste = '_'*len(game.palavra)
    #enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while not game.terminou_forca(teste):
        print(game.print_status_jogo())
        print('\nPalavra: '+teste)
        #print(palavraAux)
        print('\nLetras Erradas: \n' + letrasErradas)
        print('\nLetras Corretas: \n' + letrasCorretas)
        letra = input('Digite uma letra: ')
        pos = game.adivinhar(letra)
        if len(pos) > 0:
            letrasCorretas += letra
            for x in pos:
                palavraAux[x] = letra
        else:
            letrasErradas += letra
            game.status += 1
        teste = ''
        for x in palavraAux:
            teste += x

    #verifica o status do jogo
    #game.print_status_jogo()

    #de acordo com o status, imprime mensagem na tela para o usuário
    if game.venceu_forca(teste):
        print('\nParabéns! Você venceu!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era '+game.palavra)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')

#executa o programa
if __name__ == "__main__":
    main()