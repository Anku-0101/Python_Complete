
def Natural_Number_Sum(n):
    if(n < 1):
        return "Please enter a natual number" 
    if(n==1):
        return 1

    else :
        return n + Natural_Number_Sum(n-1)


print(Natural_Number_Sum(8))
#print(Natural_Number_Sum(0))
#print(Natural_Number_Sum(3))
