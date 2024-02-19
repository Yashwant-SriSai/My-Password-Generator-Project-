#step 1: import random and string modules,take an empty array this will store the password generated
#step 2: take input to know the strength and length of passsword the user require
#step 3: give user options like password generator types(weak,medium, strong)
#step 4: take elemts to be included in list
#step 5: using extend method along with variables that we used for declaring type of elements ,extend the created empty list according to users  requirement
#step 6: print password
import string
import random
print("for weak password generation  choose 1")
print("for medium password generation choose 2")
print("for strong password generation  choose 3")
useri=int(input("enter strength of password you want:"))
s1=string.ascii_lowercase
s2=string.ascii_uppercase
s3=string.digits
s4=string.punctuation
p=[]
r=0

if (useri==1):
    plen=int(input("enter the length of the pass word you need :"))
    p.extend(list(s1))
    p.extend(list(s3))
    print ("your password is :")
    print("".join(random.sample(p,plen)))

elif (useri==2):
    plen=int(input("enter the length of the pass word you need :"))
    p.extend(list(s1))
    p.extend(list(s2))
    p.extend(list(s3))
    print ("your password is :")
    print("".join(random.sample(p,plen)))

elif (useri==3):
    plen=int(input("enter the length of the pass word you need :"))
    p.extend(list(s1))
    p.extend(list(s2))
    p.extend(list(s3))
    p.extend(list(s4))
    print ("your password is :")
    print("".join(random.sample(p,plen)))
else:
    print("wrong input!")

1