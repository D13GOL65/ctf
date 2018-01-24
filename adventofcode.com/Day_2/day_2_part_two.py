checksum = 0

infile = open('Day_2/input_file.txt', 'r')

for line in infile:
	numbers = []
	strings = line.split('	')

	for pal in strings:
		numbers.append(int(pal))

	mod = 9

	for i in range(len(numbers)):
		for j in range(i+1,len(numbers)):

			if numbers[i] > numbers[j]:
				mod = numbers[i]%numbers[j]
				div = numbers[i]/numbers[j]

			elif numbers[j] > numbers[i]:
				mod = numbers[j]%numbers[i]
				div = numbers[j]/numbers[i]

			if mod == 0:
				checksum = checksum + div
				break

		if mod == 0:
			break


infile.close()



outfile = open('Day_2/output_file.txt', 'w')
outfile.write(str(checksum))
outfile.close()