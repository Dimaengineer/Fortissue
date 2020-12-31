from PySide import QtCore, QtGui
import sys
from ui import Ui_Dialog
from ui2 import Ui_Dialog2


    


app = QtGui.QApplication(sys.argv)
    
Dialog = QtGui.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()

def a():
    d = float(ui.lineEdit.text())
    k = float(ui.lineEdit_3.text())
    l = float(ui.lineEdit_4.text())

    q = d * 1
    p = 1 * l
    v = q * k
    z = p / v
    m = z * 1000
    pi = round(m)
    ui.label_6.setText( str(pi) + " грн за 1кг" )

    



ui.pushButton.clicked.connect( a )


def open():
    global Dialog2
    Dialog2 = QtGui.QDialog()
    ui = Ui_Dialog2()
    ui.setupUi(Dialog2)
    Dialog2.show()
    Dialog.close()

    def n():
        c = float(ui.lineEdit.text())
        x = float(ui.lineEdit_3.text())
        r = float(ui.lineEdit_4.text())

        t = c * 1
        y = t * x
        il = 1000 / y
        f = r / il
        ut = round(f)
        ui.label_7.setText( str(ut) + " грн за 1п. м." )
        
    ui.pushButton_4.clicked.connect(n)
            


    def close():
        Dialog2.close()
        Dialog.show()
        
    ui.pushButton_3.clicked.connect(close)
    
    


 
ui.pushButton_2.clicked.connect(open)


sys.exit(app.exec_())

input("Press Enter")

    









