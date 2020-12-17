import random

guess_number = int(input('Enter secret number: '))
random_number = random.randrange(10)
guesses = 0

while True:
	if guess_number == random_number:
		print(f'Number {random_number} Guessed! ')
		print(f'Guesses Left = {3 - guesses}')
		break
	else:
		guesses = guesses + 1
		print(f'{4 - guesses} Guesses Left.')
		guess_number = int(input('Wrong Guess, Try Again: '))

		if guesses == 3:
			print('No More Guesses. Run Program Again.')
			break