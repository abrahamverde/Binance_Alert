from sys import setswitchinterval
from PyQt5 import QtCore, QtGui, QtWidgets
from BinanceClasses import *
from WindowClass import *
from PyQt5 import QtTest
from win32com.client import Dispatch

##pip install pypiwin32
##pip install pyqt5???



def mainStart():


    #BREAK CONDITION - CLOSE PROGRAM
    if ui.startButton.text() == "Exit Program":
        exit(0)

    
    #SET BUTTON LABEL
    ui.startButton.setText("Exit Program")

    #FORCE REFRESH GUI
    QtTest.QTest.qWait(0)


    #READ CURRENCY FILE
    objCurrencyListing = readCurrenciesFile().getCurrencyListing()


    ##SET INFO IN GROUPBOXES
    for i in range (4):

        if i == 0:
            
            if objCurrencyListing[0].disable == "False":
                ui.groupBox_0.setTitle(objCurrencyListing[0].currencyName)
                ui.lbl_range_0.setText("[" + str(objCurrencyListing[0].minRange) + " - " + str(objCurrencyListing[0].maxRange) + "]")
                ui.currencyPrice_0.setVisible(True)
                ui.range_0.setVisible(True)
                

        
        elif i == 1:
            
           if objCurrencyListing[1].disable == "False":
                ui.groupBox_1.setTitle(objCurrencyListing[1].currencyName)
                ui.lbl_range_1.setText("[" + str(objCurrencyListing[1].minRange) + " - " + str(objCurrencyListing[1].maxRange) + "]")
                ui.currencyPrice_1.setVisible(True)
                ui.range_1.setVisible(True)
       

        elif i == 2:
            
           if objCurrencyListing[2].disable == "False":
                ui.groupBox_2.setTitle(objCurrencyListing[2].currencyName)
                ui.lbl_range_2.setText("[" + str(objCurrencyListing[2].minRange) + " - " + str(objCurrencyListing[2].maxRange) + "]")
                ui.currencyPrice_2.setVisible(True)
                ui.range_2.setVisible(True)
              

        elif i == 3:
            
            if objCurrencyListing[3].disable == "False":
                ui.groupBox_3.setTitle(objCurrencyListing[3].currencyName)
                ui.lbl_range_3.setText("[" + str(objCurrencyListing[3].minRange) + " - " + str(objCurrencyListing[3].maxRange) + "]")
                ui.currencyPrice_3.setVisible(True)
                ui.range_3.setVisible(True)


    ##CREATE BINANCE OBJECT
    objBinance = BinanceApiRequest()


    #FORCE REFRESH GUI
    QtTest.QTest.qWait(0)

    while (True):

        priceAlert = False

        #0 CURRENCY
        if objCurrencyListing[0].disable == "False":

            ui.lbl_currency_price_0.setText("Getting info")

            #FORCE REFRESH GUI
            QtTest.QTest.qWait(0)
            
            currentPrice = objBinance.requestApi(objCurrencyListing[0])

            #FIX COMMA AS DECIMAL POINT
            tempValue = str( format(currentPrice, ",").replace(',','*').replace('.',',').replace('*','.') )
            ui.lbl_currency_price_0.setText(tempValue)

            if currentPrice < objCurrencyListing[0].minRange or currentPrice > objCurrencyListing[0].maxRange:
                ui.groupBox_0.setStyleSheet("color: darkred;")
                priceAlert = True

            else:
                ui.groupBox_0.setStyleSheet("color: black;")

            #FORCE REFRESH GUI
            QtTest.QTest.qWait(0)


        #1 CURRENCY
        if objCurrencyListing[1].disable == "False":

            ui.lbl_currency_price_1.setText("Getting info")

            #FORCE REFRESH GUI
            QtTest.QTest.qWait(0)

            currentPrice = objBinance.requestApi(objCurrencyListing[1])

            #FIX COMMA AS DECIMAL POINT
            tempValue = str( format(currentPrice, ",").replace(',','*').replace('.',',').replace('*','.') )
            ui.lbl_currency_price_1.setText(tempValue)

            if currentPrice < objCurrencyListing[1].minRange or currentPrice > objCurrencyListing[1].maxRange:
                ui.groupBox_1.setStyleSheet("color: darkred;")
                priceAlert = True

            else:
                ui.groupBox_1.setStyleSheet("color: black;")

            #FORCE REFRESH GUI
            QtTest.QTest.qWait(0)


        #2 CURRENCY
        if objCurrencyListing[2].disable == "False":

            ui.lbl_currency_price_2.setText("Getting info")

            #FORCE REFRESH GUI
            QtTest.QTest.qWait(0)


            currentPrice = objBinance.requestApi(objCurrencyListing[2])

            #FIX COMMA AS DECIMAL POINT
            tempValue = str( format(currentPrice, ",").replace(',','*').replace('.',',').replace('*','.') )
            ui.lbl_currency_price_2.setText(tempValue)

            if currentPrice < objCurrencyListing[2].minRange or currentPrice > objCurrencyListing[2].maxRange:
                ui.groupBox_2.setStyleSheet("color: darkred;")
                priceAlert = True

            else:
                ui.groupBox_2.setStyleSheet("color: black;")

            #FORCE REFRESH GUI
            QtTest.QTest.qWait(0)
            

        #3 CURRENCY
        if objCurrencyListing[3].disable == "False":

            ui.lbl_currency_price_3.setText("Getting info")

            #FORCE REFRESH GUI
            QtTest.QTest.qWait(0)


            currentPrice = objBinance.requestApi(objCurrencyListing[3])

            #FIX COMMA AS DECIMAL POINT
            tempValue = str( format(currentPrice, ",").replace(',','*').replace('.',',').replace('*','.') )
            ui.lbl_currency_price_3.setText(tempValue)

            if currentPrice < objCurrencyListing[3].minRange or currentPrice > objCurrencyListing[3].maxRange:
                ui.groupBox_3.setStyleSheet("color: darkred;")
                priceAlert = True

            else:
                ui.groupBox_3.setStyleSheet("color: black;")


            #FORCE REFRESH GUI
            QtTest.QTest.qWait(0)
            

        
        if priceAlert == True:
            #ALERT SOUND
            speak("Price Alert")


        #WAIT TIMER COMPATIBLE FOR QT GUI
        QtTest.QTest.qWait(5000)

    ###END LOOP


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    #PREVENT RESIZE
    MainWindow.setFixedSize(505, 460)
    

    speak = Dispatch("SAPI.SpVoice").Speak

    #BLANK ALL GROUPBOXES
    ui.groupBox_0.setTitle("NOT IN USE")
    ui.currencyPrice_0.setVisible(False)
    ui.range_0.setVisible(False)

    ui.groupBox_1.setTitle("NOT IN USE")
    ui.currencyPrice_1.setVisible(False)
    ui.range_1.setVisible(False)

    ui.groupBox_2.setTitle("NOT IN USE")
    ui.currencyPrice_2.setVisible(False)
    ui.range_2.setVisible(False)

    ui.groupBox_3.setTitle("NOT IN USE")
    ui.currencyPrice_3.setVisible(False)
    ui.range_3.setVisible(False)

    #CLICK EVENT
    ui.startButton.clicked.connect(mainStart)


    sys.exit(app.exec_())


