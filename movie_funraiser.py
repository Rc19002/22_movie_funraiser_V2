import re


def seat_holders(ask, count=0, total_seat=150):
    name = ""
    while name != " " and count < total_seat:
        print("we have {} seats left".format(total_seat - count))
        response = ''.join(re.findall('[a-zA-Z]', input(ask)))  # Filter out all characters that are not within a-zA-Z that are inputted
        if is_blank(response):
            continue
        count += 1
        if count == total_seat:
            print("all the seats are taken thank you")
        else:
            print("we have sold {} tickets sold. \n" "there are {} seats still not taken".format(count,
                                                                                                 total_seat - count))


def no_blank(question):

    valid = False
    while not valid:
        response = input(question)
        while response != "":
            return response
        else:
            print("please enter your name don't leave this blank")

price = 0
while True:
    no_blank("name:")
    pass
    seat_holders("")
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


def is_blank(a):
    if a == '':
        return True
    return False






