import random
from string import ascii_letters
from string import digits

spec_chars = "!@$%^&()=-_+;:',./"

sec_tips = [
            "remember to periodically update your passwords! :)","Add an extra layer of security by enabling 2FA when available. :)",
            "Don't trust unsolicited messages or calls asking for personal information.", "Avoid connecting to public Wi-Fi for sensitive transactions.",
            "Stay safe :)"
            ]

all = ""
length = input("Choose the lenght of your password: ")
length = int(length)
amount = input("How many passwords would you like to generate?: ")
amount = int(amount)

letts, digs, specs = True, True, True

if letts:
    all += ascii_letters
if digs:
    all += digits
if specs:
    all += spec_chars

print(f'\n\nQuick security tip: {random.choice(sec_tips)}\n')

for x in range(amount):
    psw = "".join(random.sample(all, length))
    print("--> "+psw)
print("\n")
    

