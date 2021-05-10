from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import QPainter, QColor, QFont,QBrush,QPen , QPixmap
from PyQt5.QtCore import Qt , QPointF
from in_use import Ui_MainWindow
import sys
import numpy as np
import pyrebase
import pandas as pd
from sklearn.model_selection import train_test_split
from PyQt5 import QtWidgets , QtCore, QtWebSockets,  QtNetwork ,QtGui
from sklearn.multioutput import MultiOutputClassifier
from sklearn.svm import SVC



config = {
"apiKey": "AIzaSyCEBUDD6s_gWHc4vwikQv69lR7e9JLn7KU",
"authDomain": "esb-mobile-app.firebaseapp.com",
"databaseURL": "https://esb-mobile-app.firebaseio.com",
"storageBucket": "esb-mobile-app.appspot.com"
}

""" data = pd.read_excel (r'dataframe.xlsx') 
data = np.asarray(data)
X_train = data[:,0:3]
X_train =X_train
y_train = data[:,[3,4,5,6]]

classifier = MultiOutputClassifier(SVC(), n_jobs = None)
classifier.fit(X_train, y_train)

def get_data():
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    da_arr = np.array([db.child("data/wifi1").get().val(),db.child("data/wifi2").get().val(),db.child("data/wifi3").get().val()])
    return(da_arr)

def algorthim():
    new_arr = get_data()
    y_pred = classifier.predict(new_arr.reshape(1,-1))
    print(y_pred) """

class ApplicationWindow(QtWidgets.QMainWindow):


    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(750, 750)
        self.paint = False
        self.timer = QtCore.QTimer()
        self.timer.setInterval(3000)
        self.timer.timeout.connect(self.onTimeout)
        self.timer.start()

        """ self.timer1 = QtCore.QTimer()
        self.timer1.setInterval(3000)
        self.timer1.timeout.connect(self.predict)
        self.timer1.start() """
       

    #def predict(self):
    #   algorthim()

    def onTimeout(self):
        self.paint = True
        self.update()
        
    
    def paintEvent(self, event):
        firebase = pyrebase.initialize_app(config)
        db = firebase.database()
        self.da_arr = np.array([db.child("data/xGUI").get().val(),db.child("data/yGUI").get().val()])
        if (self.da_arr[0]==1 ):        
            painter = QPainter(self)
            self.image =QPixmap("map.jpeg")
            painter.drawPixmap(self.rect(), self.image)
            pen = QPen(Qt.red)
            painter.setPen(pen)
            painter.drawEllipse(QPointF(400,350), 13, 13)
            painter.setBrush(QBrush(Qt.red))
            painter.drawEllipse(QPointF(400,350), 7, 7) 
             
        

     
        
        
        












        '''painter.begin(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        
        painter.drawPoint(500, 300)     
        painter.end()'''
    
    
    '''def draw_something(self,event,painter):
        #painter = QtGui.QPainter(self)
        #painter.drawPixmap(self.rect(), self._image)
        #pen = QtGui.QPen()
        painter.setPen(QtGui.QColor('red'))
        #qp.setWidth(5)
        #painter.setPen(pen)
        painter.drawPoint(500, 300) # location of point
        #painter.drawEllipse(300, 300, 70, 70)
        #painter.end()
        print("in")'''

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()