import random

input_num = int(input('Enter lucky num: '))
randomNum = random.randrange(10)
print(randomNum)
guesses = 0

while True:
	if input_num == randomNum:
		print('Num Guessed! ')
		print(f'Guesses left {3 - guesses}')
		break
	else:
		print('Wrong Guess, Try Again: ')
		input_num = int(input('Enter lucky num: '))
		guesses = guesses + 1
		print(guesses)
		if guesses == 3:
			print('No More Guesses. Run Program Again')
			break