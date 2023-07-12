import os
import mysql.connector

mydb = mysql.connector.connect(
    host="Enter your Server IP here",
    user="Enter Username here",
    password="Enter Password here",
    database="Enter Database name here"
)

def Add(ad, kdvsatis, kdvalis, durum=1):
    mycursor = mydb.cursor()

    sql = "INSERT INTO TBLURUN (ad,kdvsatis,kdvalis,durum) VALUES (%s, %s, %s, %s)"
    val = (ad, kdvsatis, kdvalis, durum)
    mycursor.execute(sql, val)
    mydb.commit()


def Remove(id):
    mycursor = mydb.cursor()

    sql = "UPDATE TBLURUN SET durum=0 WHERE id=" + str(id)
    mycursor.execute(sql)

    mydb.commit()

    sql = "UPDATE TBLFIYAT SET durum = 0 WHERE uid =" + str(id)
    mycursor.execute(sql)
    mydb.commit()


def ListProduct():
    os.system('cls')
    mycursor = mydb.cursor()

    sql = "SELECT * FROM TBLURUN WHERE durum=1"
    mycursor.execute(sql)

    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def ListProducts(id):
    mycursor = mydb.cursor()

    sql = "SELECT * FROM TBLURUN WHERE durum=1 AND id="+str(id)
    mycursor.execute(sql)

    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)


def UpdateAd(id, ad):
    mycursor = mydb.cursor()

    sql = "UPDATE TBLURUN SET ad=%s WHERE id=%s"
    val = (ad, id)
    mycursor.execute(sql, val)
    mydb.commit()


def UpdateKdvSatis(id, kdvsatis):
    mycursor = mydb.cursor()

    sql = "UPDATE TBLURUN SET kdvsatis=%s WHERE id=%s"
    val = (kdvsatis, id)
    mycursor.execute(sql, val)
    mydb.commit()


def UpdateKdvAlis(id, kdvalis):
    mycursor = mydb.cursor()

    sql = "UPDATE TBLURUN SET kdvalis=%s WHERE id=%s"
    val = (kdvalis, id)
    mycursor.execute(sql, val)
    mydb.commit()


def UpdateDurum(id, durum):
    mycursor = mydb.cursor()

    sql = "UPDATE TBLURUN SET durum=%s WHERE id=%s"
    val = (durum, id)
    mycursor.execute(sql, val)
    mydb.commit()
