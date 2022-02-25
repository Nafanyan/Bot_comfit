from storage_users import*
import work_status_users as wsu

def start(update, context):
    id = str(update.effective_user.id)
    output_str = ''
    user_base = read_storage()
    if (not (id in user_base)):
        add_new_user(id)
        wsu.new_user_status(id)
    for i in user_base[id]:
        output_str += f'{i}\n'
    update.message.reply_text(f'Приветствую! \nВот список команд, доступный для использования:\n{output_str}')