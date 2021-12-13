import pyodbc
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from syf6 import *
global crs
global conn


conn = pyodbc.connect(
       "Driver={SQL Server Native Client 11.0};"
       "Server=HASAN\SQLEXPRESS1;"
       "Database=verx;"
       "Trusted_Connection=yes;"
    )




def ekle():
       
    l1=ui.lineEdit.text()
   
    l2=ui.lineEdit_2.text()
    l3=int(ui.lineEdit_3.text())
    l4=str(ui.dateEdit.date().toString(QtCore.Qt.ISODate))
        
    
    try:
        #crs.execute("select * from tabl0")

        komut = 'INSERT INTO tabl0 VALUES(?,?,?,?)'
        veriler = (l1,l2,l3,l4)
        sonuc = crs.execute(komut,veriler)

      
        crs.commit()
        
        print('olduu')
    except:
        print('başarısız')
    
def lst():
    ui.tableWidget.clear()
    ui.tableWidget.setHorizontalHeaderLabels(('ADI','SOYADI','telefon','tarih'))
    ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)         
    crs.execute('select  * from tabl0 order by adx desc')
       
    for stri,strvr in enumerate(crs):
        for suti,sutver in enumerate(strvr):
            ui.tableWidget.setItem(stri,suti,QTableWidgetItem(str(sutver)))
    
      

uyg=QApplication(sys.argv)
penAna=QMainWindow()
ui=Ui_MainWindow()
ui.setupUi(penAna)
penAna.show()







crs=conn.cursor()
#◙lst()
ui.pushButton.clicked.connect(ekle)
ui.pushButton_2.clicked.connect(lst)




