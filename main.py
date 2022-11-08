import pandas as pd
import csv    

with open('seeds_dataset.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter='\t')
    csv_writer.writerow(['Area', 'Perimeter', 'Compactness', 'Length of kernel', 'Width of kernel', 'Asymmetry coefficient', 'Length of kernel groove'])

read_file = pd.read_csv('seeds_dataset.txt')
read_file.to_csv('seeds_dataset.csv', sep='\t', mode="a", index=None)