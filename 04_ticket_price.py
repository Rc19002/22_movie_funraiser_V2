price = 0
while True:

    try:
        name = str(input("what is your name?"))
        age = int(input("how old are you?"))
        if age < 12:
            print("try again not old enough")
            continue
        elif age < 16:
            price = price + 7.50
        elif age < 65:
            price = price + 10.50
        else:
            price = price + 6.50

    except ValueError:
        print("try again")

    print("pay ${}".format(price))

    print("there any more? yes/no")
    answer = input("> ")
    if answer == "yes":
        continue
    else:
        break
