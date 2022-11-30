

num1 = 42145
num2 = 145263
num3 = 123456789

def descending_order(num):
    x = str(num)
    numbers = []
    #convert an integer into a string list
    for integer in x:
        numbers.append(integer)
    #sort the list from largest to smallest
    sorted_nums = sorted(numbers, reverse = True)
    #join the list return it to integer form
    sorted_nums = int("".join(sorted_nums))
    return sorted_nums

print(descending_order(num1))
print(descending_order(num2))
print(descending_order(num3))
