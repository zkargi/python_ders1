import os
import zipfile
from zipfile import ZipFile
import pandas as pd
import sqlite3

if not os.path.exists("veri"):
    os.mkdir("veri")
    arsiv=zipfile.ZipFile("pariteler_cikti_1hour_2022_2022.zip")
    arsiv.extractall(path="veri/")

tum_dosyalar=os.listdir("veri")
pandas_csv_listesi=[]
for csv_dosya in tum_dosyalar:
    veri =p.read_csv("veri/"+ csv_dosya)
    del veri["volume"]
    pandas_csv_listesi.append(veri)
    print(veri.head())

birlesmis_csv_ler=pd.concat(pandas_csv_listesi)
birlesmis_csv_ler.to_csv('hepsi.csv'index=False)




print(tum_dosyalar)