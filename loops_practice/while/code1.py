l1 = []
x = int(input("Enter number of integer you want to print: "))
a = 1
while a <= x:
    z = int(input("Enter an integer: "))
    l1.append(z)
    a += 1
print(l1)
for i in l1:
    if max(l1) == i and i%2!=0:
        print(i)
