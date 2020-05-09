"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
l=set()
in_c=set()
for i in calls:
    in_c.add(i[1])
in_t=set()
for i in texts:
    in_t.add(i[1])
rc_t=set()
for i in texts:
    rc_t.add(i[0])
for i in calls:
    if i[0] not in in_c and  i[0] not in in_t and i[0] not in rc_t:
        l.add(i[0])
l=list(l)
l.sort()
for i in l:
    print(i)
