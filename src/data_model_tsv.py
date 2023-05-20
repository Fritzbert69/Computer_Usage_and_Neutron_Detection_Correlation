# Author: Martin Ehrmann; ORCID: 0009-0001-0432-7145
# Licence: GPL-3.0 license
import pandas as pd
import os

dirname = os.path.dirname(__file__)
filename_in = os.path.join(dirname, '../data_input/data_raw/iosc_ci_cfp_cu.tsv')
filename_out = os.path.join(dirname, '../data_input/data_filtered/PC_Use_Filtered.csv')

def filter_and_transform():

    columns =['indic_is', 'unit', 'ind_type', 'geo\\time','2007 ','2008 ','2009 ','2010 ','2011 ','2012 ','2013 ','2014 ','2015 ','2017 ']
    countries =['EU28','BE','BG','DK','DE','EE','FI','LU','EL','IE','IT','HR','LV','LT','SE','MT','NL','AT','PL','PT','RO','CY','SK','SI','ES','CZ','HU','FR','UK']

    #df = pd.read_table('../data_input/data_raw/iosc_ci_cfp_cu.tsv',sep=r',|\t',engine='python',usecols=columns)
    df = pd.read_table(filename_in,sep=r',|\t',engine='python',usecols=columns)

    filtered_df = df[(df['indic_is']=='I_C3') & (df['ind_type']=='IND_TOTAL') & (df['geo\\time'].isin(countries))].copy()
    filtered_df=filtered_df.replace('b','',regex=True)

    increase=[]
    for index,row in filtered_df.iterrows():
        increase.append(format(float(row['2017 '])-float(row['2007 ']),".2f"))

    filtered_df['Increase']=increase
    filtered_df.drop(['indic_is', 'unit', 'ind_type'],axis=1,inplace=True)
    
    
    filtered_df = filtered_df.set_index('geo\\time').transpose(copy=True)
    filtered_df.index.rename('date', inplace=True)
    

    print("Filtered data set: % of individuals who used a computer within the previous 3 months ordered by nationality:")
    print(filtered_df)
    
    filtered_df.to_csv(filename_out)

    #providing metadata:

