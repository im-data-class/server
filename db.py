import mysql.connector


mydb = mysql.connector.connect(
    host="autorack.proxy.rlwy.net",
    user="root",
    password="SZbaEeOIWDmDAwbijBuTEIhGeYrymmUP",
    port="26815",
    database="railway",
)

mycursor = mydb.cursor()

mycursor.execute("""CREATE TABLE Persons (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);""")
