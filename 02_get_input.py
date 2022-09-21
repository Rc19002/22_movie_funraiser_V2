import re


def is_blank(a):
    if a == '':
        return True
    return False



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


seat_holders("Name: ")
