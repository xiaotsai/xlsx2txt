import pandas as pd
import os

filename =[]

for files in os.walk("./"):
    for i in list(files):
        for j in i:
            if j.endswith(".xlsx"):
                filename.append(j)
                print(filename)
   

for file in filename:
    file0 = file.split('.')[0]
    pd.read_excel(file, sheet_name="New Today",usecols=["Hidden Service", "Title"]).to_csv(file0+".txt",sep='\t',index=False)
    pd.read_excel(file, sheet_name="Up",usecols=["Hidden Service", "Title"]).to_csv(file0+".txt",mode='a',sep='\t',index=False)
    #sheet_name="工作表1 " usecols=["Hidden Service", "Title"] A1=Hidden Service B1= title ....



