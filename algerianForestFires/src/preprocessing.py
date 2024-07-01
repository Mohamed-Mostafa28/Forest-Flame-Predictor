import os
from algerianForestFires.utiles.Utilities import load_params
import pandas as pd



class DataPreprocessor:
    def __init__(self,params):      
        self.params=params  
        self.load_data()
        self.cleaning_data()    
        self.encoding_data()
        self.dump_prepaired_data()
        print("Data processing donee")
    
    
    def load_data(self):
        data_name = self.params["source_data_params"]["source_data_name"]
        source_data = self.params["source_data_params"]["source_data_path"]    
        path=os.path.join(source_data,data_name)
        print(path)
        self.data=pd.read_csv(path)
    
    
    def cleaning_data(self):
        self.data.columns=self.data.columns.str.strip()
        self.data["Classes"] = self.data["Classes"].str.strip()
        self.data["region"]=self.data["region"].str.strip()
        self.data.drop(["day","year","Ws"],axis=1,inplace=True)
        self.data.dropna(inplace=True)
     
    
    def encoding_data(self):
        Region_maping={"Bejaia Region Dataset": 0,"Sidi-Bel Abbes Region Dataset":1}
        Classes_maping={"not fire": 0,"fire":1}
        self.data["region"] = self.data["region"].replace(Region_maping)
        self.data["Classes"] = self.data["Classes"].replace(Classes_maping)

        
    def dump_prepaired_data(self):
        dataSavePath=os.path.join(self.params["processed_data_params"]["processed_data_path"],self.params["processed_data_params"]["processed_data_name"])
        self.data.to_csv(f"{dataSavePath}")

    
    
    
if __name__ == "__main__":
    params=load_params("params.yml")
    DataPreprocessor(params)
