#to call a new function
def no_blank(question):
    valid = False
    while not valid:
        response = input(question)
        while response != "":
            return response
        else:
            print("please enter your name don't leave this blank")

no_blank("name:")




def seat_holders(a):
    name = ""
    count = 0
    total_seat = 150

    while name != " " and count < total_seat:
        print("we have {} seats left".format(total_seat-count))
        response = input(a)
        count += 1
        print()
        while response != "":
            return response
        if count == total_seat:
            print("all the seats are taken thank you")
        else:
            print("we have sold {} tickets sold. \n" "there are {} seats still nat taken".format(count, total_seat - count))


seat_holders("Name: ")

