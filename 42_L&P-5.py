# Print numbers from 1 to 100 skipping multiples of 3.

for i in range(1, 101):
    if i % 3 == 0:
        continue
    print(i)