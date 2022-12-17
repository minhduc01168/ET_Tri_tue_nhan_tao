import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('D:\\Learn school\\TTNT_UD\dataset\\Bank_Marketing_Data_Set\\bank\\bank-full.csv',header = None, sep =';')
#data= pd.pivot(df, index = "", columns="age", values="Sex")
print(df)
# print(type(df))
#print(df[0])
#plt.bar(x = ['Yes', 'No'], height = [10, 20, 50])
#plt.xlabel('Tên các nhóm')
#plt.ylabel('Gía trị nhóm')