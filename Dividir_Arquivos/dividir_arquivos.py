from os import sep
import pandas as pd

#csv file name to be read in 

in_csv = r'input\PSNEW-3148__newCSV.csv'

#get the number of lines of the csv file to be read
number_lines = sum(1 for row in (open(in_csv, encoding="utf8")))

#size of rows of data to write to the csv, 
#you can change the row size according to your need

rowsize = 500

#start looping through data writing it to a new file for each set

for i in range(1,number_lines,rowsize):
      df = pd.read_csv(in_csv,header=None,nrows = rowsize, skiprows = i,sep=';', encoding='utf-8-sig')  
      out_csv = r'output\output' + str(i) + '.csv'
      df.to_csv(out_csv,index=False,header=False,mode='a', chunksize=rowsize, sep=';')

