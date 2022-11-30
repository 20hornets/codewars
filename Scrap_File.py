text1 = "the-stealth-warrior"
text2 = "The_Stealth_Warrior"

def to_camel_case(text):
    camel = []
    name = ''
    checker_1 = text.find("-")
    if checker_1 > 0:
        text = text.replace("-", " ")
    checker_2 = text.find("_")
    if checker_2 > 0:
        text = text.replace("_", " ")
    text = text.split(" ")
    for idx, word in enumerate(text):
        if idx == 0:
            camel.append(word)
        else:
            x = word.capitalize()
            camel.append(x)
    name = name.join(camel)
    return name

print(to_camel_case(text1))
print(to_camel_case(text2))
#
# word_0 = text2
# for idx, word in enumerate(text):
#     if idx == 0:
#         print(idx)
#         camel.append(word)
#     else:
#         print(idx)
#         word.capitalize()
#         camel.append(word)








