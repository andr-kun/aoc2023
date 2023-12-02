power = 0

with open('input.txt') as f:
	for line in f:
		game, rolls = line.strip().split(':')
		game = int(game.split()[-1])
		
		dice = {'r':0, 'g':0, 'b':0}
		for roll in rolls.split('; '):
			roll = roll.split(', ')
			
			for d in roll:
				n, col = d.split()
				dice[col[0]] = max(dice[col[0]], int(n))
		
		power += dice['r'] * dice['g'] * dice['b']
		 
print(power)

## regex-based solution
import re

power_re = 0

with open('input.txt') as f:
	for index, line in enumerate(f):
		r = max([int(i) for i in re.findall(r'(\d+) red', line)])
		g = max([int(i) for i in re.findall(r'(\d+) green', line)])
		b = max([int(i) for i in re.findall(r'(\d+) blue', line)])

		power_re += r*g*b

print(power_re)

## golf-ish solution (technically a one liner)

print(sum([max([int(i) for i in re.findall(r'(\d+) red', line)]) *
		   max([int(i) for i in re.findall(r'(\d+) green', line)]) *
		   max([int(i) for i in re.findall(r'(\d+) blue', line)])
		   for index, line in enumerate(open('input.txt'))]))

