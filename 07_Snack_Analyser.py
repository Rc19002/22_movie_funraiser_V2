import re

test_strings = [str(input("> "))]

for item in test_strings:
    number_regex = "^[1-9]"
    if re.match(number_regex, item):
        amount = int(item[0])
        desired_snack = item[1:]
    else:
        amount = 1
        desired_snack = item
    desired_snack = desired_snack.strip()
    print("Amount:", amount)
    print("snack:", desired_snack)
    print("length of snack", len(desired_snack))
