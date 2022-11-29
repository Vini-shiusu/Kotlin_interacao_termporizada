import os
import psutil
import time
import pyodbc
import mysql.connector

memoriaTotal = round(psutil.virtual_memory().total*(2**-30),2)

while True:
    server = 'turi.database.windows.net'
    database = 'Turi'
    username = 'adm-turi'
    password = 'Urubu1002'
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server +
                        ';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD=' + password)
    cursor = cnxn.cursor()

    #try:
     #   con = mysql.connector.connect(
      #      host='localhost', user='root', password='', database='Turi') # coloque a senha do seu mysql
       # print("Conexão ao banco estabelecida!")                          # o localhost pode ser o ip do seu docker, atenção
   # except mysql.connector.Error as error:
    #    if error.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
     #       print("Erro: Database não existe")
      #  elif error.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
       #     print("Erro: Nome ou senha incorretos")
        #else:
         #   print(error)
    #cursorLocal = con.cursor()
        
    # comando para select dos dados das variaveis no banco NUVEM
    res = cursor.execute("select resposta from respostaOcio order by id desc;")
    row = cursor.fetchone() 
    print(row[0])
    print("memoria atual:", memoriaTotal)
    print("=======================")
 # discretização - reduzir tamanho do dado coletado 
    time.sleep(5.0)
    if(memoriaTotal < 8.80):
        os.system("start comando1.bat")

    if(row[0] == 0):
        print("oi")
        #os.system("shutdown -h")

