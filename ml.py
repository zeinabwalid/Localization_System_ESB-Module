import pyrebase
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from PyQt5 import QtWidgets , QtCore, QtWebSockets,  QtNetwork ,QtGui
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn import preprocessing



data = pd.read_excel (r'dataframe.xlsx') 
data = np.asarray(data)
X_train = data[:,0:3]
X_train =X_train
y_train = data[:,[3,4,5,6]]

classifier = MultiOutputClassifier(SVC(), n_jobs = None)
classifier.fit(X_train, y_train)



config = {
"apiKey": "AIzaSyCEBUDD6s_gWHc4vwikQv69lR7e9JLn7KU",
"authDomain": "esb-mobile-app.firebaseapp.com",
"databaseURL": "https://esb-mobile-app.firebaseio.com",
"storageBucket": "esb-mobile-app.appspot.com"
}



def get_data():
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    da_arr = np.array([db.child("data/wifi1").get().val(),db.child("data/wifi2").get().val(),db.child("data/wifi3").get().val()])
    return(da_arr)


#new_arr = get_data()



def algorthim():
    new_arr = get_data()
    y_pred_1 = classifier.predict(new_arr.reshape(1,-1))
    print(y_pred_1)

for i in range (0,10000):
    algorthim()

