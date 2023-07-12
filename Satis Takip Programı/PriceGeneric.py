import os
import mysql.connector

mydb = mysql.connector.connect(
    host="Enter your Server IP here",
    user="Enter Username here",
    password="Enter Password here",
    database="Enter Database name here"
)

def Add(uid, fiyatsatis, fiyatalis, durum=1):
    mycursor = mydb.cursor()

    sql = "INSERT INTO TBLFIYAT (uid,fiyatsatis,fiyatalis,durum) VALUES (%s, %s, %s, %s)"
    val = (uid, fiyatsatis, fiyatalis,durum)
    mycursor.execute(sql, val)
    mydb.commit()


def Remove(id):
    mycursor = mydb.cursor()

    sql = "DELETE FROM TBLFIYAT WHERE uid =" + str(id)
    mycursor.execute(sql)
    mydb.commit()


def ListProduct():
    os.system('cls')
    mycursor = mydb.cursor()

    sql = "SELECT U.id,U.ad,F.fiyatalis,F.fiyatsatis, CASE F.durum WHEN '1' THEN 'AKTİF' ELSE 'PASİF' END Durum FROM TBLURUN U INNER JOIN TBLFIYAT F ON U.id=F.uid"
    mycursor.execute(sql)

    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def ListProducts(id):
    mycursor = mydb.cursor()

    sql = "SELECT U.id,U.ad,F.fiyatalis,F.fiyatsatis FROM TBLURUN U INNER JOIN TBLFIYAT F ON U.id=F.uid WHERE F.durum=1 AND f.uid="+str(id)
    mycursor.execute(sql)

    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)


def UpdateUid(id, uid):
    mycursor = mydb.cursor()

    sql = "UPDATE TBLFIYAT SET uid=%s WHERE id=%s"
    val = (uid, id)
    mycursor.execute(sql, val)
    mydb.commit()


def UpdateFiyatSatis(id, fiyatsatis):
    mycursor = mydb.cursor()

    sql = "UPDATE TBLFIYAT SET fiyatsatis=%s WHERE uid=%s"
    val = (fiyatsatis, id)
    mycursor.execute(sql, val)
    mydb.commit()


def UpdateFiyatAlis(id, fiyatalis):
    mycursor = mydb.cursor()

    sql = "UPDATE TBLFIYAT SET fiyatalis=%s WHERE uid=%s"
    val = (fiyatalis, id)
    mycursor.execute(sql, val)
    mydb.commit()


def UpdateDurum(id, durum):
    mycursor = mydb.cursor()

    sql = "UPDATE TBLFIYAT SET durum=%s WHERE uid=%s"
    val = (durum, id)
    mycursor.execute(sql, val)
    mydb.commit()
