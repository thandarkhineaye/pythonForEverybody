import re

fname = input("Enter file:")
if len(fname) < 1 : fname = "C3_week1_assign1.txt"
fh = open(fname)
try:
    fh = open(fname)
except:
    print("invalid file")
    quit()

numlist = list()
for line in fh:
    line = line.rstrip()
    e = re.findall("([0-9]+)", line)
    if len(e) < 1 : continue

    for i in range(len(e)):
        num = float(e[i])
        numlist.append(num)

print(sum(numlist))