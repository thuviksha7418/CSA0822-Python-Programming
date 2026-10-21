try:
    farmer_id = input("Enter Farmer ID: ")
    litres = float(input("Enter Milk Quantity: "))
    fat = float(input("Enter Fat Percentage: "))
    snf = float(input("Enter SNF Percentage: "))

    if litres < 0:
        print("Milk quantity cannot be negative.")
    elif not 2.0 <= fat <= 7.0:
        print("Fat must be between 2.0 and 7.0.")
    elif snf < 0:
        print("SNF cannot be negative.")
    else:
        print("Farmer ID:", farmer_id)
        print("Quantity:", litres)
        print("Fat:", fat)
        print("SNF:", snf)

except ValueError:
    print("Invalid input. Enter numbers correctly.")
