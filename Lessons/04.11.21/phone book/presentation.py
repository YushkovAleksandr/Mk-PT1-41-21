import business_logic as bl

# TODO implement formatter for messages 

def show_message(message):
    print(message)

def get_query(message):
    return input(message)

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

if __name__ == "__main__":
    while True:
        operation = get_query("Please select the operation (create, delete, exit):\n")
        if operation == "create":
            create_contact()
        elif operation == "delete":
            delete_contact()
        elif operation == "exit":
            break
        else:
            show_message("try again")
            continue
