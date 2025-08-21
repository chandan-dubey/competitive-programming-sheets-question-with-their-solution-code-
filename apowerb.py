base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))

result = 1
i = 1
while i <= exponent:
    result = result * base
    i += 1

print(result)
