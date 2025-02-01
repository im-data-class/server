import mysql.connector
import pandas as pd

dbConn = mysql.connector.connect(
    host="roundhouse.proxy.rlwy.net",
    user="root",
    password="gKMzXAztwBBbgpIclBMYSXiwTnBrtBrq",
    port="20726",
    database="railway",
)


#################################
# Create table
#################################
# cursor = dbConn.cursor()
# cursor.execute("""DROP TABLE IF EXISTS Donation;""")
# cursor.execute("""CREATE TABLE Donation (
#     id int NOT NULL AUTO_INCREMENT,
#     name varchar(255),
#     amount int NOT NULL,
#     comment varchar(255) NOT NULL DEFAULT '',
#     createdAt DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
#     updatedAt DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
#     PRIMARY KEY (id)
# );""")
# dbConn.commit()
# cursor.close()
# dbConn.close()

#################################
# Insert data
#################################
# cursor = dbConn.cursor()
# cursor.execute(
#     """INSERT INTO Donation (name, amount, comment) VALUES ('Tom', 100, 'OK');"""
# )
# dbConn.commit()
# cursor.close()
# dbConn.close()

#################################
# Read data
#################################
# cursor = dbConn.cursor()
# cursor.execute("""SELECT * FROM Donation;""")
# results = cursor.fetchall()
# df = pd.DataFrame(
#     results, columns=["id", "name", "amount", "comment", "createdAt", "updatedAt"]
# )
# df["createdAt"] = df["createdAt"].dt.strftime("%Y-%m-%d %H:%M:%S")
# df["updatedAt"] = df["updatedAt"].dt.strftime("%Y-%m-%d %H:%M:%S")
# donations = df.to_dict(orient="records")
# print(donations)
# cursor.close()
# dbConn.close()


#################################
# Modify data
#################################
# cursor = dbConn.cursor()
# cursor.execute("""UPDATE Donation SET name = 'John' WHERE id = 1;""")
# dbConn.commit()
# cursor.close()
# dbConn.close()


#################################
# Delete data (by id)
#################################
# cursor = dbConn.cursor()
# cursor.execute("""DELETE FROM Donation WHERE id = 1;""")
# dbConn.commit()
# cursor.close()
# dbConn.close()


#################################
# Delete all data
#################################
# cursor = dbConn.cursor()
# cursor.execute("""DELETE FROM Donation;""")
# dbConn.commit()
# cursor.close()
# dbConn.close()
