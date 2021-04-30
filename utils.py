import psycopg2
conn = psycopg2.connect(dbname='CompanySystem', user='postgres', 
                        password='123', host='localhost', port = '8888')
cursor = conn.cursor()


 
def printAllNames(tb, message):
	cursor.execute('SELECT * FROM airport')

	records = cursor.fetchall()
	chatid = message.chat.id
	cities = ""
	for r in records: 
		cities += f"{r[0]} | {r[1]} \n"

	tb.send_message(chatid, cities)  

def countOfUsers():
	cursor.execute('SELECT count(user_id) FROM users')
	return cursor.fetchone()[0]
def countOfQuestions():
	cursor.execute('SELECT count(question_id) FROM question')
	return cursor.fetchone()[0]
def description(general):
	cursor.execute(f'SELECT question_description FROM question WHERE question_id = {general} ORDER BY question_id')
	return cursor.fetchone()[0]
 
def addUser(user): 
    values = (countOfUsers(), user.name, user.phonenumber, user.email)
    cursor.execute(f'INSERT INTO users (user_id, user_name, user_phoneNumber, user_email) VALUES {values}')