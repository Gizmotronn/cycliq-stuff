import os
import pandas as pd
import numpy as np
from numpy import loadtxt


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


Blackcustomers = blacklist.PlatformOrderId.unique()
print(Blackcustomers)

Goodorders = datafile[~datafile['BuyerEmailAddress'].isin(Blackcustomers)]
print(Goodorders)
Goodorders.to_csv("Goodorders.csv") 