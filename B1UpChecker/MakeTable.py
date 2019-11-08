import dash
import dash_table
import pandas as pd
import csv

def makeCSV(rigName,rigUptime,rigTemp,rigGPUCount,rigHashrate,rigIP)
f = open('rigs.csv', 'w')

with f:
    fnames = ['name','up_time','temperature','gpu_count','hash_rate','ip']
    writer = csv.DictWriter(f, fieldnames=fnames)

    writer.writeheader()
    writer.writerow({'name' : rigName,
                     'up_time' : rigUptime,
                     'temperature' : rigTemp,
                     'gpu_count' : rigGPUCount,
                     'hash_rate' : rigHashrate,
                     'ip' : rigIP})