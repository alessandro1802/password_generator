import numpy as np
import string as str
import math

print("\n   Note: Sufficiently good password should contain at least 12 characters."
      " More or less acceptable password consists of 8 characters or more.")
l = int(input("Enter the password length: "))

### Check if the length is positive
while l <= 0:
    print("The length can't be less or equal to zero!")
    #quit()
    l = int(input("Enter the password length: "))

### Check if the length is more that 8
cont = True
if l < 8:
    cont = False
while cont == False:
    chooseNew = input("The chosen length is too small. Would you like to choose another value? (print 'yes' or 'no'): ")
    while chooseNew not in ("yes", "no"):
        chooseNew = input("Please write 'yes' or 'no': ")
    if chooseNew == "yes":
        l = int(input("Enter the password length: "))
        if l >= 8:
            cont = True
    elif chooseNew == "no":
        cont = True

### Create lists of characters
pas = []
punct = list(str.punctuation)
numb = list(str.digits)
lett = list(str.ascii_letters)
lowlett = list(lett[:26])
upplett = list(lett[26:])
np.random.shuffle(lowlett)
np.random.shuffle(upplett)
np.random.shuffle(numb)
np.random.shuffle(punct)

### Create the password
for i in range(math.floor(l*0.2)):
    pas.append(punct[i])
for i in range(math.floor(l*0.25)):
    pas.append(numb[i])
for i in range(math.floor(l*0.25)):
    pas.append(lowlett[i])
for i in range(math.floor(l * 0.25)):
    pas.append(upplett[i])

if len(pas) != l:
    all = []
    for i in range(len(lett)):
        all.append(lett[i])
    for i in range(len(punct)):
        all.append(punct[i])
    for i in range(len(numb)):
        all.append(numb[i])
    np.random.shuffle(all)
    for i in range(l - len(pas)):
        pas.append(all[i])

np.random.shuffle(pas)
print(''.join(pas))
input()