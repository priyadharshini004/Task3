tamil = int(input("Enter the Tamil mark:"))
english = int(input("Enter the English mark:"))
maths = int(input("Enter the Maths mark:"))
physics = int(input("Enter the Physics mark:"))
chemistry = int(input("Enter the Chemistry mark:"))
computer_science = int(input("Enter the Computer science mark:"))
if(tamil>english and tamil>maths and tamil>physics and tamil>chemistry and tamil>computer_science):
	if(tamil>100):
		print("invalid tamil mark")
	else:
		print("max mark is",tamil)

elif(english>maths and english>physics and english>chemistry and english>computer_science):
	if(english>100):
		print("invalid english mark")
	else:
		print("max mark is",english)
elif(maths>physics and maths>chemistry and maths>computer_science):
	if(maths>100):
		print("invalid maths mark")
	else:
		print("max mark is",maths)
elif(physics>chemistry and physics>computer_science):
	if(physics>100):
		print("invalid physics mark")
	else:
		print("max mark is",physics)
elif(chemistry>computer_science):
	if(chemistry>100):
		print("invalid chemistry mark")
	else:
		print("max mark is",chemistry)
else:
	if(computer_science>100):
		print("invalid tamil mark")
	else:
	 	print("max mark is",computer_science)