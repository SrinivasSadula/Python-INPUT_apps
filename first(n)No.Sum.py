#First (n) numbers Sum Problem using python
#Example:- first n=5 numbers Sum equal to 1+2+3+4+5 =15  
n=int(input("Enter Some number:"))
sum=0
i=1
while i<=n:
	sum=sum+i
	i+=1
print("The Sum of first", n, "Numbers is",sum)
