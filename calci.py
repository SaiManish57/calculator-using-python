import math
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
def combination(x,y):
    return math.comb(x,y)
def permutation(x,y):
    return math.perm(x,y)
def square(x):
    return x*x
def root(x):
    return math.sqrt(x)
operations={"+":add,"-":sub,"*":multiply,"/":divide,"nCr":combination,"nPr":permutation,"square":square,"root":root}
def calculator():
    print("List of Operations : ")
    for symbol in operations:
        print(symbol)
    result = None
    while True:
        op=input("Select an operation to perform : ")
        if op in ["+","-","*","/"]:
            if result is not None:
                n1=result
                n2=float(input("Enter the Second number : "))
            else:
                n1=float(input("Enter the first number : "))
                n2=float(input("Enter the Second number : "))
            calcifn=operations[op]
            result=calcifn(n1,n2)
            print(f"{n1}{op}{n2}={result}")
        elif op in ["nPr","nCr"]:
            if result is not None:
                n1=round(result)
                n2=int(input("Enter the Second number : "))
            else:
                n1 = int(input("Enter the first number : "))
                n2 = int(input("Enter the Second number : "))
            calcifn=operations[op]
            result=calcifn(n1,n2)
            if op == "nPr":
                print(f"{n1}P{n2}={result}")
            else:
                print(f"{n1}C{n2}={result}")
        elif op in ["square","root"]:
            if result is not None:
                n1=result
            else:
                n1 = float(input("Enter the number :"))
            calcifn=operations[op]
            result=calcifn(n1)
            print(f"{op} of {n1} = {result}")
        else:
            print("Invalid input!! Try Again")
            continue
        temp1=int(input(f"Enter 1 to continue operation with {result} or 2 to start a new operation or 3 to exit : "))
        if temp1==1:
            continue
        elif temp1==2:
            result=None
        elif temp1==3:
            print("Exiting calculator. Thank You!!")
            break
        elif (temp1 != 1 or temp1 != 2 or temp1 != 3):
            print('Invalid Input!!')
            break
calculator()