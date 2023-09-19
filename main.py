from  flask import Flask,jsonify,request,render_template

from project_app.utils import MedicalInsurance

app=Flask(__name__)

@app.route('/')
def hello_flask():
    print("Welcome to Insurance Prediction System")   
    return render_template('index.html')

@app.route('/predicted_charges',methods=['POST','GET'])
def predicted_charges():
    if request.method=='GET':
#    data=request.form
#    print('data====',data)

#    age=eval(data['age'])
#    sex=data['sex']
#    bmi=eval(data['bmi'])
#    children=eval(data['children'])
#    smoker=data['smoker']
#    region=data['region']
#    medical_insurance=MedicalInsurance(age,sex,bmi,children,smoker,region)
#    charges=medical_insurance.get_predict_charges()
#    return jsonify({"Result": f"Predicted Charges is {charges} /- Rs."})
  

     age=int(request.args.get('age'))
     sex=request.args.get('sex')
     bmi=float(request.args.get('bmi'))
     children=int(request.args.get('children'))
     smoker=request.args.get('smoker')
     region=request.args.get('region')

     print('age,sex,bmi,children,smoker,region:',age,sex,bmi,children,smoker,region)
   
     medical_insurance=MedicalInsurance(age,sex,bmi,children,smoker,region)
     charges=medical_insurance.get_predict_charges()
     print("Predicted Charges:", charges, "/- Rs.")
     #return render_template('index.html',prediction=charges)
     return render_template("index.html", prediction = charges)

app.run()
