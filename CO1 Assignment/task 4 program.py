BASE_RATE = 30.00
STANDARD_FAT = 3.5
STANDARD_SNF = 8.5
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30

litres = 10
fat = 4.0
snf = 8.7

fat_steps = round((fat - STANDARD_FAT) / 0.1)
snf_steps = round((snf - STANDARD_SNF) / 0.1)

rate = BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE
amount = round(litres * rate, 2)

print("Fat Steps:", fat_steps)
print("SNF Steps:", snf_steps)
print("Rate per Litre: Rs.", format(rate, ".2f"))
print("Total Payment: Rs.", format(amount, ".2f"))
