#Python code to take user input and if mod 1 print Fizz else print buzz
#Does not have error exception, will fail if user enters anything but a real numberz

while True:
	x=int(input())
	y= (x % 2)
	if y == 1:
		print("You entered " + str(x) + " your answer is Fizz ")
	else:
		print ("buzz")
	break