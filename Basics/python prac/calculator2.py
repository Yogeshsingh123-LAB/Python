import operator
def calsomething():
    expression = input ("enter an expression :").strip()
    
    try:
       x,y,z= expression.split()
       opps= {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
       x,z = int(x), int(z)
    except ValueError:
        print ("Please enter: `<int> <operator> <int>`")
        return
    if y in opps:
        if y=="+":
            k= opps[y],(x,z)
            print(f"the sum is {k}")
        elif y== "-":
            k= opps[y],(x,z)
            print(f"the sub is {k}")
        elif y=="*":
            k= opps[y],(x,z)
            print (f"the product is {k}")
        elif y== "/" and z == 0:
            print("denominator cannot be zero")
        else : 
               k= opps[y],(x,z)
               print(f"division is {k}")
    else:
            print("unsupported operator")

        
