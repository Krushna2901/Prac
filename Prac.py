while(True):
    ans = input("Enter a input")

    if ans[0]=="-":
        r = ans[1:].isdigit()
        if r==True:
           print("right")
           break
    elif ans.isdigit():
        print("Right")
        break
    else:
        print("\nEnter a digit ::")


