import csv
import pandas as pd
import os
import tkinter
from tkinter import filedialog

def getNum(inputString):
    number = []
    for char in inputString:
        if (char.isdigit() == True):
            number.append(char)
    return number

def listToString(s):  
    # initialize an empty string 
    str1 = ""  
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    # return string   
    return str1

def resistance(col):
    if 'Channel 1' in col:
        print(df[col].astype('float') >= 3)
        return 714
    if 'Channel 2' in col:
        return 715
    if 'Channel 3' in col:
        return  716
    if 'Channel 4' in col:
        return  717
    if 'Channel 5' in col:
        return  716
    if 'Channel 6' in col:
        return  3572
    if 'Channel 7' in col:
        return  3546
    if 'Channel 8' in col:
        return  3555
    if 'Channel 9' in col:
        return  3554
    if 'Channel 10' in col:
        return  3562

def sumSpecial(x):
    try:
        f = float(x)
        return f
    except Exception as e:
        return 0

root = tkinter.Tk()
root.withdraw()

filename = filedialog.askopenfilename(parent=root,title='Select the csv file containing the data you would like energy calculated for.')

print(filename)

df = pd.read_csv(filename)
df.columns = df.iloc[2]
df = df[3:]


print(df.index[0])
df.drop(df.index[0], inplace = True)


for index, col in enumerate(df.columns[1:]):
    if col == None:
        break
    elif 'Channel' in col:
        tmp = getNum(col)
        num = listToString(tmp)
        loc = df.columns.get_loc(col)
        col_name = 'Energy ' + num
        df.insert(loc + 1, col_name, value=['' for i in range(df.shape[0])])
        res = resistance(col)
        df[col] = df[col].astype('float')
        #df[col_name] = (((df[col].astype('float'))**2)/res) * 600
        df.loc[df[col] >= 3, col_name] = ((df[col]**2)/res) * 600
        df.loc[df[col] < 3, col_name] = 0
        df[col_name] = df[col_name].astype('float')
        energy_name = 'Total Energy ' + str(num)
        df[energy_name] = df[col_name].sum()
        df.loc[5::, energy_name] = None


df.to_csv('EnergyCalculation.csv')

print(df)