import telebot
from telebot import types
import utils
import user
import csvload

numOfQuestions = utils.countOfQuestions()
tb = telebot.TeleBot('1305724214:AAHQ_G-_ztkUW2xLMMz6vO8HBWLhPP7nFX0')      

commands = ['help', 'start', 'test']
admincmd = ['remove']
ADMIN_ID = 902287112
general = 0
user1 = user.User("null", "null", "null")

test = user.Test("null", "null")
@tb.message_handler(commands=[commands[2]])
def test(message):
	if user1.name == "null":
		tb.send_message(message.chat.id, "Для начала введите /start комманду!")
	else:
		tb.send_message(message.chat.id, "Итак, теперь анкетированный тест:")
		tb.send_message(message.chat.id, "Напишите немного о себе")
		tb.register_next_step_handler(message, testuser)
	 
def testuser(message):
	test.description = message.text
	tb.send_message(message.chat.id, "И к концу скиньте ссылку на linkiedin/github")
	tb.register_next_step_handler(message, link) 
def link(message):
	test.test_link = message.text
	utils.addtest(test, user1)
	tb.send_message(message.chat.id, "Спасибо за внимание")
	csvload.createCSVFile(utils.listOfTests())
	
@tb.message_handler(commands=[commands[0]])
def start(message):
	str = ""
	if ADMIN_ID == 902287111:
		for command in admincmd:
			str += "/" + command + '\n'
	else:
		for command in commands:
			str += "/" + command + '\n' 
	tb.send_message(message.chat.id, f"Список комманд: \n{str}")


@tb.message_handler(commands=[admincmd[0]])
def remove(message):
	tb.send_message(message.chat.id, "Введите id человека, которого хотите удалить")
	tb.register_next_step_handler(message, deleteUser)
def deleteUser(message):
	if message.chat.id == ADMIN_ID:
		try:
			utils.deleteUser(int(message.text))
			tb.send_message(message.chat.id, "Человек успешно удален!")
		except:
			tb.send_message("Введенный текст не соответствует id!")
@tb.message_handler(commands=[commands[1]])
def addUser(message):
	tb.send_message(message.chat.id, "Введите имя юсера:" )
	tb.register_next_step_handler(message, add)
def add(message):
	tb.send_message(message.chat.id, "Введите номер телефона юсера:")
	user1.name = message.text
	tb.register_next_step_handler(message, adduserTelephone)
def adduserTelephone(message):
	tb.send_message(message.chat.id, "Введите email юсера:")
	user1.phonenumber = message.text
	tb.register_next_step_handler(message, adduserEmail)
def adduserEmail(message):
	user1.email = message.text
	try:
		utils.addUser(user1)
		tb.send_message(message.chat.id, "Успешно! юсер был залит в базу!")
		tb.send_message(message.chat.id, "Напишите комманду /test для продолжения!")
	except:
		tb.send_message(message.chat.id, "Человек создан или возникла техническая ошибка!") 

@tb.message_handler(func=lambda message: True, content_types=['text'])
def checkdata(message):
	str = ""
	for command in commands:
		str += "/" + command + '\n'
	tb.send_message(message.chat.id, f"Напишите комманду /{commands[0]} чтобы посмотреть все комманды! {message.chat.id}") 
	
 
@tb.callback_query_handler(func=lambda call: True)
def send_rus_trans(message):
	start_markup = tb.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False) #Return to start keyboard
	start_markup.row('/start', '/help', '/hide') 

tb.polling() 
#Use none_stop flag let polling will not stop when get new message occur error.
tb.polling(none_stop=True)
# Interval setup. Sleep 3 secs between request new message.
tb.polling(interval=3)

# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
tb.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
tb.load_next_step_handlers()
while True: # Don't let the main Thread end.
    pass

 