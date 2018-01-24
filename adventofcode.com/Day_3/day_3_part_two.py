import math


def create_grid(end):
	next_pos = ['north', 'west', 'south', 'east']
	it = 0

	#Create matrix
	N = 1 + int(math.sqrt(end))

	if N%2 == 0:
		N = N + 1


	grid = [0] * N
	for i in range(N):
	    grid[i] = [0] * N



	#write data
	i = int(N/2)
	j = i

	grid[i][j] = 1

	j = j + 1

	while 1:

		n = add_adjacent(grid, i, j)

		grid[i][j] = n

		it = (it + 1)%4

		if n > end:
			break

		if next_pos[it] == 'west':
			if grid[i][j-1] == 0:
				j = j - 1
			else:
				it = (it - 1)%4
				i = i - 1

		elif next_pos[it] == 'south':
			if grid[i+1][j] == 0:
				i = i + 1
			else:
				it = (it - 1)%4
				j = j - 1

		elif next_pos[it] == 'east':
			if grid[i][j+1] == 0:
				j = j + 1
			else:
				it = (it - 1)%4
				i = i + 1

		elif next_pos[it] == 'north':
			if grid[i-1][j] == 0:
				i = i - 1
			else:
				it = (it - 1)%4
				j = j + 1



	return grid, n


def add_adjacent(grid, i, j):
	ac = grid[i+1][j] + grid[i+1][j+1] + grid[i][j+1] + grid[i-1][j+1] + grid[i-1][j] + grid[i-1][j-1] + grid[i][j-1] + grid[i+1][j-1]

	return ac


def main():
	infile = open('Day_3/input_file.txt', 'r')

	for line in infile:
		end = int(line)

	infile.close()

	tupl = create_grid(end)

	grid = tupl[0]


	outfile = open('Day_3/grid.txt', 'w')

	for i in range(len(grid)):

		outfile.write(str(grid[i])+'\n')

	outfile.close()

	result = tupl[1]

	outfile = open('Day_3/output_file.txt', 'w')

	outfile.write(str(result))

	outfile.close()


#Start program
main()
