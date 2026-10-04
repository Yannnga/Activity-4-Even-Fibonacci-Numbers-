#star number
first_number = 1
second_number = 2
total = 0

while second_number < 4000000:
    remainder = second_number % 2
    if remainder == 0:
        total += second_number

    next_number = first_number + second_number
    first_number = second_number
    second_number = next_number

print(total)