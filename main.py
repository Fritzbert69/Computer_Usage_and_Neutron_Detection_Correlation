# Author: Martin Ehrmann; ORCID: 0009-0001-0432-7145
# Licence: GPL-3.0 license
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import csv
import os.path
import sys
from src.data_model_tsv import filter_and_transform as model_tsv
from src.data_model_txt import filter_and_transform as model_txt

# Check for input data

if os.path.exists('data_input/data_raw/iosc_ci_cfp_cu.tsv'):
    print("Dataset: iosc_ci_cfp_cu.tsv found! \n Procede with data-filtering and callculations")
    model_tsv()


else:
    print("Dataset: iosc_ci_cfp_cu.tsv not found! \n Possible reasons:") 
    print("Wrong name: the original name has not been modified and should be \"iosc_ci_cfp_cu.tsv\"")
    print("Wrong data format: data format should be \".tsv\"")
    print("Wrong path: iosc_ci_cfp_cu.tsv should be within \"/data_input/data_raw/\"")
    print("...\n ")

    
    while True:
        user_input = input('Should the experiment proceede with the already transformed data? [Y/N]: ')
        if user_input.lower() == 'y':
            print('Proceede with transformed data.')

            if os.path.exists('data_input/data_filtered/PC_Use_Filtered.csv'):
                print("Filtered dataset: PC_Use_Filtered.csv found! \n Procede with creating visualizations")
                break

            else:
                print("Filtered dataset: PC_Use_Filtered.csv not found! \n Considere instructions in the README file or clone the repository again!") 
                print('Terminate the execution.')
                sys.exit()
                
        elif user_input.lower() == 'n':
            print('Terminate the execution.')
            sys.exit()

        else:
            print('Please type Y for yes or N for no')

if os.path.exists('data_input/data_raw/nmdb_2023_05_13.txt'):
    print("Dataset: nmdb_2023_05_13.txt found! \n Procede with data-filtering and callculations")
    model_txt()


else:
    print("Dataset: nmdb_2023_05_13.txt not found! \n Possible reasons:") 
    print("Wrong name: the original name has not been modified and should be \"nmdb_2023_05_13.txt\"")
    print("Wrong data format: data format should be \".txt\"")
    print("Wrong path: nmdb_2023_05_13.txt should be within \"/data_input/data_raw/\"")
    print("...\n ")

    
    while True:
        user_input = input('Should the experiment proceede with the already transformed data? [Y/N]: ')
        if user_input.lower() == 'y':
            print('Proceede with transformed data.')
            if os.path.exists('data_input/data_filtered/Neutron_Detection_Filtered.csv'):
                print("Filtered dataset: Neutron_Detection_Filtered.csv found! \n Procede with creating visualizations")
                break
            else:
                print("Filtered dataset: Neutron_Detection_Filtered.csv not found! \n Considere instructions in the README file or clone the repository again!") 
                print('Terminate the execution.')
                sys.exit()
                
        elif user_input.lower() == 'n':
            print('Terminate the execution.')
            sys.exit()

        else:
            print('Please type Y for yes or N for no')


# Load filtered datasets
df_pc_usage = pd.read_csv('data_input/data_filtered/PC_Use_Filtered.csv',sep=',',skipinitialspace = True,engine='python')
df_neutron_detection = pd.read_csv('data_input/data_filtered/Neutron_Detection_Filtered.csv',sep=',',skipinitialspace = True,engine='python')


# plot and output data generation
plot_bar_x=np.linspace(0,28,29)
countries=df_pc_usage.iloc[[-1][:]]
row_average=list(countries.iloc[0])
average_values=[]
for i in range(len(row_average)-1):
    average_values.append(float(row_average[i+1]))
plt.figure(figsize=(15,6))
plt.bar(plot_bar_x,average_values, tick_label=list(countries)[1:],label="10-year period increase")

plt.grid()
plt.ylabel("increase in %-points")
plt.xlabel("EU-countries")
plt.legend()
plt.savefig("data_output/plots_output/computer_usage_increase_10y_EUall_bar.png")
 
# show the plot
#plt.show()

plt.close()

# field names 
fields = ['country', 'increase'] 
computer_usage_increase_10y_EUall_bar =[]
for i in range(len(average_values)):
    computer_usage_increase_10y_EUall_bar.append([list(countries)[i+1],average_values[i]])

# name of csv file 
filename = "data_output/raw_data_output/computer_usage_increase_10y_EUall_bar.csv"
    
# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(fields) 
        
    # writing the data rows 
    csvwriter.writerows(computer_usage_increase_10y_EUall_bar)
 


plt.figure(figsize=(15,6))
plt.plot(df_pc_usage.iloc[:-1]['date'],df_pc_usage.iloc[:-1]['EU28'],'-x',label="% of adult individuals who used a computer within the previous 3 months")
ax = plt.gca()
ax.set_xlim(ax.get_xlim()[::-1])
plt.grid()
plt.ylabel("% of adult individuals")
plt.xlabel("Average over all 28 EU-countries between 2007 and 2017")
plt.legend()
plt.savefig("data_output/plots_output/computer_usage_3m_EUsingle_line.png")

# show the plot
#plt.show()

plt.close()

# field names 
fields = ['year', 'percentage_of_individuals'] 
computer_usage_3m_EUsingle_line =[]
for i in range(len(list(df_pc_usage.iloc[:-1]['date']))):
    computer_usage_3m_EUsingle_line.append([df_pc_usage.iloc[i]['date'],df_pc_usage.iloc[i]['EU28']])

# name of csv file 
filename = "data_output/raw_data_output/computer_usage_3m_EUsingle_line.csv"
    
# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(fields) 
        
    # writing the data rows 
    csvwriter.writerows(computer_usage_3m_EUsingle_line)


plt.figure(figsize=(15,6))
plt.plot(df_neutron_detection.iloc[:]['date'],df_neutron_detection.iloc[:]['Average_per_year'],'-x',label="neutron detection per second averaged over EU countries")
plt.xticks(list(df_neutron_detection.iloc[:]['date']))
plt.grid()
plt.ylabel("number of neutron detections per second")
plt.xlabel("Average over 8 neutron detectors in EU-countries between 2007 and 2017")
plt.legend()
plt.savefig("data_output/plots_output/anualy_averaged_neutron_detections_per_sec_EU.png") 

# show the plot
#plt.show()

plt.close()

# field names 
fields = ['year', 'neutron_detections_per_second_averaged'] 
anualy_averaged_neutron_detections_per_sec_EU =[]
for i in range(len(list(df_neutron_detection.iloc[:]['date']))):
    anualy_averaged_neutron_detections_per_sec_EU.append([int(df_neutron_detection.iloc[i]['date']),df_neutron_detection.iloc[i]['Average_per_year']])

# name of csv file 
filename = "data_output/raw_data_output/anualy_averaged_neutron_detections_per_sec_EU.csv"
    
# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(fields) 
        
    # writing the data rows 
    csvwriter.writerows(anualy_averaged_neutron_detections_per_sec_EU)

print(" ")
print("Plots and output data generated successfully")
