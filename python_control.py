import os
import psutil
import time
import pyodbc

#memoriaTotal = round(psutil.virtual_memory().total*(2**-30),2)


while True:
    server = 'turi.database.windows.net'
    database = 'Turi'
    username = 'adm-turi'
    password = 'Urubu1002'
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server +
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

    sqlNuvem001 = "select resposta from respostaOcio order by id desc;"
    cursor.execute(sqlNuvem001)
    row = cursor.fetchone()

    print("Capturando a memoria do seu caixa")
    print("aguarde")
    memoriaTotal = round(psutil.virtual_memory()[2], 2)
    time.sleep(3.0)
    print("memoria RAM ultilizada no momento:", memoriaTotal)
    print("=======================")

    row[-1] = 0
 # discretização - reduzir tamanho do dado coletado 
    time.sleep(5.0)
    if(memoriaTotal < 65.0):
        print("Ociosidade ")
        time.sleep(30.0)
        os.system("start comando1.bat")
        cursor.execute(sqlNuvem001)
        row = cursor.fetchone()
        

        if(row[-1] != 1):
           print("Colocando o caixa em modo de hibernação")
           #os.system("shutdown -h")
        else:
         print("retornar")

