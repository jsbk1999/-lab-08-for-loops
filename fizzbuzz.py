for i in range (1, 100):
	if (i % 3 == 0 + i % 5 == 0):
		print("Fizzbuzz")

	else:
		if (i % 3 == 0):
			print("Fizz")
		elif (i % 5 == 0):
			print("Buzz")
		else:
			print(i)
