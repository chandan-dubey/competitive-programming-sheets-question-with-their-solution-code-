A = int(input("Enter number: "))
temp = A
rev = 0
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

if A == rev:
    print("Yes, Palindrome")
else:
    print("No, Not Palindrome")
