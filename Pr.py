def Display(n):
    i=1
    if n%2!=0:
        while(i<n):
            print(i,end=" ")
            i+=1
    else:
        return Display(n+1)

n = int(input())
Display(n)