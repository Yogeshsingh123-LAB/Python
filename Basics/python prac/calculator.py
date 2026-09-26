def main():
    expression= input("enter a expression:")
    x,y,z= expression.split()
    x= int(x)
    z= int(z)
    if y == "+":
        result= x+z
    elif y =="-":
        result =x-z
    elif y =="*":
        result =x*z
    elif y == "/":
      if z==0:
          print ("0 is not allowed ")
      else:
          result= x/z
    print(f"{result:.1f}")
if __name__=="__main__":
    main()
