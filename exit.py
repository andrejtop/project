random_task = ['Выпить стакан воды', 'Сделать 10 приседаний', "Сделать 10 отжиманий", "Перекусить"]
HELP = """
/help - показать доступные команды.
/add - добавить задачу в список (название задачи запрашиваем у пользователя).
/show - напечатать все добавленные задачи.
/random - добавить случайную задачу на Сегодня.
/exit"""
tasks = {}
def ad_todo(date, task):
  if date in tasks:
    tasks[date].append(task)
  else:
    tasks[date] = []
    tasks[date].append(task)


@bot.message_handler(commands = ["help"])
def help(message):
  bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands = ["add"])
def add(message):
    command = message.text.split(maxsplit=2)
    date = command[1].lower()
    task = command[2]
    if len(task) < 3:
        bot.send_message(message.chat.id, 'Задачи должны быть больше 3х символов')
    ad_todo(date, task)
    text = f"Задача {task} добавлена на дату {date}"
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands = ["random"])
def add_random(message):
    date = "сегодня"
    task = random.choice(random_task)
    ad_todo(date, task)
    text = f"Задача {task} добавлена на дату {date}"
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands = ["show", "print"])
def show(message):
    command = message.text.split(maxsplit=1)
    date = command[1].lower()
    text = ""
    if date in tasks:
        text = date.upper() + "\n"
        for task in tasks[date]:
            text = text + "- " + task + "\n"
    else:
        text = "Задач на эту дату нет"
    bot.send_message(message.chat.id, text)