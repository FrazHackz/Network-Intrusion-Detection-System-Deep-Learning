# script to append all the csv data files into 1
import csv
import os
import sys
import numpy as np
import pandas as pd
from sklearn.utils import shuffle

dataPath = 'data'  # use your path
directory_files = os.listdir("D:\\University\\semester 6\\Data Mining\\Project\\data")
fileNames = []
for file in directory_files:
    fileNames.append(file)

df = pd.read_csv(os.path.join(dataPath, fileNames[0]))
print(df.shape)
for name in fileNames[1:]:
    fname = os.path.join(dataPath, name)
    print('appending:', fname)
    df1 = pd.read_csv(fname)
    df = df.append(df1, ignore_index=True)

df = shuffle(df)
print("Data Shape : ",df.shape)

print('creating binary-class file')
#converting multiclass to binary
df["Label"] = df["Label"].map(
    {'BENIGN': 0, 'DDoS': 1, 'PortScan': 1, 'Bot': 1, 'Infiltration': 1, 'Web Attack Brute Force' : 1,
     'Web Attack XSS': 1, 'Web Attack Sql Injection': 1, 'FTP-Patator': 1, 'SSH-Patator': 1,'DoS Hulk':1,
     'DoS GoldenEye': 1, 'Heartbleed': 1, 'DoS slowloris': 1,'DoS Slowhttptest':1})

print(df['Label'][1:20])
outFile = os.path.join(dataPath, 'IDS-2017-binaryclass')
df.to_csv(outFile + '.csv', index=False)
df.to_pickle(outFile + '.pickle')
print('all done...')
