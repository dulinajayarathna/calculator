# import operations as op
from operations import add,substract,multiply,division

print('1.add')
print('2.substract')
print('3.divide')
print('4.multiply')
option=input("select action :")
option=int(option)
x=int(input("enter number 1 : "))
y=int(input("eneter number2 : "))

if option==1:	
	print("answer is =",add(x,y))
if option==2:
	print("answer is =",substract(x,y))
if option==3:
	print("answer is =",multiply(x,y))
if option==4:
	print("answer is =",divis
	ion(x,y))