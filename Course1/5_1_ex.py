largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    
    if num == "done" : 
        break
    else:
        try:
            inputnum = float(num)
            if largest is None:
                largest = inputnum
            elif inputnum > largest:
                largest = inputnum

            if smallest is None:
                smallest = inputnum
            elif inputnum < smallest:
                smallest = inputnum
        except:
            print("Invalid Input")
            continue


    print(num)

print("Maximum", int(largest))
print("Minimum", int(smallest))