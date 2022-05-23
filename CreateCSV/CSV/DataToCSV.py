import sys
from traceback import print_tb
sys.path.append(r'C:\Users\Miika\Desktop\Python projects\Projects\WebscraperNewsProgram')

import CreateCSV.Constants.Constants as c


import csv

def writecsv(file): #for writing csv             
    with open(c.ARTICLE,'w',encoding='utf-8') as csv_file:
        csv_writer = csv.DictWriter(csv_file,fieldnames=c.FIELDNAMES, delimiter=',')
        csv_writer.writeheader()
        csv_writer = csv.writer(csv_file, delimiter=',')
        for data in file:
            csv_writer.writerow(data)
        return file