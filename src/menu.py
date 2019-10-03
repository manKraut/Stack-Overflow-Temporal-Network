def menu():
    print(
        "Below, there is a series of options, in order to extract several info from the given data set of"
        " network. Please, follow the order and press buttons 1 to 7 in an ascendant order, for the proper"
        " functionality of the program.\n\n"
        "1.\n"
        "2.\n"
        "3.\n"
        "4.\n"
        "5.\n"
        "6.\n"
        "7.\n\n")


def return_to_choice():
    choice = -1
    print("Specify option.")
    while True:
        try:
            choice = int(input())
        except ValueError:
            print("Please provide a valid option from the given in man menu")
            continue
        if 1 <= choice <= 7:
            break
        else:
            print("Please provide a valid option from the given in main menu")
    return choice
