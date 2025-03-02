import math
def calculator():
    while True:
        print("CALCULATOR")
        print("Select an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Power (^)")
        print("6. Square Root (√)")
        print("7. Exit")
        choice = input("Choose an operation (1-7 or symbol [+ - * / ^ √]): ").strip()
        if choice in ['7', 'exit', 'quit']:
            print("Exiting calculator. Goodbye!")
            break
        if choice in ['1', '+', '2', '-', '3', '*', '4', '/', '5', '^']:
            try:
                num1 = float(input("Enter first number: ").strip())
                num2 = float(input("Enter second number: ").strip())
                if choice in ['1', '+']:
                    print(f"✅ Result: {num1} + {num2} = {num1 + num2}")
                elif choice in ['2', '-']:
                    print(f"✅ Result: {num1} - {num2} = {num1 - num2}")
                elif choice in ['3', '*']:
                    print(f"✅ Result: {num1} * {num2} = {num1 * num2}")
                elif choice in ['4', '/']:
                    if num2 == 0:
                        print("❌ Error: Division by zero is not allowed.")
                    else:
                        print(f"✅ Result: {num1} / {num2} = {num1 / num2}")
                elif choice in ['5', '^']:
                    print(f"✅ Result: {num1} ^ {num2} = {num1 ** num2}")
            except ValueError:
                print("❌ Error: Please enter valid numeric values.")
        
        elif choice in ['6', '√']:
            try:
                num = float(input("Enter a number: ").strip())
                if num < 0:
                    print("❌ Error: Cannot calculate square root of a negative number.")
                else:
                    print(f"✅ Result: √{num} = {math.sqrt(num)}")
            except ValueError:
                print("❌ Error: Invalid input. Please enter a number.")
        else:
            print("❌ Invalid choice. Please select a valid option.")
        again = input("\nWould you like to perform another calculation? (yes/no): ").strip().lower()
        if again not in ['yes', 'y']:
            print("Goodbye! ")
            break
if __name__ == "__main__":
    calculator()
