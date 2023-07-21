n = int(input("Enter a number ::"))

result = 0
if n%2 ==0:
    r = n/2
    result = (r//2)*(2*r)
else:
    r = (n+1)/2
    result = (r//2)*(2*r)

print(result)
  