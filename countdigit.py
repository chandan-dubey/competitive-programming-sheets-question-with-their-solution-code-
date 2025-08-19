number = int(input("Enter the number: "))
count = 0

while number > 0:
    count += 1          
    number //= 10       
print("Total digits:", count)
