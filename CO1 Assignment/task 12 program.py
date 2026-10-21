from decimal import Decimal

def calculate_rate(fat, snf, month):
    if month in [4, 5, 6]:
        base_rate = Decimal("32.00")
        fat_step_value = Decimal("0.45")
    else:
        base_rate = Decimal("30.00")
        fat_step_value = Decimal("0.40")

    snf_step_value = Decimal("0.30")

    fat_steps = round((fat - Decimal("3.5")) / Decimal("0.1"))
    snf_steps = round((snf - Decimal("8.5")) / Decimal("0.1"))

    rate = (
        base_rate
        + Decimal(fat_steps) * fat_step_value
        + Decimal(snf_steps) * snf_step_value
    )

    return rate

def calculate_bonus(total_litres):
    if total_litres > Decimal("500"):
        return total_litres * Decimal("0.50")
    return Decimal("0.00")

try:
    month = int(input("Enter month number (1-12): "))
    total_litres = Decimal(input("Enter total litres for 10 days: "))
    fat = Decimal(input("Enter fat percentage: "))
    snf = Decimal(input("Enter SNF percentage: "))

    if not 1 <= month <= 12:
        print("Invalid month.")
    elif total_litres < 0 or not Decimal("2.0") <= fat <= Decimal("7.0") or snf < 0:
        print("Invalid milk details.")
    else:
        rate = calculate_rate(fat, snf, month)
        payment = (total_litres * rate).quantize(Decimal("0.01"))
        bonus = calculate_bonus(total_litres).quantize(Decimal("0.01"))
        final_payment = payment + bonus

        print("Rate per Litre: Rs.", rate)
        print("Milk Payment: Rs.", payment)
        print("Bonus: Rs.", bonus)
        print("Final Payment: Rs.", final_payment)

except Exception as e:
    print("Invalid input:", e)
