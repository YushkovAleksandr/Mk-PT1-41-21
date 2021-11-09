import data

def show_all_contacts():
    contacts = data.get_all_contacts()
    res = []
    for contact in contacts:
        res.append(f"{contact[0]}:{str.join(',', contact[1])}")
    return str.join('\n', res)

def create_contact(name, phones):
    data.create_contact(name, *phones.split(','))
    return 1,1

def delete_contact(name):
    id = data.get_id_by_name(name)
    if id >= 0:
        data.delete_contact(id)
    else:
        return -1, "there is no such name in the book"

    return id, ""

def add_number(name, number):
    id = data.get_id_by_name(name)
    if id >= 0:
        data.add_number(id, number)
    else:
        return -1, "there is no such name in the book"

    return id, ""

def search(number):
    res = data.search_by_phone(number)
    if res:
        return res, ""
    else:
        return -1, "there is no such number in the book"