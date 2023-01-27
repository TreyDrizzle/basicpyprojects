import random 

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "[]{}!@#$%^&*()*-+?"

upper, lower, nums, syms = True, True, True, True #Change vaule to False if you dont want to include. (True, False, False, Fasle) will only generate uppercase passwords


all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits
if syms:
    all += symbols

length = 20
amount = 1 

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)