from flask import Flask , render_template,request,url_for
import pandas as pd
import numpy as np
import pickle

app=Flask(__name__)

# import the model
pipe = pickle.load(open('D:\Capstone Project-1\Laptop_Price_Prediction\pipe.pkl','rb'))
dfa = pickle.load(open('D:\Capstone Project-1\Laptop_Price_Prediction\df.pkl','rb'))
df=pd.read_csv("D:\Capstone Project-1\Laptop_Price_Prediction\laptop_data_final.csv")

@app.route('/')
def index():
    company = sorted(df['company'].unique())
    typename = (df['typename'].unique())
    ram = (df['ram'].unique())
    # touchscreen =('Touchscreen',['No','Yes'])
    # ips =('IPS',['No','Yes'])
    resolution = (df['screen_resolution'].unique())
    cpu = (df['cpu'].unique())
    meamory= (df['memory'].unique())
    gpu = (df['gpu'].unique())
    weight=(df['weight'].unique())
    os = (df['os'].unique())

    return render_template('lpp.html',company=company,typename=typename,ram=ram,resolution=resolution,cpu=cpu,meamory=meamory,gpu=gpu,weight=weight,os=os)

@app.route('/predict', methods=['POST'])
def predict():
    
    if request.method == "POST":
        #pname=request.form['pname']  
        company=(request.form.get('company'))
        typename=(request.form.get('type')) 
        ram=(request.form.get('ram'))
        weight=(request.form.get('weight'))
        touchscreen=(request.form.get('touchscreen'))
        ips=(request.form.get('ips'))
        # screen_size=(request.form.get('screensize'))
        resolution=(request.form.get('resolution'))
        cpu=(request.form.get('cpu'))
        meamory=(request.form.get('memory'))
        # hhd=(request.form.get('hhd'))
        # ssd=(request.form.get('ssd'))
        gpu=int(request.form.get('gpu'))
        os=request.form.get('os')
        
        # prediction=model1.predict(pd.DataFrame(data=np.array([model,companies,year,km_driven,fuel_type,transmission_type]).reshape(1, 6)),columns=['full_name', 'company', 'year', 'kms_driven', 'fuel_type','transmission_type'])      
        prediction = pipe.predict(pd.DataFrame(data=([[company,typename,ram,weight,touchscreen,ips,resolution,cpu,meamory,gpu,os]]),columns=['company','type','ram','weight','touchscreen','ips','resolution','cpu','meamory','gpu','os']))
      
    return str(prediction[0])
        
if __name__=="__main__":
    app.run(debug=True)