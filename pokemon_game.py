# What Pokemon are you?
# 1. Multiply the day you were born by the month you were born
# 2. Multiply the results by the amount of letters in your name
# 3. Divide the result by 2 until it's 649 or under
# 4. Google "Pokemon Number" and your result
# ----
# We shall compute the range of the above function, to see
# which Pokemon no one can be.
from datetime import *
import re

# 1.
d = date(1,1,1)   # January 1, 0001 CE
one_day = timedelta(1) # 1 day
prods = set([])
for i in range(365):
    d += one_day
    prods.add(d.day * d.month)
prods.add(2 * 29) # leap day

#2. 
lprods = list(prods)
prods = set([])
for p in lprods:
    for k in range(1,13): # Names are never longer than 12 chars
        prods.add(p*k)

#3.
lprods = list(prods)
prods = set([])
for p in lprods:
    while p > 649:
        p = int(p/2)
    prods.add(p)
nprods = set(range(1,max(prods))) - prods
lprods = list(nprods)

#4.
pat = "\{\{rdex\|\d{3}\|(\d{3})\|([A-Za-z ]+)\|\d(?:\|[A-Za-z]+){1,2}\}\}"
prog = re.compile(pat)
with open("pokemon.txt", "r") as pokemon_list:
    for line in pokemon_list:
        match = prog.match(line)
        if match and int(match.group(1)) in lprods:
            print "%s. %s" % match.group(1,2)

