hrs = input("Enter Hours:")
h = float(hrs)

rte = input("Enter Rate:")
r = float(rte)

pay = 0

if h > 40:
    aboveh = h - 40
    abover = r * 1.5
    pay1 = 40 * r
    pay2 = aboveh * abover
   	pay = pay1 + pay2
    
else:
	pay = h * r

print(pay)