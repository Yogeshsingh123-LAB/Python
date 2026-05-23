#find cube root of a perfect cube number
x = int(input("Enter a number: "))
ans = 0
while ans**3<abs(x):
    ans += 1
if ans**3 != abs(x):
    print(x, "is not a perfect cube")
else:
    if x<0:
        ans = -ans
    print("Cube root of", x, "is", ans)