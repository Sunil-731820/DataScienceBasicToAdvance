import  mysql.connector

myDb = mysql.connector.connect(
    host= 'localhost',
    user = 'root',
    password = 'root',
    port = 3306,
    database = "python_userdata"
)

myCursor = myDb.cursor()
myCursor.execute('select *from python_user_data')
users = myCursor.fetchall()
for user in users:
    print(user)
