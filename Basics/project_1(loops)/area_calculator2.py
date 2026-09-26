print("==================\nArea Calculator 📐\n==================")
print("1) Triangle\n2) Rectangle\n3) Square\n4) Circle\n5) Quit")
while True:
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = 0.5 * base * height
        print(f"The area of the triangle is: {area:.2f}")
    elif choice == '2':
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = length * width
        print(f"The area of the rectangle is: {area:.2f}")
    elif choice == '3':
        side = float(input("Enter the side length of the square: "))
        area = side ** 2
        print(f"The area of the square is: {area:.2f}")
    elif choice == '4':
        radius = float(input("Enter the radius of the circle: "))
        area = 3.14159 * radius ** 2
        print(f"The area of the circle is: {area:.2f}")
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")