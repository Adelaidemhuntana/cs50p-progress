def main():
    
    expression = input("Expression: ")

  
    x, operator, z = expression.split()

  
    x = int(x)
    z = int(z)

  
    if operator == "+":
        result = x + z
    elif operator == "-":
        result = x - z
    elif operator == "*":
        result = x * z
    elif operator == "/":
        result = x / z

    print(f"{result:.1f}")

main()
