#*
#**
#***
#**** need this 

n=int(input("Enter Number of rows:"))
for i in range(1,n+1): #i represents row number
	for j in range(1,i+1): #j represents column no.(no.of stars)
		print("*",end=" ")
	print()