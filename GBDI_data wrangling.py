#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from tqdm import tqdm


# In[10]:


# Read record_01 to dataframe
record_01 = pd.read_csv("Desktop/GBDI_MSD/SES60/record_01.csv")

#Copy df to df2 and generate AREA_ID

record_01['AREA_ID'] = ""

for i in tqdm(record_01.index):
    record_01['AREA_ID'].iloc[i] = str(record_01['CWT'].iloc[i]).zfill(2) + str(record_01['AMP'].iloc[i]).zfill(2) + str(record_01['TMB'].iloc[i]).zfill(2)

#Change type of AREA_ID from obj to int64
record_01[['AREA_ID']]=record_01[['AREA_ID']].astype('int64')

#Read AREA_ID from excel
AREA_ID = pd.read_excel('Desktop/GBDI_MSD/SES60/datadict.xlsx',sheet_name='AREA_ID')

#Merge , Drop , Rename variables in df2
record_01 = record_01.merge(AREA_ID, left_on='AREA_ID', right_on='AREA_ID')
record_01 = record_01.drop(columns=['REG_x', 'CWT_x','AMP_x','TMB_x'])
record_01 = record_01.rename(columns={"CWT_y": "CWT", "AMP_y": "AMP","TMB_y": "TMB","REG_y": "REG"})


# In[11]:


#Record 01 adding value label

VAR_DICT = ['AREA','A01','A03','C01','C03','C04']
rec_01_chk = VAR_DICT.copy()
record_01[VAR_DICT]=record_01[VAR_DICT].astype('str')

for i in tqdm(range(len(VAR_DICT))):
    varDictDf = pd.read_excel('Desktop/GBDI_MSD/SES60/datadict.xlsx',sheet_name=VAR_DICT[i])
    varDictDf =varDictDf.astype('str')
    varDict = dict(varDictDf[[VAR_DICT[i],VAR_DICT[i] + "_DESC"]].values)
    record_01[[VAR_DICT[i]]] = record_01[[VAR_DICT[i]]].replace(varDict)

# record_01.to_csv("Desktop/GBDI_MSD/SES60/record_01_recode.csv",index=False, encoding="utf-8")
record_01.to_excel("Desktop/GBDI_MSD/SES60/record_01_recode.xlsx",index=False)


# In[ ]:


#Record 02 adding value label

record_02 = pd.read_csv("Desktop/GBDI_MSD/SES60/record_02.csv")

VAR_DICT = ['HM02','HM03','HM05','HM06','HM07','HM08','HM09','HM10','HM11','HM13','HM14','HM15','HM16','HM22','HM23','HM24','HM25','HM26','HM32','HM33','HM34','HM35','HM36','HM37','HM38','HM40','HM41']
rec_02_chk = VAR_DICT.copy() 
record_02[VAR_DICT]=record_02[VAR_DICT].astype('str')

for i in tqdm(range(len(VAR_DICT))):
    varDictDf = pd.read_excel('Desktop/GBDI_MSD/SES60/datadict.xlsx',sheet_name=VAR_DICT[i],dtype={VAR_DICT[i]:"str"})
    varDictDf =varDictDf.astype('str')
    varDict = dict(varDictDf[[VAR_DICT[i],VAR_DICT[i] + "_DESC"]].values)
    record_02[[VAR_DICT[i]]] = record_02[[VAR_DICT[i]]].replace(varDict)
    #if VAR_DICT[i] == "HM36" :
    #    print(varDict)
    
# record_02.to_csv("Desktop/GBDI_MSD/SES60/record_02_recode.csv",index=False, encoding="utf-8")
record_02.to_excel("Desktop/GBDI_MSD/SES60/record_02_recode.xlsx",index=False)


# In[5]:


record_01_recode = pd.read_csv("Desktop/GBDI_MSD/SES60/record_01_recode.csv")
record_02_recode = pd.read_csv("Desktop/GBDI_MSD/SES60/record_02_recode.csv")


# In[6]:


#checking record_01 categories variable
for i in range(len(rec_01_chk)):
    print(rec_01_chk[i],record_01_recode[rec_01_chk[i]].unique())
    print("---------------------------------------")


# In[7]:


#checking record_02 categories variable
for i in range(len(rec_02_chk)):
    print(rec_02_chk[i],record_02_recode[rec_02_chk[i]].unique())
    print("---------------------------------------")

