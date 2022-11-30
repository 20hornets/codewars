list1 = []
list2 = ["Peter"]
list3 = ["Jacob", "Alex"]
list4 = ["Max", "John", "Mark"]
list5 = ["Alex", "Jacob", "Mark", "Max"]
def likes(names):
    if len(names) == 0:
        likes = "no one likes this"
    elif len(names) == 1:
        likes = f'{names[0]} likes this'
    elif len(names) == 2:
        likes = f'{names[0]} and {names[1]} like this'
    elif len(names) == 3:
        likes = f'{names[0]}, {names[1]} and {names[2]} like this'
    else:
        likes = f'{names[0]}, {names[1]} and {len(names)-2} others like this'
    return likes

print(likes(list1))
print(likes(list2))
print(likes(list3))
print(likes(list4))
print(likes(list5))


