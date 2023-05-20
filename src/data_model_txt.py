# Author: Martin Ehrmann; ORCID: 0009-0001-0432-7145
# Licence: GPL-3.0 license
import pandas as pd
import os

dirname = os.path.dirname(__file__)
filename_in = os.path.join(dirname, '../data_input/data_raw/nmdb_2023_05_13.txt')
filename_out = os.path.join(dirname, '../data_input/data_filtered/Neutron_Detection_Filtered.csv')


def filter_and_transform():
        
    columns=['date','ATHN'   , 'ROME'  ,  'JUNG'  , 'JUNG1'  ,  'LMKS' ,   'DRBS'  ,  'KIEL'  ,  'OULU']
    df = pd.read_table(filename_in,sep=';',skiprows=29,engine='python',header=0,names=columns,parse_dates=True)
    df['date'] = pd.to_datetime(df['date'])
    df['date'] = df['date'].dt.year


    filtered_df=df[(df['date']<2018)].copy()


    average=[]
    for index,row in filtered_df.iterrows():
        number_of_datapoints=len(columns)-1
        avg=0

        for column_name in columns[1:]:
            if row[column_name]=='   null' :
                number_of_datapoints-=1
            else:
                avg+=float(row[column_name])

        average.append(format(avg/number_of_datapoints,".3f"))

        #average.append(format(float(row['2017 '])-float(row['2007 ']),".2f"))

    filtered_df['Average_per_year']=average

    print("Filtered data set: Number of Neutron detections per second averaged over a one year period:")
    print(filtered_df)
    filtered_df.to_csv(filename_out,index=False)
    #providing metadata: