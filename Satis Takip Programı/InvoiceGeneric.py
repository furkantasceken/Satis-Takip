import mysql.connector

mydb = mysql.connector.connect(
    host="",
    user="pyuser",
    password="user12345",
    database="mysqldb"
)

def Add(mid, tarih, tur, brut=0, kdv=0, net=0, durum=1):
    mycursor = mydb.cursor()

    sql = "INSERT INTO TBLFATURA (mid,tarih,tur,brut,kdv,net,durum) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (mid, tarih, tur, brut, kdv, net, durum)
    mycursor.execute(sql, val)
    mydb.commit()


def AddInvoiceDetail(fid,uid,miktar,brut=0,kdv=0,net=0):
    mycursor=mydb.cursor()

    sql = "INSERT INTO TBLFATURADETAY (fid,uid,miktar,brut,kdv,net) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (fid, uid, miktar, brut, kdv, net)
    mycursor.execute(sql, val)
    mydb.commit()
