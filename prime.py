print prime number from 1 to 100 using while loop

a = 1
while a < 100:
	if a > 1:
		b = 2
		prime = True
		while b < a:
			if a % b ==0:
				print (a,"prime nhi hai")
				prime = False
				break
			b+=1
		if (prime):
			print (a,"prime hai")
	a+=1 