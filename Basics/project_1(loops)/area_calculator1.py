print("==================\nArea Calculator 📐\n==================")
shape = input("Enter the shape (circle, rectangle, triangle, square): ").lower()
if shape == "circle":
    radius = float(input("Enter the radius of the circle: "))
    area = 3.14159 * radius ** 2
    print(f"The area of the circle is: {area:.2f}")
elif shape == "rectangle":
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print(f"The area of the rectangle is: {area:.2f}")
elif shape == "triangle":
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print(f"The area of the triangle is: {area:.2f}")
elif shape == "square":
    side = float(input("Enter the side length of the square: "))
    area = side ** 2
    print(f"The area of the square is: {area:.2f}")
else:
    print("Invalid shape entered. Please enter circle, rectangle, triangle, or square.")