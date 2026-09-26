num= int(input("Enter a number: "))
num1= int(input("Enter a number: "))
num2= int(input("Enter a number: "))

if num > num2 and num > num1:
        print(f"{num} is greater than both number ")
elif num1 > num and num1 > num2:
        print(f"{num1} is greater than both numbers")
else:
        print (f"{num2} is greater than both numbers")