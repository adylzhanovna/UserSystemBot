import psycopg2
conn = psycopg2.connect(dbname='CompanySystem', user='postgres', 
                        password='123', host='localhost', port = '8888')
cursor = conn.cursor()
conn.autocommit = True

 
def printAllNames(tb, message):
	cursor.execute('SELECT * FROM airport')

	records = cursor.fetchall()
	chatid = message.chat.id
	cities = ""
	for r in records: 
		cities += f"{r[0]} | {r[1]} \n"

	tb.send_message(chatid, cities)  
 
def getUserName(userid):
	cursor.execute(f"SELECT user_name FROM users WHERE user_id = '" + f"{userid}" + "'")
	return cursor.fetchone()[0]
def getUserId(username):
	cursor.execute(f"SELECT user_id FROM users WHERE user_name = '" + f"{username}" + "'")
	return cursor.fetchone()[0]
def countOfUsers():
	cursor.execute('SELECT count(user_id) FROM users')
	return cursor.fetchone()[0]
def countOfQuestions():
	cursor.execute('SELECT count(question_id) FROM question')
	return cursor.fetchone()[0]
def description(general):
	cursor.execute(f'SELECT question_description FROM question WHERE question_id = {general} ORDER BY question_id')
	return cursor.fetchone()[0]
def addUser(employee):  
    cursor.execute(f"INSERT INTO users (user_id, user_name, user_phoneNumber, user_email) VALUES ({countOfUsers()+4}," + f"'{employee.name}'," + f"'{employee.phonenumber}'," + f"'{employee.email}')")
def deleteUser(id):
	cursor.execute(f"DELETE FROM users WHERE user_id = {id}")
def addtest(test, employee):  
    cursor.execute(f"INSERT INTO tests VALUES ({countOfUsers()}," + f"'{test.description}'," + f"'{test.test_link}'," + f"'{getUserId(employee.name)}')")

def listOfTests():
	cursor.execute('SELECT * FROM tests')
	data_list = [["UserId", "Description", "Link"]]
	records = cursor.fetchall()
	for r in records:
		print(int(r[3]))
		data_list += [[f"{getUserName(int(r[3]))}", f"{r[1]}", f"{r[2]}"]]
	return data_list