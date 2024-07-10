import pandas as pd
import os
dir=input('Enter the directory name in the format (City_weather) replace City with 1)lahore 2) Murree 3) Dubai: ')
if dir=='Dubai_weather' or dir=='Murree_weather':    
    Date=input('Enter the Date in format YYYY/M year can be in range (2004 - 2016): ')
elif dir=='lahore_weather':
    Date=input('Enter the Date in format YYYY/M year can be in range (1996 - 2011): ')
max_temp=0
min_temp=100000000
max_humidity=0
Date=Date.split('/')
l1=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']
l2=['Oct', 'Nov', 'Dec']
if Date[1] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
    M = l1[int(Date[1])-1]
else:
    M = l2[int(Date[1])-10]

year=Date[0]

    
for files in os.listdir(dir):
    file_path=str(os.path.join(dir,files))
    if year in file_path:
      
            if M in file_path:
            
                # print(file_path)

                file_path1=file_path.split('_')

                a='Mean TemperatureC'
                b=' Mean Humidity'

                f=pd.read_csv(file_path,delimiter=',')
                # print(f)
                max_at=f[a].max()
                min_at=f[a].min()
                max_ah=f[b].max()
                # print(max_ah)
                if max_at>max_temp:
                    max_temp=max_at
                    row1=f[f[a]==max_temp]
                    date1=row1.iloc[:,0]
                    date1=str(date1.values[0])
                    print(date1)


                if min_at<min_temp:
                    min_temp=min_at
                    row2=f[f[a]==min_temp]
                    date2=row2.iloc[:,0]
                    date2=str(date2.values[0])

                if max_ah>max_humidity:
                    max_humidity=max_ah
                    row3=f[f[b]==max_humidity]
                    date3=row3.iloc[:,0]
                    date3=str(date3.values[0])
     
                
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
    
    
print(       f'Highest: {max_temp} C on {M} {day1}')
print(f'Lowest: {min_temp} C on {M} {day2}')
print(f'Humidity: {max_humidity} % on {M} {day3}')
