import random

length=int(input('Enter the length of the otp:')) 
otp=""
for i in range(length):
    digit=random.randint(0,9)
    otp=otp+str(digit)
print("Your OTP is",otp)



