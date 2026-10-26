def simple_calculator():
    print("\n--- SIMPLE CALCULATOR ---")
    print("Operations: +, -, *, /")
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ").strip()
        num2 = float(input("Enter second number: "))

        if op == "+":
            print(f"Result: {num1 + num2}")
        elif op == "-":
            print(f"Result: {num1 - num2}")
        elif op == "*":
            print(f"Result: {num1 * num2}")
        elif op == "/":
            if num2 != 0:
                print(f"Result: {num1 / num2}")
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid operator!")
    except ValueError:
        print("Error: Please enter valid numbers.")


def unit_converter():
    print("\n--- UNIT CONVERTER ---")
    print("1. Length (meters <-> feet)")
    print("2. Weight (kilograms <-> pounds)")
    print("3. Temperature (Celsius <-> Fahrenheit)")

    choice = input("Choose category (1/2/3): ").strip()

    if choice == "1":
        val = float(input("Enter value in meters: "))
        print(f"{val} meters = {val * 3.28084:.4f} feet")
    elif choice == "2":
        val = float(input("Enter value in kilograms: "))
        print(f"{val} kg = {val * 2.20462:.4f} lbs")
    elif choice == "3":
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        sub = input("Choose option (1/2): ").strip()
        if sub == "1":
            c = float(input("Enter °C: "))
            print(f"{c}°C = {(c * 9/5) + 32:.2f}°F")
        elif sub == "2":
            f = float(input("Enter °F: "))
            print(f"{f}°F = {(f - 32) * 5/9:.2f}°C")
        else:
            print("Invalid choice.")
    else:
        print("Invalid category.")


def main():
    while True:
        print("\n=== MAIN MENU ===")
        print("1. Calculator")
        print("2. Unit Converter")
        print("3. Exit")

        selection = input("Select an option (1-3): ").strip()

        if selection == "1":
            simple_calculator()
        elif selection == "2":
            unit_converter()
        elif selection == "3":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid selection, try again.")


if __name__ == "__main__":
    main()
