from dataclasses import dataclass
import imp
import CreateCSV.CSV.CreateData as Data
import CreateCSV.CSV.DataToCSV as CSV
import CreateCSV.Constants.Constants as c
from selenium import webdriver

def main():
    data = Data.ApNews.data() #create ApNews and Yle data with data(); name is silly for class, but it does ap primarily, refers to yle after
    file = CSV.writecsv(data) #write the data into the file file with writecsv()
    print(file)

if __name__ == '__main__':
    main()