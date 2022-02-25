import storage_users

source: dict = {}

# Считывание статусов пользователя

def read_status(id):
    file_status = open(f'C:/Users/01112/PycharmProjects/my_firts_tb_bot/status_users/{id}.txt','r')
    elements_status = []
    for info in file_status:
        info_status = info.split('\n')
        diff_status = info_status[0].split()
        for i in range(1, len(diff_status)):
            elements_status.append(diff_status[i])
        source[diff_status[0]] = elements_status
        elements_status = []
    file_status.close()
    return source

# Изминения имеющегося статуса
# Например во время хода игры
def change_status(new_source, id):
    file_status = open(f'C:/Users/01112/PycharmProjects/my_firts_tb_bot/status_users/{id}.txt','w')
    for i in new_source:
        file_status.writelines(f'{i} ')
        for el_st in new_source[i]:
            file_status.writelines(f'{el_st}\n')
    file_status.close()

# Проверка статуса прошлых действий на незавершенность
def check_status(action,id):
    status = read_status(id)
    if (status[action][0] == '0'): return True
    else: return False

# Добавить нулевые статусы для всех состояний, в случае прихода нового пользователя
def new_user_status(id):
    new_source = storage_users.read_storage()
    statuses = new_source[id]
    new_dict: dict = {}
    for i in range(len(statuses)):
        new_dict[statuses[i].replace('/','')] = '0'
    change_status(new_dict,id)








