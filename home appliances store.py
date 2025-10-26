import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user = 'root',
    password='kavya@28',
    database='home_appliances'
)

#print ('database.connector')

cursor = conn.cursor()
#create table categories
#cursor.execute("""CREATE TABLE IF NOT EXISTS categories (
   # categoryID int,
  #  catrgory_name varchar (100) not null,
  #  description varchar(255)
 #  )
#""")

#print ('category table created')

#create table products
#cursor.execute(""" create table if not exists products(
#productID int,
#productName varchar(255) not null,
#categoryID int,
#brand varchar(100),
#modelNumber varchar(50),
#price decimal(10,2) not null,
#stockQuantity int default 0,
#description text,
#imageURL varchar(255),
#supplierID int
#)
#""")

#print('products table created')


#create table customers
#cursor.execute(""" create table if not exists customers(
 #   customerID int,
  #  fullname varchar(255),
   # email varchar(100),
    #phonenumber varchar(15),
    #address TEXT,
    #city varchar(100),
    #state varchar(100),
   # ziocode varchar(20),
    #country varchar(100),
    #passwordHash varchar(255) not null
#)
#""")

#print('customers table created')

#create table orders
#cursor.execute("""create table If not exists orders(
#orderID int,
#customerID int,
#orderDate VARCHAR(100),
#totalAmount INT,
#orderStatus VARCHAR(100),
#paymentStatus VARCHAR(100), 
#shippingAddress VARCHAR(100)
#)
#""")
#print('orders table is created')

#create table order_details
#cursor.execute("""create table If not exists orders_details(
 #   orderdetailID int,
  #  orderId int,
   # productId int,
   # quantity int,
   # price varchar(100),
   # total_price varchar(100)
#)
#""")

#print('order_details table created')

#create table payment 
#cursor.execute = ("""create table if not exists payment(
#paymentId int ,
#orderID int,
#paymentmethod varchar(100),
#paymentdate DATETIME default current_timestamp,
#amount varchar(100),
#transcriptionID varchar(100) unique
#)
#""")
#print('payment table created')

#cursor.execute=("""create table suppliers if not exists(
#supplierID int,
#supplierName varchar(255),
#contactPerson varchar(255),
#Email varchar(100),
#PhoneNumber varchar(15),
#Address TEXT,
#City varchar(100),
#Country(100)
#)
#""")

#print('suppliers table created')

cursor.execute("""create table Reviews(
ReviewID int,
ProductID int,
CustomerID int,
Rating int,
Review varchar(100),
ReviewDate varchar(100)
)
""")

print('Reviews Table crated')