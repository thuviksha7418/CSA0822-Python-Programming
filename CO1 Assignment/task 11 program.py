from decimal import Decimal

BASE_RATE = Decimal("30.00")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")

def calculate_rate(fat, snf):
    fat_steps = round((fat - Decimal("3.5")) / Decimal("0.1"))
    snf_steps = round((snf - Decimal("8.5")) / Decimal("0.1"))

    rate = (
        BASE_RATE
        + Decimal(fat_steps) * FAT_STEP_VALUE
        + Decimal(snf_steps) * SNF_STEP_VALUE
    )

    return rate

def calculate_payment(litres, fat, snf):
    rate = calculate_rate(fat, snf)
    payment = litres * rate
    return rate, payment.quantize(Decimal("0.01"))

try:
    litres = Decimal(input("Enter litres: "))
    fat = Decimal(input("Enter fat: "))
    snf = Decimal(input("Enter SNF: "))

    if litres < 0 or not Decimal("2.0") <= fat <= Decimal("7.0") or snf < 0:
        print("Invalid input.")
    else:
        rate, payment = calculate_payment(litres, fat, snf)

        print("Rate per Litre: Rs.", rate)
        print("Total Payment: Rs.", payment)

except Exception as e:
    print("Invalid input:", e)
