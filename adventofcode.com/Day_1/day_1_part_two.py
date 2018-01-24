ac = 0

infile = open('Day_1/input_file.txt', 'r')

for line in infile:
	tamLine = len(line)
	mid = tamLine / 2

	for i in range(tamLine):

		if int(line[i]) == int(line[(i+mid)%tamLine]):
			ac = ac + int(line[i])


infile.close()


outfile = open('Day_1/output_file.txt', 'w')
outfile.write(str(ac))
outfile.close()