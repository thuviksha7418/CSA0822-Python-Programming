from decimal import Decimal
import time

n = 10000

start = time.perf_counter()
float_total = 0.0

for i in range(n):
    float_total += 0.10

float_time = time.perf_counter() - start

start = time.perf_counter()
decimal_total = Decimal("0.00")

for i in range(n):
    decimal_total += Decimal("0.10")

decimal_time = time.perf_counter() - start

print("Number of payments:", n)
print("Float Total:", float_total)
print("Decimal Total:", decimal_total)
print("Float Time:", float_time)
print("Decimal Time:", decimal_time)
print("Difference:", abs(float_total - float(decimal_total)))
