input("enter values")
p=int(input())
q=int(input())
r=int(input())
if p==q and q==r and r==p:
    print("equilater triangle")
elif p==q or p==r or q==r:
    print("isoscale triangle")
else:
    print("scalene triangle")  