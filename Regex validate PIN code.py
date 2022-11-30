import re
pins = ['1','654','abc','abcd', '1234','123456']
def validate_pin(pin):
    #set strict patterns to 4 or 6 digit pins
    pattern4 = "[0-9]{4}"
    pattern6 = "[0-9]{6}"
    #check for a match on length 4 or 6 and return bool
    if len(pin) == 4:
        result = bool(re.match(pattern4, pin))
    elif len(pin) == 6:
        result = bool(re.match(pattern6, pin))
    #if not length 4 or 6 and not strictly a digit return false
    else:
        result = False
    return result

for idx, i in enumerate(pins):
    print(idx+1, validate_pin(i))

