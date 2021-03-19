from flask import Flask, render_template, request

import requests
import pickle
import numpy as np
import sklearn





app = Flask(__name__)



#load my knn model that i trained in my Jupyter Notebook
pickle_in = open('classifier.pkl','rb')

classifier = pickle.load(pickle_in)


@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')




@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        
        
        ram = int(request.form['RAM'])
        
        battery_power = int(request.form['batteryPower'])
        px_width = int(request.form['pixelWidth'])
        px_height = int(request.form['pixelHeight'])
        mobile_wt = int(request.form['mobileWeight'])
        int_memory = int(request.form['internalMemory'])
        n_cores = int(request.form['numOfCores'])
   
        prediction = classifier.predict([[ram,battery_power,px_width,px_height,mobile_wt,int_memory,n_cores]])
        
        priceRangeNum = prediction[0]
        
        if(priceRangeNum==0):
            priceRangeStr = "low" 
        elif(priceRangeNum==1):
            priceRangeStr = "medium"
        elif(priceRangeNum==2):
            priceRangeStr = "high"
        elif(priceRangeNum==3):
            priceRangeStr = "very high"
        
        
        
        
        
        
        
        
        
        return render_template('index.html',prediction_text="The price range of the phone is " + priceRangeStr )
        
    
    
    else:
        return render_template('index.html')
        
    
    






if __name__=="__main__":
    app.run()