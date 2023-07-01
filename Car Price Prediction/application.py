from flask import Flask , render_template,request,url_for
import pandas as pd
import numpy as np
import pickle

app=Flask(__name__)

model1=pickle.load(open("D:\Capstone Project-1\Car Price Prediction\LinearRegressionModel.pkl",'rb'))
# model1='LinearRegressionModel.pkl'
car=pd.read_csv("D:\Capstone Project-1\Car Price Prediction\cardekho_updated.csv")

@app.route('/')
def index():
    model=sorted(car['full_name'].unique())
    companies=(car['company'].unique())
    transmission_type=sorted(car['transmission_type'].unique())
    year=sorted(car['year'].unique(),reverse=True)
    fuel_type=car['fuel_type'].unique()
    km_driven=(request.form.get('km_driven'))
    
    return render_template('cpp.html',companies=companies,model=model,transmission_type=transmission_type, year=year, fuel_type=fuel_type,km_driven=km_driven)


@app.route('/predict', methods=['POST'])
def predict():
    
    if request.method == "POST":
        #pname=request.form['pname']  
        model=(request.form.get('model'))
        companies=(request.form.get('company')) 
        transmission_type=(request.form.get('transmission_type'))
        year=int(request.form.get('year'))
        fuel_type=request.form.get('fuel_type')
        km_driven=request.form['km_driven']
        # prediction=model1.predict(pd.DataFrame(data=np.array([model,companies,year,km_driven,fuel_type,transmission_type]).reshape(1, 6)),columns=['full_name', 'company', 'year', 'kms_driven', 'fuel_type','transmission_type'])      
        prediction = model1.predict(pd.DataFrame(data=([[model,companies,year,km_driven,fuel_type,transmission_type]]),columns=['full_name','company','year','km_driven','fuel_type','transmission_type']))
       # prediction=model1.predict(pd.DataFrame([['Ford Fiesta 1.5','Ford',2014,120000,'Petrol','Manual']],columns=['full_name','company','year','km_driven','fuel_type','transmission_type']))
        # print(model)
        # print(companies)
        # print(transmission_type)
        # print(year)
        # print(fuel_type)
        # print(km_driven)    
        #return str(np.round(prediction[0]),2)
    return str(prediction[0])
    
        
if __name__=="__main__":
    app.run(debug=True)