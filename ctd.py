import csv
import os
from decimal import *
getcontext().prec = 15


def read_matrix(filename) :
    matrix = []
    with open('csv_raw/'+filename) as csvfile:
        annasreader = csv.reader(csvfile, delimiter=',')
        for row in annasreader:
            matrix.append(row)
    return matrix

def write_matrix(filename) :
    # TODO - writes a file called filename
    print('todo')

# tools
def matrix_transpose(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

def makecolumn(matrix,number):
    column = []
    for row in matrix:
        column.append(row[number])
    return column

def avg(array):
    total = 0
    for n in array :
        total = total + Decimal(n)
    return total / len(array)

#split the matrices
def general_info(fullmatrix) :
    out = fullmatrix[0:27]
    return out

def profile_data(fullmatrix) :
    return fullmatrix[29:]

#identify desired info in matrix
def cast_time_utc(profiledata):
    return profiledata[2][1]

def cast_time_local(profiledata):
    return profiledata[3][1]

def start_lat(profiledata):
    return profiledata[9][1]

def start_lon(profiledata):
    return profiledata[10][1]

def start_gps_horz_error(profiledata):
    return profiledata[12][1]

def end_lat(profiledata):
    return profiledata[15][1]

def end_lon(profiledata):
    return profiledata[16][1]

def end_gps_horz_error(profiledata):
    return profiledata[18][1]

def cast_duration(profiledata):
    return profiledata[21][1]

def depth(profiledata):
    return profiledata[-1][0]

def surface_temp(profiledata):
    return profiledata[0][2]

def min_temp(profiledata):
    a = makecolumn(profiledata,2)
    a=list(map(lambda x: Decimal(x), a))
    return min(a)

def max_temp(profiledata):
    a = makecolumn(profiledata,2)
    a=list(map(lambda x: Decimal(x), a))
    return max(a)

def avg_temp(profiledata):
    a = makecolumn(profiledata,2)
    a=list(map(lambda x: Decimal(x), a))
    return avg(a)

def min_salin(profiledata):
    a = makecolumn(profiledata,4)
    a=list(map(lambda x: Decimal(x), a))
    return min(a)

def max_salin(profiledata):
    a = makecolumn(profiledata,4)
    a=list(map(lambda x: Decimal(x), a))
    return max(a)

def avg_salin(profiledata):
    a = makecolumn(profiledata,4)
    a=list(map(lambda x: Decimal(x), a))
    return avg(a)

#build output matrix
output_matrix = []

for filename in os.listdir('csv_raw_test'):
    if filename.endswith(".csv"): 
        current_matrix = read_matrix(filename)
        general_info_matrix = general_info(current_matrix)
        profile_data_matrix = profile_data(current_matrix)

        output_matrix.append([
            filename,
            cast_time_utc(general_info_matrix),
            cast_time_local(general_info_matrix),
            start_lat(general_info_matrix),
            start_lon(general_info_matrix),
            start_gps_horz_error(general_info_matrix),
            end_lat(general_info_matrix),
            end_lon(general_info_matrix),
            end_gps_horz_error(general_info_matrix),
            cast_duration(general_info_matrix),
            depth(profile_data_matrix),
            surface_temp(profile_data_matrix),
            min_temp(profile_data_matrix),
            max_temp(profile_data_matrix),
            avg_temp(profile_data_matrix),
            min_salin(profile_data_matrix),
            max_salin(profile_data_matrix),
            avg_salin(profile_data_matrix),
        ])

# https://docs.python.org/3/library/decimal.html

#add headers
headers = ['filename','cast_time_utc', 'cast_time_local', 'start_lat', 'start_lon', 'start_gps_horz_error', 'end_lat', 'end_lon', 'end_gps_horz_error','cast_duration', 'depth', 'surface_temp', 'min_temp','max_temp', 'avg_temp', 'min_spec_cond','max_spec_cond', 'avg_spec_cond']
output_matrix.insert(0,headers)

for row in output_matrix :
    print(row)
print("\n")

#create new .csv file
with open("ctdcastdata.csv", "w", newline="") as f:
   writer = csv.writer(f)
   writer.writerows(output_matrix)
