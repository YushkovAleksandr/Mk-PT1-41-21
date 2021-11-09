import business_logic as bl

def show_message(message):
    print(message)

def get_query(message):
    return input(message + ":\n")

def show_all_contacts():
    result = bl.show_all_contacts()
    show_message(result)

def create_contact():
    name = get_query("Enter new name")
    phones = get_query("Enter phones separated by comma")
    # TODO implement validation
    result, message = bl.create_contact(name, phones)
    if result:
        show_message("new contact was created")
    else:
        show_message(message)

    return result

def delete_contact():
    name = get_query("Enter a name")
    result, message = bl.delete_contact(name)
    if result:
        show_message("the contact was deleted")
    else:
        show_message(message)

    return result   

def add_number():
    name = get_query("Enter a name")
    number = get_query("Enter a new number")
    result, message = bl.add_number(name, number)
    if result:
        show_message("new number was added")
    else:
        show_message(message)

def search():
    number = get_query("Enter a number")
    result, message = bl.search(number)
    if result > 0:
        show_message(result)
    else:
        show_message(message)

if __name__ == "__main__":
    while True:
        operation = get_query("Please select the operation (show, create, delete, add number, search, exit)")
        if operation == "show":
            show_all_contacts()
        elif operation == "create":
            create_contact()
        elif operation == "delete":
            delete_contact()
        elif operation == "add number":
            add_number()
        elif operation == "search":
            search()
        elif operation == "exit":
            break
        else:
            show_message("try again")
            continue
