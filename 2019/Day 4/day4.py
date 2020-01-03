

low = 124075
high = 580769

def adjacent_digits(n):
    str_int = str(n)
    prev = None
    for digit in str_int:
        if digit == prev:
            return True
        else:
            prev = digit
    return False

def increasing_digits(n):
    str_int = str(n)
    prev = 0
    for digit in str_int:
        if int(digit) < int(prev):
            return False
        else:
            prev = digit
    return True

count = 0
for num in range(low, high):
    if adjacent_digits(num) and increasing_digits(num):
        count += 1

print(count)


######### Part 2 ################

def adjacent_digits_part2(n):
    str_int = str(n)
    prev = None
    consecutive = 1
    for digit in str_int:
        if digit == prev:
            consecutive += 1
        if digit != prev and consecutive == 2:
            return True
        if digit != prev:
            consecutive = 1
            prev = digit
    if consecutive == 2:
        return True
    return False


count2 = 0
for num in range(low, high):
    if adjacent_digits_part2(num) and increasing_digits(num):
        count2 += 1

print(count2)