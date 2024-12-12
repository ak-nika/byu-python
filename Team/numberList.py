numbers = []
new_number = None

while new_number != 0:
    new_number = int(input("Enter a number: "))
    
    if new_number == 0:
        print("Done.")
    else:
        numbers.append(new_number)
        
# Calculate the sum and print it
sum = 0
for number in numbers:
    sum += number

print(f"The sum is: {sum}")

# Calculate the average and print it
average = sum / len(numbers)
print(f"The average is: {average}")

# Find the largest number and print it
largest = 0
for number in numbers:
    if number > largest:
        largest = number

print(f"The largest number is: {largest}")

# Stretch challenge
# Find the smallest positive number and print it
smallest = 9999999
for number in numbers:
    if number < smallest and number > 0:
        smallest = number

print(f"The smallest positive number is: {smallest}")

# Sort the numbers
numbers.sort()
for number in numbers:
    print(number)