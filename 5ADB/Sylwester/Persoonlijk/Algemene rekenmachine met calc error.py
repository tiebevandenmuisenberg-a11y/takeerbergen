import math

def universal_root(number, root_degree):
    if root_degree == 0:
        return "Calculator Error: Root degree cannot be zero."
    
    if number < 0 and root_degree % 2 == 0:
        return "Calculator Error: Cannot take even root of a negative number."
    
    if number < 0:
        return -round((-number) ** (1 / root_degree), 2)
    
    return round(number ** (1 / root_degree), 2)

while True:
    try:
        Calculation = str(input("Choose an operation: (basic, advanced) or exit: ")).lower()
    except ValueError:
        print("Invalid input. Please enter an operation.")
        continue

    if Calculation == 'exit':
        print("Exiting calculator. Goodbye!")
        break

    elif Calculation in ('basic', 'b'):
        try:
            operation1 = str(input("Choose a basic operation (+, -, *, /) or 'back' to return: "))
            
            if operation1 == 'back':
                continue
        
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue
        
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if operation1 == '+':
            print(f"Result: {num1 + num2}")
        
        elif operation1 == '-':
            print(f"Result: {num1 - num2}")
        
        elif operation1 == '*':
            print(f"Result: {num1 * num2}")
        
        elif operation1 == '/':
            if num2 == 0:
                print("Calculator Error: Division by zero is not allowed.")
            else:
                print(f"Result: {num1 / num2}")
        
        
    elif Calculation in ('advanced', 'a'):
        try:
            operation2 = str(input("Choose an advanced operation (power, root, pi, shapes, trig functions) or 'back' to return: ")).lower()
        
            if operation2 == 'back':
                continue
        
        except ValueError:
            print("Invalid input. Please enter an operation.")
            continue
            
        
        if operation2 in ('power', '^'):
            try:
                base = float(input("Enter the base number: "))
                exponent = float(input("Enter the exponent: "))
                
                if base == 0 and exponent <= 0:
                    print("Calculator Error: 0 cannot be raised to a non-positive power.")
                else:
                    print(f"Result: {base ** exponent}")
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

        elif operation2 == 'root':
            while True:
                try:
                    if Calculation == 'back':
                        break
                
                    num_input = input("Enter the number you want to find the root of: ")
                    degree_input = input("Enter the root degree: ")

                    num = float(num_input)
                    degree = int(degree_input)

                    result = universal_root(num, degree)

                    if isinstance(result, str):
                        print(result)
                    else:
                        print(f"The {degree} root of {num} is: {result}")
                    break 

                except ValueError:
                    print("Invalid input. Please enter a numeric value for the number and an integer for the root degree.")
    
        elif operation2 == 'pi':
            try:
                pi_input = input("Enter the number you want to multiply pi with: ")
                print (f"Result: {(math.pi) * float(pi_input)}")

            except ValueError:
                print("Invalid input. Please enter a numeric value.")
                continue
    
        elif operation2 == 'shapes':
            while True:
                try:
                    shape = input("Choose a shape (circle, square, rectangle, triangle) or 'back' to return: ").lower()
                
                    if shape == 'back':
                        break
                
                    if shape == 'circle':
                        radius = float(input("Enter the radius of the circle: "))
                        area = math.pi * radius ** 2
                        perimeter = 2 * math.pi * radius
                        print(f"Circle Area: {round(area, 2)}, Perimeter: {round(perimeter, 2)}")
                
                    elif shape == 'square':
                        side = float(input("Enter the side length of the square: "))
                        area = side ** 2
                        perimeter = 4 * side
                        print(f"Square Area: {round(area, 2)}, Perimeter: {round(perimeter, 2)}")
                
                    elif shape == 'rectangle':
                        length = float(input("Enter the length of the rectangle: "))
                        width = float(input("Enter the width of the rectangle: "))
                        area = length * width
                        perimeter = 2 * (length + width)
                        print(f"Rectangle Area: {round(area, 2)}, Perimeter: {round(perimeter, 2)}")
                
                    elif shape == 'triangle':
                        base = float(input("Enter the base of the triangle: "))
                        height = float(input("Enter the height of the triangle: "))
                        side1 = float(input("Enter the length of side 1: "))
                        side2 = float(input("Enter the length of side 2: "))
                        area = 0.5 * base * height
                        perimeter = base + side1 + side2
                        print(f"Triangle Area: {round(area, 2)}, Perimeter: {round(perimeter, 2)}")
                
                    else:
                        print("Invalid shape. Please choose from circle, square, rectangle, triangle.")
            
                except ValueError:
                    print("Invalid input. Please enter numeric values for dimensions.")
    
        elif operation2 in ('trig' 'functions' 'trig functions'):
            while True:
                try:
                    if Calculation == 'back':
                        break
                
                    func = input("Choose a function (sin, cos, tan, asin, acos, atan) or 'back' to return: ").lower()
                
                    if func == 'back':
                        break
                
                    angle = float(input("Enter the angle in degrees: "))
                    radians = math.radians(angle)
                
                    if func == 'sin':
                        result = math.sin(radians)
                        print(f"sin({angle}) = {round(result, 4)}")
                
                    elif func == 'cos':
                        result = math.cos(radians)
                        print(f"cos({angle}) = {round(result, 4)}")
                
                    elif func == 'tan':
                        result = math.tan(radians)
                        print(f"tan({angle}) = {round(result, 4)}")
                
                    elif func == 'asin':
                        if angle < -1 or angle > 1:
                            print("Calculator Error: Input for asin must be in the range [-1, 1].")
                    
                        else:
                            result = math.degrees(math.asin(angle))
                            print(f"asin({angle}) = {round(result, 4)} degrees")
                
                    elif func == 'acos':
                        if angle < -1 or angle > 1:
                            print("Calculator Error: Input for acos must be in the range [-1, 1].")
                    
                        else:
                            result = math.degrees(math.acos(angle))
                            print(f"acos({angle}) = {round(result, 4)} degrees")
                
                    elif func == 'atan':
                        result = math.degrees(math.atan(angle))
                        print(f"atan({angle}) = {round(result, 4)} degrees")

                    else:
                        print("Invalid function. Please choose from sin, cos, tan, asin, acos, atan.")
            
                except ValueError:
                    print("Invalid input. Please enter a numeric value for the angle.")