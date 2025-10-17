import mysql.connector

mydb = mysql.connector.connect(
    host = "root",
    user = "root",
    password = "root",
    database = "alx_book_store"
)

mycursor = mydb.mycursor

mycursor.execute("""
    CREATE TABLE IF NOT EXISTS Books(
    book_id (PRIMARY_KEY),
    title VARCHAR (130),
    FOREIGN KEY (author_id) REFERENCES Authors Table(author_id),
    price DOUBLE,
    publication_date DATE)
""");

print("Successfully created Books Table.")

mycursor.execute("""
    CREATE TABLE IF NOT EXISTS Authors(
    author_id PRIMARY KEY,
    customer_name VARCHAR(215),
    email VARCHAR(215),
    address TEXT)
""");
print("Successfully created the Authors Table.")

mycursor.execute("""
    CREATE TABLE IF NOT EXISTS Customers(
    customer_id PRIMARY KEY,
    customer_name VARCHAR(215),
    email VARCHAR(215),
    address TEXT)
""");
print("Successfully created the Customers Table.")

mycursor.execute("""
    CREATE TABLE IF NOT EXISTS Orders(
    order_id PRIMARY KEY),
    customer_id FOREIGN KEY REFERENCES Customers(customer_id),
    order_date DATE
""");
print("Successfully created Orders Table.")

mycursor.execute("""
    CREATE TABLE IF NOT EXISTS Order_Details(
    orderdetailid PRIMARY KEY),
    order_id FOREIGN KEY REFERENCES Orders(order_id),
    book_id FOREIGN KEY REFERENCES Books(book_id),
    quantity DOUBLE
""");
print("Succesfully created the Orders_Details Table.")