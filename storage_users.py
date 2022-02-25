# Модуль для работы с файлом в котором хранится id пользователя и список доступных ему команд


users_rights: dict = {}
users_actions = ['/sweet','/help','/hello']

# Считать данные всех пользователей с хранилища
def read_storage():
    info = open('storage_users.txt','r')
    for data in info:
        data_list = data.split()
        list_action = []
        for i in range(1,len(data_list)):
            list_action.append(data_list[i])
        users_rights[data_list[0]] = list_action
    info.close()
    return users_rights

# Добавить нового пользователя в хранилище
def add_new_user(id):
    info = open('storage_users.txt','a')
    info.writelines(f'\n{id} ')
    for i in users_actions:
        info.writelines(f'{i} ')
    info.close()

