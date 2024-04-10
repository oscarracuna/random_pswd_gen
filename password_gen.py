import random
import math
from string import ascii_letters
from string import digits

#Just for fun hehe
sec_tips = [
            "remember to periodically update your passwords! :)","Add an extra layer of security by enabling 2FA when available. :)",
            "Don't trust unsolicited messages or calls asking for personal information.", "Avoid connecting to public Wi-Fi for sensitive transactions.",
            "Stay safe :)"
            ]
spec_chars = "!@$%^&()=-_+;:',./"

all = ""
lenght = input("Lenght of the password: ")
lenght = int(lenght)
amount = input("How many passwords to generate? ")
amount = int(amount)

lett, digs, specs = True, True, True

if lett:
            all += ascii_letters
if digs:
            all += digits
if specs:
            all += spec_chars

print(f"\nQuick security tips: \n {random.choice(sec_tips)}\n")
for x in range(amount):
            psw = "".join(random.sample(all, lenght))
            print("--> " + psw)
print("\n")

question_entropy = input("Would you like to know your password's entropy level?")

if question_entropy == 'y' ir 'yes':
            ent_1 = int(52) 
            ent_2 = int(10)
            ent_3 = int(30)

            R = ent_1 + ent_2 + ent_3
            L = lenght
            RTL = R ** L
            entropy_level = float((math.log2(RTL)))
            entropy_level = float(entropy_level)
            print(f"\nOk, your password entropy measure is: {entropy_level}")

            if entropy_level >= 120:
                        print("Your password is VERY strong.\n")
            if entropy_level >= 60:
                        print("Your password is STRONG.\n")
            if entropy_llevel >=36:
                        print("Your password is WEAK.\n")
            else:
                        print("Your password is VERY weak.\n")

else:
            pass
