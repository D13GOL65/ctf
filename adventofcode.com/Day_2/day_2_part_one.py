checksum = 0

infile = open('Day_2/input_file.txt', 'r')

for line in infile:
	numbers = []
	strings = line.split('	')

	for pal in strings:
		numbers.append(int(pal))

	max_number = max(numbers)
	min_number = min(numbers)

	checksum = checksum + (max_number - min_number)

infile.close()



outfile = open('Day_2/output_file.txt', 'w')
outfile.write(str(checksum))
outfile.close()