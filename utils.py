import numpy as np 
import pandas as ps 
import pickle
import json
import  config
import os
import warnings
warnings.filterwarnings('ignore')

class MedicalInsurance():
    def __init__(self,age,sex,bmi,children,smoker,region):
        self.age=age
        self.sex=sex
        self.bmi=bmi
        self.smoker=smoker
        self.children=children
        self.region='region_' + region
    def load_model(self):
        with open (config.MODEL_FILE_PATH,'rb') as f:
           self.model= pickle.load(f)
        
        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data=json.load(f)
    
    def get_predict_charges(self):

        self.load_model()
        region_index = list(self.json_data['columns']).index(self.region)
       
        test_array=np.zeros(len(self.json_data['columns']))

        test_array[0]=self.age
        test_array[1]=self.json_data['sex'][self.sex]
        test_array[2]=self.bmi
        test_array[3]=self.children
        test_array[4]=self.json_data['smoker'][self.smoker]
        test_array[region_index]=1

        print("Test Array -->\n", test_array)

        charges=round(self.model.predict([test_array])[0],3)
        
        print('The Predictive Charges Of Medical Insurance is:',charges)
        return charges

if __name__=="__main__":
    age="30"
    sex='female'
    bmi=27
    children=0
    smoker='yes'
    region='northwest'

    medical_insurance=MedicalInsurance(age,sex,bmi,children,smoker,region)
    charges=medical_insurance.get_predict_charges()
    print("Predicted Charges:", charges, "/- Rs.")




    