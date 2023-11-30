import random

mayus = "ABCDEFGHJKLMNOPQRSTUVWXYZ"
minus = mayus.lower()
nums = "1234567890"
spec_chars = "!@$%^&()=-_+;:',./"

all = ""
length = input("Choose the lenght of your password: ")
length = int(length)
amount = input("How many passwords would you like to generate?: ")
amount = int(amount)

upper, lower, digs, specs = True, True, True, True

if upper:
    all += mayus
if lower:
    all += minus
if digs:
    all += nums
if specs:
    spec_chars

for x in range(amount):
    psw = "".join(random.sample(all, length))
    print(psw)
