import sys

sys.setrecursionlimit(10000)   #This is to overcome default python recursion limit

def fibonacci(num,start=2):
    memo[start]=memo[start-1]+memo[start-2]
    if(num==0):
        return 0
    elif(num==1):
        return 1
    elif(num==start):
        return 
    else:
        fibonacci(num,start+1)
        return memo[num]


memo={0:0,1:1} #global dictionary to store the fibonacci number already computed
a=int(input("Enter no. - "))
print("Fibonacci number:",fibonacci(a))
