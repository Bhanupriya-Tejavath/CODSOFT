print("=" * 40)
print("      CodSoft Smart Calculator")
print("=" * 40)

operations = {
    "+": "Addition",
    "-": "Subtraction",
    "*": "Multiplication",
    "/": "Division",
    "%": "Modulus",
    "//": "Floor Division",
    "**": "Power"
}

for symbol, name in operations.items():
    print(f"{symbol:>3} : {name}")

try:
    num1 = float(input("\nEnter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Choose operation (+, -, *, /, %, //, **): ").strip()

    if op not in operations:
        print("Invalid operation selected.")
    elif op in ["/", "//", "%"] and num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            result = num1 / num2
        elif op == "%":
            result = num1 % num2
        elif op == "//":
            result = num1 // num2
        elif op == "**":
            result = num1 ** num2

        print(f"\nResult: {num1} {op} {num2} = {result}")

except ValueError:
    print("Please enter valid numeric values.")