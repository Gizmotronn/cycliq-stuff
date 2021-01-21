import os
import pandas as pd
from numpy import loadtxt
import numpy as np


# get dataset
for root,dirs,files in os.walk('.', topdown=True):
    for file in files:
       if file.endswith(".csv"):
        f=open(file, 'r', encoding='utf-8')
        #  perform calculation
        datafile = pd.read_csv(f)
        print(datafile)
        f.close()

Skus = loadtxt("sku.txt", comments="#", delimiter=",", unpack=False, dtype=str)



blacklist = datafile[~datafile['MerchantSku'].isin(Skus)]
print(blacklist)


Blackcustomers = blacklist.BuyerEmailAddress.unique()
print(Blackcustomers)

Goodorders = datafile[~datafile['BuyerEmailAddress'].isin(Blackcustomers)]
print(Goodorders)
Goodorders.to_csv("Goodorders.csv") 