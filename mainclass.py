import sys
import PyQt5
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDateEdit, QFileDialog, QTableWidgetItem, QTableWidget
from first import Ui_FirstWindow
from second import Ui_RegisterWindow
from third import Ui_SigninWindow
from fourth import Ui_FourthWindow
from customerdetails import Ui_CustomerWindow
#from flightbookwindow import Ui_FlightBookWindow
from searchcustomers import Ui_SearchCustWindow
from amadeus import Client, ResponseError
from flightoptions import Ui_FlightOptionsWindow
from book import Ui_BookedWindow

class FirstWindow(QMainWindow):
    def showRegister(self):
        self.rw = RegisterWindow()
        self.rw.show()
        self.hide()

    def showsignin(self):
        self.siw = SigninWindow()
        self.siw.show()
        self.hide()
        
    def __init__(self):
        super().__init__()
        self.ui = Ui_FirstWindow()
        self.ui.setupUi(self)
        self.ui.newadminButton.clicked.connect(self.showRegister)
        self.ui.currentadminButton.clicked.connect(self.showsignin)

class RegisterWindow(QMainWindow, QMessageBox):
    def goback(self):
        self.fw = FirstWindow()
        self.fw.show()
        self.hide()

    def register(self):
        import pymysql

        fname = self.ui.FName.text()
        lname = self.ui.LName.text()
        email = self.ui.EMail.text()
        uname = self.ui.Username.text()
        pwd = self.ui.Password.text()
        telno = self.ui.Telno.text()
        print(fname,lname,email,uname,pwd,telno)
        self.db = pymysql.connect('localhost','root','webcom#123','airsys')
        self.cursor = self.db.cursor()
        sql = 'INSERT INTO admintable VALUES(%s,%s,%s,%s,%s,%s)'
        args = (fname,lname,email,uname,pwd,telno)
        self.cursor.execute(sql,args)
        self.db.commit()
        self.db.close()
        self.msg = QMessageBox()
        self.msg.setText("Your details have been saved successfully!")
        self.msg.setInformativeText("Please Go To The Current Admin Page Now!")
        #msg.setStandardButtons(QMessageBox.Ok)
        self.msg.exec_()
        self.ui.FName.setText(' ')
        self.ui.LName.setText(' ')
        self.ui.EMail.setText(' ')
        self.ui.Username.setText(' ')
        self.ui.Password.setText(' ')
        self.ui.Telno.setText(' ')
        
    def __init__(self):
        super().__init__()
        self.ui = Ui_RegisterWindow()
        self.ui.setupUi(self)
        #self.show()
        self.ui.cancelButton.clicked.connect(self.goback)
        self.ui.registerButton.clicked.connect(self.register)

class SigninWindow(QMainWindow):
    def login(self):
        import pymysql
        n = self.ui.lineEdit.text()
        p = self.ui.lineEdit_3.text()
        e = self.ui.lineEdit_2.text()
        self.db = pymysql.connect('localhost','root','webcom#123','airsys')
        self.cursor = self.db.cursor()
        sql = 'select * from admintable where email=%s'
        args = (e)
        self.cursor.execute(sql,args)
        data = self.cursor.fetchall()
        #print(data)
        if(n == data[0][3] and p == data[0][4]):
            self.fwin = fourthWindow()
            self.fwin.show()
            self.hide()
        else:
            #print("Check Details")
            self.ui.statusbar.showMessage("Check Your Details...")
            self.ui.lineEdit.setText(" ")
            self.ui.lineEdit_2.setText(" ")
            self.ui.lineEdit_3.setText(" ")

    def goback2main(self):
        self.fwa = FirstWindow()
        self.fwa.show()
        self.hide()
        
    def __init__(self):
        super().__init__()
        self.ui = Ui_SigninWindow()
        self.ui.setupUi(self)
        self.ui.signinButton.clicked.connect(self.login)
        self.ui.commandLinkButton.clicked.connect(self.goback2main)
        #self.show()

class fourthWindow(QMainWindow):
    def showcustomer(self):
        self.cdetails = CustomerDetails()
        self.cdetails.show()
        self.hide()

    def showflightbook(self):
        self.fow1 = FOWindow()
        self.fow1.show()
        self.hide()

    def cancel(self):
        self.firwin = FirstWindow()
        self.firwin.show()
        self.hide()

    def booked(self):
        self.ui = BookClass()
        self.ui.show()
        self.hide()
        
    def __init__(self):
        super().__init__()
        self.ui = Ui_FourthWindow()
        self.ui.setupUi(self)
        self.ui.commandLinkButton_3.clicked.connect(self.showflightbook)
        self.ui.commandLinkButton.clicked.connect(self.showcustomer)
        self.ui.pushButton.clicked.connect(self.cancel)
        self.ui.commandLinkButton_2.clicked.connect(self.booked)

class BookClass(QMainWindow):
    def cancelorgo(self):
        self.ui = fourthWindow()
        self.ui.show()
        self.hide()

    def loadtickets(self):
        import pymysql
        self.db = pymysql.connect('localhost','root','webcom#123','airsys')
        self.cursor = self.db.cursor()
        sql = 'SELECT Name from customertable'
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        col = 1
        sql2 = 'SELECT fromcode from firstsegment'
        self.cursor.execute(sql2)
        data2 = self.cursor.fetchall()
        sql3 = 'SELECT tocode from secondsegment'
        self.cursor.execute(sql3)
        data3 = self.cursor.fetchall()
        sql4 = 'SELECT class from secondsegment'
        self.cursor.execute(sql4)
        data4 = self.cursor.fetchall()
        sql5 = 'SELECT Price from pricetable'
        self.cursor.execute(sql5)
        data5 = self.cursor.fetchall()
        #print("Thanks1")
        self.db.close()
        col = 0
        for x in range(len(data)):
            self.ui.tableWidget.setItem(x,col, QTableWidgetItem(data[x][0]))
        col = 1
        for x in range(len(data2)):
            self.ui.tableWidget.setItem(x,col,QTableWidgetItem(data2[x][0]))
        col = 2
        for x in range(len(data3)):
            self.ui.tableWidget.setItem(x,col,QTableWidgetItem(data3[x][0]))
        col = 3
        for x in range(len(data4)):
            self.ui.tableWidget.setItem(x,col,QTableWidgetItem(data4[x][0]))
        col = 4
        for x in range(len(data5)):
            self.ui.tableWidget.setItem(x,col,QTableWidgetItem(data5[x][0]))
        self.ui.statusbar.showMessage("Tickets Loaded...")
        
        
    def emailit(self):
        import smtplib
        x = self.ui.lineEdit.text()
        #content['subject'] = "Your Travel Ticket!"
        content = "Your Travel Ticket!!\nPlease check all the details carefuly."
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login('pyappmedia@gmail.com','pythonmultimediaapp2018')
        mail.sendmail('pyappmedia@gmail.com',x,content)
        mail.close()
        self.ui.statusbar.showMessage("Ticket Sent. Please Check Your Inbox!")
        
    def __init__(self):
        super().__init__()
        self.ui = Ui_BookedWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.loadtickets)
        self.ui.pushButton_2.clicked.connect(self.cancelorgo)
        self.ui.commandLinkButton.clicked.connect(self.emailit)
        
        
class CustomerDetails(QMainWindow):
    def getnsave(self):
        import pymysql
        custname = self.ui.cname.text()
        custid = self.ui.cid.text()
        custfather = self.ui.fathername.text()
        de = self.ui.dateEdit.date()
        pyde = de.toPyDate()
        pn = self.ui.phonenumber.text()
        custaddr = self.ui.address.toPlainText()
        self.db = pymysql.connect('localhost','root','webcom#123','airsys')
        self.cursor = self.db.cursor()
        sql = "INSERT INTO customertable VALUES(%s,%s,%s,%s,%s,%s)"
        args = (custname,custid,custfather,pyde,pn,custaddr)
        self.cursor.execute(sql,args)
        self.db.commit()
        self.db.close()
        self.ui.statusbar.showMessage("Customer Details Added Successfully!")
          
    def showfourth(self):
        self.fourthwin2 = fourthWindow()
        self.fourthwin2.show()
        self.hide()

    def getimg(self):
        fd = QFileDialog.getOpenFileName(self,"Select Customer's Image","","*.jpg")
        pm = QPixmap(fd[0])
        self.ui.label_2.setPixmap(pm)

    def loadCustomers(self):
        self.scw = SearchCustomers()
        #self.scw.show()
        #self.hide()
        
        import pymysql

        self.db = pymysql.connect('localhost','root','webcom#123','airsys')
        self.cursor = self.db.cursor()
        sql = "SELECT * FROM customertable"
        ####Database Code Here...
        self.scw.show()
        self.hide()
        
    def __init__(self):
        super().__init__()
        self.ui = Ui_CustomerWindow()
        self.ui.setupUi(self)
        
        self.ui.cancelbutton.clicked.connect(self.showfourth)
        self.ui.submitbutton.clicked.connect(self.getnsave)
        self.ui.imagebutton.clicked.connect(self.getimg)
        self.ui.actionShow_Customers.triggered.connect(self.loadCustomers)

class FOWindow(QMainWindow):
    def cancel(self):
        self.win4 = fourthWindow()
        self.win4.show()
        self.hide()
        
    def searchflights(self):
        de = self.ui.dateEdit.date()
        pyde1 = de.toPyDate()
        pyde = pyde1.strftime("%Y-%m-%d")
        #print(pyde)
        cb1 = self.ui.comboBox.currentText()
        print(cb1)
        cb2 = self.ui.comboBox_2.currentText()
        print(cb2)
        #cb3 = self.ui.comboBox_3.currentText()
        #from amadeus import Client, ResponseError
        self.ui.statusbar.showMessage("Please Wait While Results Are Fetched...")
        try:
            amadeus = Client(client_id = 'njhEkI3GnugdZbdV7HQ4snGzmsIkHbwr', client_secret = 'pozG8ritKpbs4Mq3')
            response = amadeus.shopping.flight_offers.get(origin= cb1, destination= cb2, departureDate=str(pyde))
            l1 = []
            l2 = []
            l3 = []
            l4 = []
            l5 = []
            l6 = []
            l7 = []
            l8 = []
            l9 = []
            l10 = []
            for a in response.data:
                departure1stfrom = (a['offerItems'][0]['services'][0]['segments'][0]['flightSegment']['departure']['iataCode'])
                l1 += [departure1stfrom]
            #print(l1)
            print(len(l1))
            for a in response.data:
                departure1sttime = (a['offerItems'][0]['services'][0]['segments'][0]['flightSegment']['departure']['at'])
                l2 += [departure1sttime]
            #print(l2)
            #listnew = list(zip(l1,l2))
            #print(listnew)
            for a in response.data:
                arrival1stat = (a['offerItems'][0]['services'][0]['segments'][0]['flightSegment']['arrival']['iataCode'])
                l3 += [arrival1stat]
            #print(l3)
            ##print(listnew2)
            for a in response.data:
                arrival1sttime = (a['offerItems'][0]['services'][0]['segments'][0]['flightSegment']['arrival']['at'])
                l4 += [arrival1sttime]
            #print(l4)
            for a in response.data:
                aircraft1st = (a['offerItems'][0]['services'][0]['segments'][0]['flightSegment']['aircraft']['code'])
                l5 += [aircraft1st]
            #print(l5)
            for a in response.data:
                firsttravelClass = (a['offerItems'][0]['services'][0]['segments'][0]['pricingDetailPerAdult']['travelClass'])
                l6 += [firsttravelClass]
            #print(l6)
            for a in response.data:
                departure2ndfrom = (a['offerItems'][0]['services'][0]['segments'][1]['flightSegment']['departure']['iataCode'])
                l7 += [departure2ndfrom]
            #print(l7)
            for a in response.data:
                departure2ndtime = (a['offerItems'][0]['services'][0]['segments'][1]['flightSegment']['departure']['at'])
                l8 += [departure2ndtime]
            #print(l8)
            for a in response.data:
                arrival2ndat = (a['offerItems'][0]['services'][0]['segments'][1]['flightSegment']['arrival']['iataCode'])
                l9 += [arrival2ndat]
            #print(l9)
            for a in response.data:
                arrival2ndtime = (a['offerItems'][0]['services'][0]['segments'][1]['flightSegment']['arrival']['at'])
                l10 += [arrival2ndtime]
            #print(l10)
            l11 = []
            for a in response.data:
                aircraft2nd = (a['offerItems'][0]['services'][0]['segments'][1]['flightSegment']['aircraft']['code'])
                l11 += [aircraft2nd]
            #print(l11)
            l12 = []
            for a in response.data:
                secondtravelClass = (a['offerItems'][0]['services'][0]['segments'][1]['pricingDetailPerAdult']['travelClass'])
                l12 += [secondtravelClass]
            #print(l12)
            l13 = []
            for a in response.data:
                availability = (a['offerItems'][0]['services'][0]['segments'][0]['pricingDetailPerAdult']['availability'])
                l13 += [availability]
            #print(l13)
            l14 = []
            for a in response.data:
                prices = a['offerItems'][0]['pricePerAdult']['total']
                l14 += [prices]            
            for x in range(len(l14)):
                self.pricelist.append(l14[x])
            #print(self.pricelist)
        except ResponseError as error:
            print(error)
        self.ui.statusbar.showMessage("Please wait while First Segment is loaded...")
        #print(l1)
        col = 0
        for row in range(len(l1)):
            self.ui.tableWidget.setItem(row,col,QTableWidgetItem(l1[row]))
        col = 1
        for row in range(len(l2)):
            self.ui.tableWidget.setItem(row,col,QTableWidgetItem(l2[row]))
        col = 2
        for row in range(len(l3)):
            self.ui.tableWidget.setItem(row,col,QTableWidgetItem(l3[row]))
        col = 3
        for row in range(len(l4)):
            self.ui.tableWidget.setItem(row,col,QTableWidgetItem(l4[row]))
        col = 4
        for row in range(len(l5)):
            self.ui.tableWidget.setItem(row,col,QTableWidgetItem(l5[row]))
        col = 5
        for row in range(len(l6)):
            self.ui.tableWidget.setItem(row,col,QTableWidgetItem(l6[row]))
        #col = 6
        #self.ui.statusbar.showMessage("Load Done.")
        self.ui.statusbar.showMessage("Please wait while Second Segment is loaded...")
        #print(l1)
        col = 0
        for row in range(len(l7)):
            self.ui.tableWidget_2.setItem(row,col,QTableWidgetItem(l7[row]))
        col = 1
        for row in range(len(l8)):
            self.ui.tableWidget_2.setItem(row,col,QTableWidgetItem(l8[row]))
        col = 2
        for row in range(len(l9)):
            self.ui.tableWidget_2.setItem(row,col,QTableWidgetItem(l9[row]))
        col = 3
        for row in range(len(l10)):
            self.ui.tableWidget_2.setItem(row,col,QTableWidgetItem(l10[row]))
        col = 4
        for row in range(len(l11)):
            self.ui.tableWidget_2.setItem(row,col,QTableWidgetItem(l11[row]))
        col = 5
        for row in range(len(l12)):
            self.ui.tableWidget_2.setItem(row,col,QTableWidgetItem(l12[row]))
        #col = 6
        self.ui.statusbar.showMessage("Load Done.")
        
    def fetch(self):
        items1 = self.ui.tableWidget.selectionModel().selectedIndexes()
        for a in range(len(items1)):
            self.listA.append(items1[a].data())
        
    def fetch2(self):
        items2 = self.ui.tableWidget_2.selectionModel().selectedIndexes()
        for a in range(len(items2)):
            self.listB.append((items2[a].data()))
               
    def book(self):
        #print("First Segment: ",self.listA)
        #print("Second Segment: ",self.listB)
        self.msg = QMessageBox()
        self.msg.setWindowTitle("Final Flight Save Confirmation!!!")
        self.msg.setText("Want To Confirm and Save The Selected Iternary?")
        self.msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)      
        reply = self.msg.exec_()
        if reply == QMessageBox.Ok:
            self.saveflight()
        else:
            self.cancelflight()

    def saveflight(self):
        import pymysql
        self.db = pymysql.connect('localhost','root','webcom#123','airsys')
        self.cursor = self.db.cursor()
        sql1 = 'INSERT INTO firstsegment VALUES(%s,%s,%s,%s,%s,%s)'
        args1 = (self.listA[0],self.listA[1],self.listA[2],self.listA[3],self.listA[4],self.listA[5])
        self.cursor.execute(sql1,args1)
        #self.db.commit()
        #print("Going Good")
        sql2 = 'INSERT INTO secondsegment VALUES(%s,%s,%s,%s,%s,%s)'
        args2 = (self.listB[0],self.listB[1],self.listB[2],self.listB[3],self.listB[4],self.listB[5])
        #print("Here")
        self.cursor.execute(sql2,args2)
        sql3 = 'INSERT INTO pricetable VALUES(%s)'
        args3 = [
            (self.pricelist[0]),
            (self.pricelist[1]),
            (self.pricelist[2]),
            (self.pricelist[3]),
            (self.pricelist[4]),
            (self.pricelist[5]),
            (self.pricelist[6]),
            (self.pricelist[7]),
            (self.pricelist[8]),
            (self.pricelist[9]),
            (self.pricelist[10])
            ]
        self.cursor.executemany(sql3,args3)
        self.db.commit()
        self.db.close()
        #print("Going Good")
        self.ui.statusbar.showMessage("Iternary Saved... Please Go To Customers Window To Enter Passenger Details...")


    def cancelflight(self):
        print("Thanks")
        
    def __init__(self):
        super().__init__()
        self.ui = Ui_FlightOptionsWindow()
        self.ui.setupUi(self)
        self.listA = []
        self.listB = []
        self.pricelist = []
        self.ui.pushButton_2.clicked.connect(self.cancel)
        self.ui.pushButton_3.clicked.connect(self.searchflights)
        self.ui.tableWidget.clicked.connect(self.fetch)
        self.ui.tableWidget_2.clicked.connect(self.fetch2)
        self.ui.pushButton.clicked.connect(self.book)

class SearchCustomers(QMainWindow):
    def showfourthW(self):
        self.sfw = fourthWindow()
        self.sfw.show()
        self.hide()
        
    def __init__(self):
        super().__init__()
        self.ui = Ui_SearchCustWindow()
        self.ui.setupUi(self)
        self.ui.actionGo_Back_To_Main_Window.triggered.connect(self.showfourthW)

class MainClass:
    def __init__(self):
        pass

    def showFirst(self):
        self.first = FirstWindow()
        self.first.show()

    
    
def main():
    app = QApplication(sys.argv)
    mc = MainClass()
    mc.showFirst()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
