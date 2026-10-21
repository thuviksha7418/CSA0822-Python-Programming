BASE_RATE = 30.00
STANDARD_FAT = 3.5
STANDARD_SNF = 8.5

def rate_per_litre(fat, snf):
    fat_steps = round((fat - STANDARD_FAT) / 0.1)
    snf_steps = round((snf - STANDARD_SNF) / 0.1)
    return BASE_RATE + fat_steps * 0.40 + snf_steps * 0.30

def payout(litres, fat, snf):
    rate = rate_per_litre(fat, snf)
    return round(litres * rate, 2)

litres = 10
fat = 3.5
snf = 8.5

rate = rate_per_litre(fat, snf)
amount = payout(litres, fat, snf)

print("Rate per Litre: Rs.", format(rate, ".2f"))
print("Payment: Rs.", format(amount, ".2f"))
