a= int(input("enter the value: "))
b= int(input("enter the value:"))
x=a+b
print ("the sum of the given values are ", x)
def positive_test():
    if x>=0:
        print("it is positive no. ")
    else :
        print("it is negative no.")
        return
def even_notest():
    if x%2==0:
        print("it is even no. ")
    else :
        print("it is odd no.")
if __name__=="__main__":
    positive_test()
    even_notest()
