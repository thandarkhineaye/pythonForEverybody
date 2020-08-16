'''
Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''

fname = input("Enter file:")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = dict()
splst = list()
try:
    fh = open(fname)
except:
    print("invalid file")
    quit()

for line in fh:
    if not line.startswith("From ") : 
        continue
    else:
        splst = line.split()
        count[splst[1]] = count.get(splst[1],0) + 1

largest = -1
address = None
for a,b in count.items():
    if b > largest:
        largest = b
        address = a
print(a,b)