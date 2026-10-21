def calculate_rate(fat, snf):
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)
    return 30.00 + fat_steps * 0.40 + snf_steps * 0.30

test_cases = [
    (10, 3.5, 8.5),
    (10, 4.0, 8.7),
    (10, 3.0, 8.0),
    (5, 2.0, 8.5),
    (5, 7.0, 8.5)
]

for litres, fat, snf in test_cases:
    rate = calculate_rate(fat, snf)
    payment = round(litres * rate, 2)

    print("Litres:", litres)
    print("Fat:", fat, "SNF:", snf)
    print("Rate: Rs.", format(rate, ".2f"))
    print("Payment: Rs.", format(payment, ".2f"))
    print("--------------------")
