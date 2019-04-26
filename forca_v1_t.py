# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

	# Método Construtor
	def __init__(self, palavra):
		self.palavra = palavra
		self.letras_erradas = []
		self.letras_corretas = []
		
	# Método para adivinhar a letra
	def adivinhar(self, letra):
		if letra in self.palavra and letra not in self.letras_corretas:
			self.letras_corretas.append(letra)
		elif letra not in self.palavra and letra not in self.letras_erradas:
			self.letras_erradas.append(letra)
		else:
			return False
		return True
		
	# Método para verificar se o jogo terminou
	def terminou_jogo(self):
		return self.venceu_jogo() or (len(self.letras_erradas == 6))
		
	# Método para verificar se o jogador venceu
	def venceu_jogo(self):
		if '_'not in self.palavra_escondida():
			return True
		return False

	# Método para não mostrar a letra no board
	def palavra_escondida(self):
		rtn = ''
		for letra in self.palavra:
			if letra not in self.letras_corretas:
				rtn += '_'
			else:
				rtn += letra
		return  rtn
		
	# Método para checar o status do game e imprimir o board na tela
	def print_status_jogo(self):
		print(board[len(self.letras_erradas)])
		print('\nPalavra: '+self.palavra_escondida())
		print('\nLetras Erradas:')
		for letra in self.letras_erradas:
			print(letra,)
		print()
		print('\nLetras corretas:')
		for letra in self.letras_corretas:
			print(letra,)
		print()

# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
        with open("palavras.txt", "rt") as f:
                bank = f.readlines()
        return bank[random.randint(0,len(bank))].strip()


# Função Main - Execução do Programa
def main():

	# Objeto
	game = Hangman(rand_word())

	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
	

	# Verifica o status do jogo
	game.print_game_status()	

	# De acordo com o status, imprime mensagem na tela para o usuário
	if game.hangman_won():
		print ('\nParabéns! Você venceu!!')
	else:
		print ('\nGame over! Você perdeu.')
		print ('A palavra era ' + game.word)
		
	print ('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa		
if __name__ == "__main__":
	main()
