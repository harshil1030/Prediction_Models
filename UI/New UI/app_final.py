from flask import Flask , render_template,request,url_for
from flask_cors import CORS,cross_origin
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)
cors=CORS(app)
model1=pickle.load(open("D:\Prediction_Models\Car Price Prediction\LinearRegressionModel.pkl",'rb'))
pipe = pickle.load(open('D:\Prediction_Models\Laptop_Price_Prediction\pipe.pkl','rb'))
# df = pickle.load(open('df.pkl','rb'))
# model1='LinearRegressionModel.pkl'
car=pd.read_csv("D:\Prediction_Models\Car Price Prediction\cardekho_updated.csv")
# df=pd.read_csv("D:\Capstone Project-1\Laptop_Price_Prediction\laptop_data_final.csv")
df=pd.read_csv("D:\Prediction_Models\Laptop_Price_Prediction\lappy.csv")


#Main Page
@app.route('/')
def index():
    return render_template('index.html')        
 
#Car Price Prediction
@app.route('/cpp')
def cpp():
    #model=sorted(car['full_name'].unique())
    car_models=sorted(car['full_name'].unique())
    companies=(car['company'].unique())
    transmission_type=sorted(car['transmission_type'].unique())
    year=sorted(car['year'].unique(),reverse=True)
    fuel_type=car['fuel_type'].unique()
    km_driven=(request.form.get('km_driven'))
    
    return render_template('car.html',companies=companies,car_models=car_models,transmission_type=transmission_type, year=year, fuel_type=fuel_type,km_driven=km_driven)


@app.route('/cpp', methods=['POST'])
def predict():
    if request.method == "POST":
        car_model=(request.form.get('car_models'))
        companies=(request.form.get('company')) 
        transmission_type=(request.form.get('transmission_type'))
        year=int(request.form.get('year'))
        fuel_type=request.form.get('fuel_type')
        km_driven=request.form['km_driven']
        # prediction=model1.predict(pd.DataFrame(data=np.array([model,companies,year,km_driven,fuel_type,transmission_type]).reshape(1, 6)),columns=['full_name', 'company', 'year', 'kms_driven', 'fuel_type','transmission_type'])      
        prediction = model1.predict(pd.DataFrame(data=([[car_model,companies,year,km_driven,fuel_type,transmission_type]]),columns=['full_name','company','year','km_driven','fuel_type','transmission_type']))
       # prediction=model1.predict(pd.DataFrame([['Ford Fiesta 1.5','Ford',2014,120000,'Petrol','Manual']],columns=['full_name','company','year','km_driven','fuel_type','transmission_type']))
    if  prediction < 0:
        prediction = "Data Irrelevent"
        return(prediction)
    else:
        return str(np.round(prediction[0],2))
    

#Laptop Price Prediction
@app.route('/lpp')
def lpp():
    company =(df['company'].unique())
    typename = (df['typename'].unique())
    Ram = (df['Ram'].unique())
    Touchscreen =(df['Touchscreen'].unique())
    screen_resolution = (df['screen_resolution'].unique())
    cpu = (df['cpu'].unique())
    Ips= (df['Ips'].unique())
    gpu = (df['gpu'].unique())
    Weight=(df['Weight'].unique())
    os = (df['os'].unique())
    ppi=(df['ppi'].unique())
    HDD=(df['HDD'].unique())
    SSD=(df['SSD'].unique())

    return render_template('lap.html',company=company,Ips=Ips,typename=typename,Ram=Ram,Touchscreen=Touchscreen,ppi=ppi,HDD=HDD,SSD=SSD,screen_resolution=screen_resolution,cpu=cpu,gpu=gpu,Weight=Weight,os=os)

@app.route('/lpp', methods=['POST'])
def predicta():
    if request.method == "POST":
        company=(request.form.get('company'))
        typename=(request.form.get('typename')) 
        Ram=(request.form.get('Ram'))
        Weight=(request.form.get('Weight'))
        Touchscreen=(request.form.get('Touchscreen'))
        Ips=(request.form.get('Ips'))
        screen_resolution=(request.form.get('screen_resolution'))
        cpu=(request.form.get('cpu'))
        gpu=(request.form.get('gpu'))
        os=request.form.get('os')
        ppi=(request.form.get('ppi'))
        HDD=(request.form.get('HDD'))
        SSD=(request.form.get('SSD'))
            
        # prediction=model1.predict(pd.DataFrame(data=np.array([model,companies,year,km_driven,fuel_type,transmission_type]).reshape(1, 6)),columns=['full_name', 'company', 'year', 'kms_driven', 'fuel_type','transmission_type'])      
        predictiona= pipe.predicta(pd.DataFrame(data=([[SSD,HDD,ppi,Ips,company,typename,Ram,Weight,Touchscreen,screen_resolution,cpu,gpu,os]]),columns=['company','typename','Ram','Weight','Touchscreen','screen_resolution','cpu','ppi','gpu','os','SSD','HDD','Ips']))
    return str(np.round(predictiona[0],2))

@cross_origin()
def info():
    return render_template('infromation.html')
                 
if __name__=="__main__":
    app.run(debug=True) 