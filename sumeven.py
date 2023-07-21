n = int(input("Enter a number :: "))
sum=0
while(n>0):
    if n%2==0:
        sum =sum+n
        n-=2
    else:
        n-=1

print(f"{sum} is sum of all even number")