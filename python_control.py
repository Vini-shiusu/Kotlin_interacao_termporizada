import os
import psutil
import time
import datetime

memoriaTotal = round(psutil.virtual_memory().total*(2**-30),2)

while True:
    # comando para select dos dados das variaveis no banco NUVEM
        sqlNuvem3 = "select memoria_total from computador"
        cursor.execute(sqlNuvem3)
        print(cursor.rowcount,"select SQL SERVER")
        print("=======================")
        time.sleep(2.0) # discretização - reduzir tamanho do dado coletado 
 time.sleep(5.0)
 if(memoriaTotal < 4.80):
  os.system("start comando1.bat")

 else:
  print(memoriaTotal)
