score = input("Enter Score: ")
try:
	sfloat = float(score)	
except:
	print("Error: please insert in number format")
    quit()

if 0.0 < sfloat < 1.0:
    if sfloat >= 0.9:
        print("A")
    elif sfloat >= 0.8:
    	print("B")
	elif sfloat >= 0.7:
    	print("C")
	elif sfloat >= 0.6:
    	print("D")
    else:
        print("F")
    
else:
	print("Error: grading will be generate between 0.0 and 1.0")
    quit()