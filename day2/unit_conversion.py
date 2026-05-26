while True:
    print("Unit Convertor")
    print("1. Celsius to Farenheit")
    print("2. Farenheit to Celsius")
    print("3. Meters to Kilometers")
    print("4. Kilometers to Meters")
    print("5. Exit")

    choice = int(input("Enter your option "))

   
    if choice == 5:
        print("Exiting program")
        break

    val = float(input("Enter value: "))

    match choice:
        case 1: 
            result = (val * 9/5) + 32
            print(f"Result (Farenheit): {result}")

        case 2:
            result = (val - 32) * 5/9
            print(f"Result (Celsius): {result}")

        case 3:
            result = val / 1000
            print(f"Result (KM): {result}")

        case 4:
            result = val * 1000
            print(f"Result (m): {result}")

        case _:
            print("Invalid choice")


        
    # if choice == 1:
    #     result = (val * 9/5) + 32
    #     print(f"Result (Farenheit): {result}")
    # elif choice == 2:
    #     result = (val - 32) * 5/9
    #     print(f"Result (Celsius): {result}")
    # elif choice == 3:
    #     result = val / 1000
    #     print(f"Result (KM): {result}")
    # elif choice == 4:
    #     result = val * 1000
    #     print(f"Result (m): {result}")
    # else:
    #     print("invalid choice")