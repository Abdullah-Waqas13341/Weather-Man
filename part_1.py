import pandas as pd
import os
dir=input('Enter the directory name in the format (City_weather) replace City with 1)lahore 2) Murree 3) Dubai: ')
if dir=='Dubai_weather' or dir=='Murree_weather':    
    year=input('Enter the year in range (2004 - 2016): ')
elif dir=='lahore_weather':
    year=input('Enter the year in range (1996 - 2011): ')
max_temp=0
min_temp=100000000
max_humidity=0

for files in os.listdir(dir):
    file_path=str(os.path.join(dir,files))
    if year in file_path:

        # print(file_path)
        file_path1=file_path.split('_')

        a='Max TemperatureC'
        b='Min TemperatureC'
        c='Max Humidity'
        
        f=pd.read_csv(file_path,delimiter=',')
        # print(f)
        max_t=f[a].max()
        min_t=f[b].min()
        max_hum=f[c].max()
        if max_t>max_temp:
            max_temp=max_t
            row1=f[f[a]==max_temp]
            date1=row1.iloc[:,0]
            date1=str(date1.values[0])
            var=file_path1[4]
          
        if min_t<min_temp:
            min_temp=min_t
            row2=f[f[b]==min_temp]
            date2=row2.iloc[:,0]
            date2=str(date2.values[0])
            var1=file_path1[4]
        if max_hum>max_humidity:
            max_humidity=max_hum
            row3=f[f[c]==max_humidity]
            date3=row3.iloc[:,0]
            date3=str(date3.values[0])
            var2=file_path1[4]
                
try:
    day1=date1.split('-')
    day1=day1[2]
    day2=date2.split('-')
    day2=day2[2]
    day3=date3.split('-')
    day3=day3[2] 
except:
    print('Given Month is not available in the dataset. Please try again with another month.')       
    exit()         


print(f'Highest: {max_temp} C on {var[:3]} {day1}')
print(f'Lowest: {min_temp} C on {var1[:3]} {day2}')
print(f'Humidity: {max_humidity} % on {var2[:3]} {day3}')

    



# For All datess
# for i in range(len(date1)):
#     day1=str(date1.values[i])
#     print(f'Highest: {max_temp} on {var2} {day1[7:]}')
# for i in range(len(date2)):
#     day2=str(date2.values[i])
#     print(f'Lowest: {min_temp} on {var2} {day2[7:]}')
# for i in range(len(date3)):
#     day3=str(date3.values[i])
#     print(f'Humidity: {max_humidity}% on {var2} {day3[7:]}')