from collections import defaultdict
import time
import numpy as np

# all coord and dir is in (x, y) format

cached_state = set()

def tilt_platform(ball_pos, dir):
	x, y = ball_pos

	x, y = x+dir[0], y+dir[1]
	while ((x >= 0 and y >= 0) and (x < width and y < height)) and platform[y][x] == '.':
		# try to move the ball
		x, y = x+dir[0], y+dir[1]
	
	# Update only at the end to save unnecessary iterative updating 
	platform[ball_pos[1]][ball_pos[0]] = '.'
	platform[y-dir[1]][x-dir[0]] = 'O'
	
def tilt_col_row(col, row, dir):
	free_spot = None
	for x in row:
		for y in col:
			if platform[y][x] == '.' and free_spot is None:
				free_spot = (x, y)
			elif platform[y][x] == '#':
				free_spot = None
			elif platform[y][x] == 'O' and free_spot is not None:
				swap_x, swap_y = free_spot
				platform[y][x] = '.'
				platform[swap_y][swap_x] = 'O'
				free_spot = (swap_x-dir[0], swap_y-dir[1])
	
def run_cycle_alt():
	directions = [(0,-1), (-1,0), (0,1), (1,0)]
	iterator = {
		(0,-1): (range(width), range(height)), (-1,0): (range(width), range(height)),
		(0,1): (range(width), range(height-1, -1, -1)),
		(1,0): (range(width-1, -1, -1), range(height))
	}
	
	for dir in directions:
		
		if dir[0] == 0:
			for x in iterator[dir][0]:
				tilt_col_row(iterator[dir][1], [x], dir)
		else:
			for y in iterator[dir][1]:
				tilt_col_row([y], iterator[dir][0], dir)

def run_cycle():
	directions = [(0,-1), (-1,0), (0,1), (1,0)]
	iterator = {
		(0,-1): (range(width), range(1, height)), (-1,0): (range(1,width), range(height)),
		(0,1): (range(width), range(height-2, -1, -1)),
		(1,0): (range(width-2, -1, -1), range(height))
	}
	
	for dir in directions:
		for y in iterator[dir][1]:
			for x in iterator[dir][0]:
				if platform[y][x] == 'O':
					tilt_platform((x,y), dir)
				

def get_tilted_load(cycles):
	
	for i in range(cycles):
		run_cycle_alt()
		#print('Cycle',i)
		#for line in platform:
		#	print(''.join(line))
		#print('=========')
	
	load = 0
	for y in range(height):
		for x in range(width):
			if platform[y][x] == 'O':
				load += height-y
	return load


with open('input.txt') as f:
	platform = []
	mapping = {'.':0, 'O':1, '#':-1}
	for line in f:
		line = line.strip()
		platform.append([c for c in line])
	
	#platform = np.array(platform)
	#print(platform)
	
	t = time.time()
	width, height = len(platform[0]), len(platform)
	load_total = get_tilted_load(100)
	print(time.time()-t)

print(load_total)