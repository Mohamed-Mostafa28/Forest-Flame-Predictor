import pandas as pd
from algerianForestFires.utiles.Utilities import dump_model
from algerianForestFires.utiles.Utilities import save_image
from algerianForestFires.utiles.Utilities import save_model_info
from algerianForestFires.utiles.Utilities import load_params
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
import os

class ModelTrainer:
    
    def __init__(self,params):
        self.params=params
        self.read_prepaired_data()
        self.split_prepaired_data()
        self.train_model()
        self.predict()     
        self.evaluate_model()
        self.dump_model()


    def read_prepaired_data(self):        
        prepaired_data_path=self.params["processed_data_params"]["processed_data_path"]
        prepaired_data_name=self.params["processed_data_params"]["processed_data_name"]
        path=os.path.join(prepaired_data_path,prepaired_data_name)
        self.prepaired_data=pd.read_csv(f"{path}", usecols=lambda column: column != 'Unnamed: 0')



    def split_prepaired_data(self):
        y=self.prepaired_data["Classes"]
        x=self.prepaired_data.drop(["Classes"],axis=1)
        self.xtrain ,self.xtest,self.ytrain,self.ytest =train_test_split(x,y,test_size=self.params["split_params"]["test_size"],random_state=self.params["split_params"]["random_state"])

    
    def train_model(self):
        self.model_name=self.params["model_params"]["model_name"]
        self.model_params=self.params["model_params"]["param"]
        if self.model_name == "LogisticRegression":
           self.model =  LogisticRegression(**self.model_params)
        if self.model_name == 'RandomForest':
            self.model = RandomForestClassifier(**self.model_params)            
        if self.model_name == "DecisionTreeClassifier":
            self.model = DecisionTreeClassifier(**self.model_params)            
        self.model.fit(self.xtrain,self.ytrain)                

    def predict(self):        
        self.y_train_pred= self.model.predict(self.xtrain)    
        self.y_test_pred = self.model.predict(self.xtest)            
        
    def evaluate_model(self):        
        self.train_accuracy= accuracy_score(self.y_train_pred,self.ytrain)
        self.test_accuracy = accuracy_score(self.y_test_pred,self.ytest)
        self.classification_report = classification_report(self.ytest, self.y_test_pred)
        self.confusion_matrix = confusion_matrix(self.y_test_pred,self.ytest)    

    def dump_model(self):            
        # save CM
        cm_dump_path = self.params["dump_outputs"]["images_dump_path"]
        
        path=os.path.join(cm_dump_path,f"{self.model_name}_confusion_matrix.png")
        save_image(self.confusion_matrix, ['Class 0', 'Class 1'], self.model_name, self.model_params,path)       
        
         
        # save model info in text file
        model_info_dump_path = self.params["dump_outputs"]["info_dump_path"]
        
        path=os.path.join(model_info_dump_path,f"{self.model_name}_model_info.txt")
        save_model_info(self.model_name, self.test_accuracy, self.model_params,  self.classification_report, path)
        
        #dump model
        model_dump_path = self.params["dump_outputs"]["models_dump_path"]
        
        path=os.path.join(model_dump_path,f"{self.model_name}_model.pkl")
        dump_model(self.model, path)

    
    
    
if __name__=="__main__":
    params=load_params("params.yml")
    ModelTrainer(params)
