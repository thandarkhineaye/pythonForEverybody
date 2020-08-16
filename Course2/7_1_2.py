# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
x = 0
y = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    else:
        x = x + 1
        y = y + float(line[21:])
print("Average spam confidence:", float(y/x))
