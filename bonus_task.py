import pandas as pd
import os
from termcolor import colored
import math

dir=input('Enter the directory name in the format (City_weather) replace City with 1)lahore 2) Murree 3) Dubai: ')
if dir=='Dubai_weather' or dir=='Murree_weather':    
    Date=input('Enter the Date in format YYYY/M year can be in range (2004 - 2016): ')
elif dir=='lahore_weather':
    Date=input('Enter the Date in format YYYY/M year can be in range (1996 - 2011): ')
max_temp = 0
min_temp = 100000000
max_humidity = 0
day1 = ''
day2 = ''
day3 = ''
Date = Date.split('/')
l1=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']
l2=['Oct', 'Nov', 'Dec']
if Date[1] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
    M = l1[int(Date[1])-1]
else:
    M = l2[int(Date[1])-10]

year = Date[0]

rows = []
for files in os.listdir(dir):
    file_path = str(os.path.join(dir, files))
    if year in file_path and M in file_path:
        f = pd.read_csv(file_path, delimiter=',')
        rows = f.loc[:, ['Max TemperatureC', 'Min TemperatureC']].values

print(M + ' ' + year)
print("")
f=True
for i in range(len(rows)):
    if i == len(rows) - 1:
        break
    print(f'{i + 1} ', end='')

    try:
        max_temp_value = float(rows[i][0])
        min_temp_value = float(rows[i][1])
        
        if math.isnan(max_temp_value) or math.isnan(min_temp_value):
            print(f'Skipping row {i + 1} due to NaN value')
            continue
        
        max_temp_value = int(max_temp_value)
        min_temp_value = int(min_temp_value)
        
    except ValueError:
        print(f'Skipping row {i + 1} due to invalid number format')
        continue

    for j in range(min_temp_value):
        print(colored('+', 'cyan'), end='')
        f=False
       
    for j in range(max_temp_value):
        print(colored('+', 'red'), end='')
        if j == max_temp_value - 1:
            print(colored('+', 'red'), end=f' {min_temp_value}--{max_temp_value} C')
    
    print('')
if f:
    print('No data available for the given month and year. Please try again with another month.')
