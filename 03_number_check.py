while True:
    try:
        age = int(input("how old are you?"))
        if 12 > age or age > 130:
            print("please put a valid age")
            pass
        else:
            print("nice")
            break
    except ValueError:
        print("please use numbers for this part.")
