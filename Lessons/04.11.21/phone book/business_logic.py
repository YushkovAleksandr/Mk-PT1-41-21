import data

def create_contact(name, phones):
    data.create_contact(name, phones.split(','))
    return 1,1

def delete_contact(name):
    id = data.get_id_by_name(name)
    if id >= 0:
        data.delete_contact(id)
    else:
        return -1, "there is no such name in the book"

    return id, ""
