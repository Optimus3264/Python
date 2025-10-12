import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user = 'root',
    password='kavya@28',
    database='game_store',
)

#print('Database connected')

cursor = conn.cursor()
#create table user
#cursor.execute("""CREATE TABLE IF NOT EXISTS users (
 #       id INT,
  #      name VARCHAR(100),
   #     email VARCHAR(100),
    #    phone VARCHAR(100)
#   )
#""")
#print('Table Users created')


#create table games
#cursor.execute("""CREATE TABLE IF NOT EXISTS games(
        #game_id int,
        #title varchar(100),
        #genre varchar(100),
        #price varchar(100),
        #stock varchar(100)


#)
#""")

#print("table games created")

#cursor.execute("insert into users (id, name, email, phone) values (%s,%s,%s,%s)" , ("1","rushi","abc@gmail.com","9850123123" ))
#cursor.execute("SELECT*FROM users")
#for row in cursor.fetchall():
 #   print(row)


#cursor.execute("insert into users (id, name, email, phone) values (%s,%s,%s,%s)" , ("2","bhhushan","xyz@gmail.com","9850123152" ))
#cursor.execute("SELECT*FROM users")
#for row in cursor.fetchall():
 #  print(row)

data =[
    ("1","cs","action","100","10"),
    ("2","fifa","sport","200","15"),
    ("3","mk4","fight","80","8")
]

query= "INSERT INTO games (game_id ,title ,genre,price ,stock) VALUES (%s,%s,%s,%s,%s)"
cursor.executemany(query,data)

cursor.execute("select * from games")
for row in cursor.fetchall():
    print(row)




