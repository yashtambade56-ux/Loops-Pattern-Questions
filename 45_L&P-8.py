# Count how many digits are in a number (no string conversion).

num = 123456
count = 0
while num > 0:
    num //= 10
    count += 1
print("Number of digits:", count)