valid = 0

with open('input.txt') as f:
	for line in f:
		game, rolls = line.strip().split(':')
		game = int(game.split()[-1])
		
		for roll in rolls.split('; '):
			roll = roll.split(', ')
			dice = {'r':12, 'g':13, 'b':14}
			
			for d in roll:
				n, col = d.split()
				dice[col[0]] -= int(n)

			if min(dice.values()) < 0:
				break
		else:
			valid += game
		 
print(valid)

## regex-based solution
import re

valid_re = 0

with open('input.txt') as f:
	for index, line in enumerate(f):
		r = max([int(i) for i in re.findall(r'(\d+) red', line)])
		g = max([int(i) for i in re.findall(r'(\d+) green', line)])
		b = max([int(i) for i in re.findall(r'(\d+) blue', line)])

		if all([r <= 12, g <= 13, b <= 14]):
			valid_re += index+1

print(valid_re)

## golf-ish solution (technically a one liner)

print(sum([index+1 for index, line in enumerate(open('input.txt')) if
		   all([max([int(i) for i in re.findall(r'(\d+) red', line)]) <= 12,
		  max([int(i) for i in re.findall(r'(\d+) green', line)]) <= 13,
		  max([int(i) for i in re.findall(r'(\d+) blue', line)]) <= 14])]))