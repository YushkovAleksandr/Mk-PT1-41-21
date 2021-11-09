phone_book = {"id_number":("name", ["some_number", "some_number"])}
#phones_cache = {"4353": "id_number"}

def get_all_contacts():
    return [v for k, v in phone_book.items()]

def create_contact(name, *phones):
    id = len(phone_book)+1
    phone_book[id] = (name, phones)

def delete_contact(id):
    phone_book[id] = ()
    #del phone_book[id]

def change_number(id, old_number, new_number):
    delete_number(id, old_number)
    add_number(id, new_number)

def add_number(id, new_number):
    phone_book[id][1].append(new_number)

def delete_number(id, old_number):
    phone_book[id][1].remove(old_number)

def search_by_phone(query):
    for id, contact in phone_book.items():
        for number in contact[1]:
            if query == number:
                return contact[0]
    return -1

def get_id_by_name(name):
    for id, contact in phone_book.items():
        if contact[0] == name:
            return id
    return -1
