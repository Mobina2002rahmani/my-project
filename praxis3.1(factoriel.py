#factoriel

n=int(input("enter a number : "))
s=1
if n<0:
    print("dont have facto")
elif n==0:
    print("no")
else :
    for i in range(1,n+1):
      s = s*i
print(s)


################################

import math
b=math.factorial(5)
print(b)