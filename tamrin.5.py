#We have a nested list and we want to calculate the total price of the items and give a 10% discount.


kala=[
     [1,"A",10,1400],
     [2,"B",15,2500],
     [3,"C",12,1700],
]
prices = (kala[0][3]*10, kala[1][3]*15, kala[2][3]*12)
print(list(prices))


y = lambda x : (x > 20000 )
z = (filter(y,prices))
print(list(z))

if z :
     print("10 percent discount")
     


















