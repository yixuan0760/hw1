# Part. 1

#=======================================

# Import module

#  csv -- fileIO operation

import csv

#=======================================


# Part. 2

#=======================================

# Read cwb weather data

cwb_filename = '106061202.csv'

data = []

header = []

with open(cwb_filename) as csvfile:

   mycsv = csv.DictReader(csvfile)

   header = mycsv.fieldnames

   for row in mycsv:

      data.append(row)
#=======================================


# Part. 3

#=======================================

# Analyze data depend on your group and store it to target_data like:

# Retrive all data points which station id is "C0X260" as a list.

# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))
target_data_C0A880 = list(filter(lambda item: item['station_id'] == 'C0A880', data))
column_C0A880 = [row['PRES'] for row in target_data_C0A880]
sum_C0A880=0
for i in range(len(column_C0A880)):
    if column_C0A880[i]== '-99.000':
        column_C0A880[i] = 0
    sum_C0A880 += float(column_C0A880[i])
mean_C0A880=sum_C0A880/len(column_C0A880)
if mean_C0A880 == 0:
    print(['C0A880','None'])
else :
    print(['C0A880',mean_C0A880],)

target_data_C0F9A0 = list(filter(lambda item: item['station_id'] == 'C0F9A0', data))
column_C0F9A0 = [row['PRES'] for row in target_data_C0F9A0]
sum_C0F9A0=0
for i in range(len(column_C0F9A0)):
    if column_C0F9A0[i]== '-99.000':
        column_C0F9A0[i] = 0
    sum_C0F9A0 += float(column_C0F9A0[i])
mean_C0F9A0=sum_C0F9A0/len(column_C0F9A0)
if mean_C0F9A0 == 0:
    print (['C0F9A0','None'],)
else :
    print (['C0F9A0',mean_C0F9A0],)

target_data_C0G640 = list(filter(lambda item: item['station_id'] == 'C0G640', data))
column_C0G640 = [row['PRES'] for row in target_data_C0G640]
sum_C0G640=0
for i in range(len(column_C0G640)):
    if column_C0G640[i]== '-99.000':
        column_C0G640[i] = 0
    sum_C0G640 += float(column_C0G640[i])
mean_C0G640=sum_C0G640/len(column_C0G640)
if mean_C0G640 == 0:
    print (['C0G640','None'],)
else :
    print (['C0G640',mean_C0G640],)

sum_C0R190=0
target_data_C0R190 = list(filter(lambda item: item['station_id'] == 'C0R190', data))
column_C0R190 = [row['PRES'] for row in target_data_C0R190]
sum_C0R190=0
for i in range(len(column_C0R190)):
    if column_C0R190[i]== '-99.000':
        column_C0R190[i] = 0
    sum_C0R190 += float(column_C0R190[i])
mean_C0R190=sum_C0R190/len(column_C0R190)
if mean_C0R190 == 0:
    print (['C0R190','None'],)
else :
    print (['C0R190',mean_C0R190],)

sum_C0X260=0
target_data_C0X260 = list(filter(lambda item: item['station_id'] == 'C0X260', data))
column_C0X260 = [row['PRES'] for row in target_data_C0X260]
sum_C0X260=0
for i in range(len(column_C0X260)):
    if column_C0X260[i]== '-99.000':
        column_C0X260[i] = 0
    sum_C0X260 += float(column_C0X260[i])
mean_C0X260=sum_C0X260/len(column_C0X260)
if mean_C0X260 == 0:
    print (['C0X260','None'],)
else :
    print (['C0X260',mean_C0X260],)

