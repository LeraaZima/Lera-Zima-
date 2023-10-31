documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

def owner(number_doc):
    owner_name = ""
    for doc in documents:
        if number_doc == doc["number"]:
            owner_name = "Владелец документа: " + doc["name"]
    if owner_name == "":
        owner_name = "Таких нет,пока"

    return owner_name


def main():
    while True:
        user_input = input(f"введите команду: \n") 
        if user_input == 'p':
            user_num = input(f"вводи nomer \n")
            print(owner(user_num))
        elif user_input == 'q':
            break
        else:
            print("такой команды нет")
main()
    
        


