def check_for_stop(user_input):
        if user_input.upper() == "STOP":
            return True
Cassie = "Cassie"
address_book = {"CASSIE": "Los Altos", "ROBERT": "Los Altos", "TREVOR": "Mountain View", "BILLY": "Bellevue"}

print('This program allows you to store and look up people and where they live in an address book. You can stop at anytime by typing the word "stop".')
while(True):
    name = raw_input("Please enter the name of the person you would like to add or look up: ")
    if check_for_stop(name):
        break
    if name.upper() in address_book:
        print(name + " lives in " + address_book[name.upper()])
    else:
        print(name + " is not currently in your address book.")
        add_name = raw_input("Would you like to add " + name + " to your address book? (yes/no) ")
        if check_for_stop(add_name):
            break
        if add_name.upper() == "YES":
            city = raw_input("Please enter the city in which " + name + " currently lives: ")
            if check_for_stop(city):
                break
            address_book[name.upper()] = city
            print("Congratulations! " + name + ", who lives in " + city + ", has been added to your address book.")
print("The address book has been closed.")
