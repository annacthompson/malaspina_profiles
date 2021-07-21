import csv
import os

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

def general_info(fullmatrix) :
    out = fullmatrix[0:27]
    return out

def profile_data_column_names(fullmatrix) :
    return fullmatrix[28]

def profile_data(fullmatrix) :
    return fullmatrix[30:]

def cast_time(generalinfo):
    return generalinfo[2][1]

output_matrix = []

for filename in os.listdir('csv_raw'):
    current_matrix = read_matrix(filename)
    output_matrix.append(cast_time(current_matrix))

# https://docs.python.org/3/library/decimal.html

print(output_matrix)