# Computer_Usage_and_Neutron_Detection_Correlation

## About

The research project aims to to raise awareness of possible bit flips in computer hardware 
due to high energy cosmic rays in correlation with the ever increasing amount of computer 
usage in the European Union (EU) between 2007 and 2017. By leveraging two external datasets,
annual data from neutron detectors across different European countries and the percentage of 
individuals who used a computer within the previous three months, this study seeks to raise 
awareness of possible bit flips in computer hardware due to cosmic ray particles.

The software in this repository reuses two external datasets and takes them as input in order 
to filter, analyse and produce three output plots and the corresponding raw data.

## Download

Download the whole repository via git clone to your working directory.


## Installation

The projekt is tested under Linux Ubuntu-20.04 and Python 3.8.10.

It is recommended to create a virtual environment inside your local repository folder. 
For more information on creating virtual environments consider:
<https://docs.python.org/3/library/venv.html>

After the creation (and activation) of the virtual environment you can run
```
pip install -r requirements.txt
```
This will download and install the necessary dependencies for you.

## Retrieving the necessary datasets
NOTE: If one is not able to retrieve the complete data sets, the program will provide 
the option to reuse already filtered datasets which are already included in the repository.

### Neutron detectors
#### Record citation:

• re3data.org - Registry of Research Data Repositories.

• re3data.org: NMDB

• editing status 2022-05-31

• DOI: http://doi.org/10.17616/R3PW80

• last accessed: 2023-05-21

• Repository URL: https://www.nmdb.eu

• access: open access

For this research 8 different neutron detectors in EU-member countries have been selected:

#### Instructions for retrieving the data:

1. go to to the repository website https://www.nmdb.eu
2. read the data retrieval instructions under header Data and go to https://www.nmdb.eu/
nest/
3. use the following settings for the data query:

• Stations: ATHN, ROME, JUNG, JUNG1, LMKS, DRBS, KIEL, OULU

• Date Selection (UTC) From: 2007-01-01 00:00:00 UTC

• Date Selection (UTC) To: 2019-01-01 00:00:00 UTC

• Resolution Time Resolution: 1 year

• Data variables: Pressure & efficiency corr.

• Scale: Counts/s*

• Output: Ascii

4. click an Submit
5. select and copy the result starting with the line

QUERY RESULTS SUMMARY

and ending (and including) the last line of data points. Do not copy the Total execution
time line!
6. safe the data in an .txt file to your local repository with the name nmdb_data.txt in the folder /input_data/data_raw/

### Computer Usage:
#### Record citation:

• re3data.org - Registry of Research Data Repositories.

• re3data.org: Eurostat

• editing status 2021-12-15

• DOI: http://doi.org/10.17616/R3FW3X

• last accessed: 2023-05-13

• Repository URL: https://ec.europa.eu/eurostat/

• access: open access

• Policy and Licence: https://ec.europa.eu/eurostat/about-us/policies/copyright

For this research the whole dataset ISOC_CI_CFP_CU has been chosen.

#### Instructions for retrieving the data:

1. go to to the repository website https://ec.europa.eu/eurostat/
2. enter ISOC_CI_CFP_CU into the search bar and select the first dataset
3. choose the dataset with the title Individuals - computer use and the code isoc_ci_cfp_cu
and click Download data
4. you should find a packaged file with the name isoc_ci_cfp_cu.tsv.gz in your download
folder.
5. unpack this file and safe it under the name isoc_ci_cfp_cu.tsv to your local repository /input_data/data_raw/

## Run the experiment:
type the following line into your bash console:
```
python3 ./main.py
```
