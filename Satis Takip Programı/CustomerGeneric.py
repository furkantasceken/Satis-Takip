import os
import mysql.connector

mydb = mysql.connector.connect(
    host="Enter your Server IP here",
    user="Enter Username here",
    password="Enter Password here",
    database="Enter Database name here"
)

def Add(unvan, tcvn, durum=1):
    mycursor = mydb.cursor()

    sql = "INSERT INTO TBLMUSTERI (unvan,tcvn,durum) VALUES (%s, %s, %s)"
    val = (unvan, tcvn, durum)
    mycursor.execute(sql, val)
    mydb.commit()


def Remove(id):
    mycursor = mydb.cursor()

    sql = "UPDATE TBLMUSTERI SET durum = 0 WHERE id =" + str(id)
    mycursor.execute(sql)
    mydb.commit()


def ListProduct():
    os.system('cls')
    mycursor = mydb.cursor()

    sql = "SELECT * FROM TBLMUSTERI WHERE durum=1"
    mycursor.execute(sql)

    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def ListProducts(id):
    mycursor = mydb.cursor()

    sql = "SELECT * FROM TBLMUSTERI WHERE durum=1 AND id="+str(id)
    mycursor.execute(sql)

    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def UpdateUnvan(id, unvan):
    mycursor = mydb.cursor()

    sql = "UPDATE TBLMUSTERI SET unvan=%s WHERE id=%s"
    val = (unvan, id)
    mycursor.execute(sql, val)
    mydb.commit()


def UpdateTcvn(id, tcvn):
    mycursor = mydb.cursor()

    sql = "UPDATE TBLMUSTERI SET tcvn=%s WHERE id=%s"
    val = (tcvn, id)
    mycursor.execute(sql, val)
    mydb.commit()


def UpdateDurum(id, durum):
    mycursor = mydb.cursor()

    sql = "UPDATE TBLMUSTERI SET durum=%s WHERE id=%s"
    val = (durum, id)
    mycursor.execute(sql, val)
    mydb.commit()
