num= int(raw_input("Enter a number:"))
result=""
for i in range(32):
	if (num%2==0):
		result=str(0)+result
	elif(num%2==1):
		result=str(1)+result
	elif(num==0):
		break
	num=num/2
print result
