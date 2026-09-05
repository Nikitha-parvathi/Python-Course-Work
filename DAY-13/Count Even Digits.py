num = input("Enter a number: ")
count = 0

for digit in num:
    if int(digit) % 2 == 0:
        count += 1

print("Even Digits:", count)