#students name and marks into dict as keyboard as a input 
n=int(input("Enter the number of students:"))
d={}
for i in range(n):
	name=input("Student name: ")
	marks=int(input("Enter Student Marks: "))
	d[name]=marks
print(d)
while True:
	name=input("Enter Student Name to get marks: ")
	marks=d.get(name,-1)
	if marks ==-1:
		print("Student not Found..!")
	else:
		print("The marks of {} = {}".format(name,marks))
	option=input("Do you want to find another  student marks[Yes|No]: ")
	if option=="No":
	  	break
print("Thanks for using our application(*_*) ")