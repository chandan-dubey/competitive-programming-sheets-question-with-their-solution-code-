a = int(input("Enter base number: "))
b = int(input("Enter exponent: "))

ans = 1
for i in range(b):
    ans = ans * a  
print("a^b =", ans)

