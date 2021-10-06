import csv
import matplotlib.pyplot as plt
import numpy as np
from ctd import * 

def read_matrix1(filename) :
    matrix = []
    with open(filename) as csvfile:
        annasreader = csv.reader(csvfile, delimiter=',')
        for row in annasreader:
            matrix.append(row)
    return matrix

ann=read_matrix1('ctdcastdata_annotated.csv')
filenames = makecolumn(ann,3)
sitkagi = filenames[1:16]
backdoor = filenames[16:25]
backdoor.append('CC1838007_20210705_214726.csv')
backdoor.append('CC1838007_20210705_220644.csv')
backdoor.append('CC1838007_20210705_225753.csv')
malaspina = filenames[42:81]
intermediate = filenames[25:42]
OIDs = makecolumn(ann,1)
OIDs = filenames[1:len(filenames)]

print('filenames=', filenames)
print('sitkagki=', sitkagi)
print('backdoor=', backdoor)
print('malaspina=', malaspina)
print('intermediate=', intermediate)

Sspcon_map = {}
Stemp_map = {}
Sdepth_map = {}
Bspcon_map = {}
Btemp_map = {}
Bdepth_map = {}
Mspcon_map = {}
Mtemp_map = {}
Mdepth_map = {}
Ispcon_map = {}
Itemp_map = {}
Idepth_map = {}
for filename in sitkagi:
    m = read_matrix(filename)
    m=profile_data(m)
    Sspcon_map[filename] = makecolumn(m,4)
    Stemp_map[filename] = makecolumn(m,2)
    Sdepth_map[filename] = makecolumn(m,0)
for filename in backdoor:
    m = read_matrix(filename)
    m=profile_data(m)
    Bspcon_map[filename] = makecolumn(m,4)
    Btemp_map[filename] = makecolumn(m,2)
    Bdepth_map[filename] = makecolumn(m,0)
for filename in malaspina:
    m = read_matrix(filename)
    m=profile_data(m)
    Mspcon_map[filename] = makecolumn(m,4)
    Mtemp_map[filename] = makecolumn(m,2)
    Mdepth_map[filename] = makecolumn(m,0)
for filename in intermediate:
    m = read_matrix(filename)
    m=profile_data(m)
    Ispcon_map[filename] = makecolumn(m,4)
    Itemp_map[filename] = makecolumn(m,2)
    Idepth_map[filename] = makecolumn(m,0)    
        
##Salinity Profile
fig, ax = plt.subplots()
keys=Mspcon_map.keys()
for key in keys:
    x=Mspcon_map[key]
    y=Mdepth_map[key]
    x = np.asarray(x, dtype=np.float64)
    x = np.array(x)
    y = np.asarray(y, dtype=np.float64)
    y = np.array(y)
    y = y*-1
    ax.plot(x, y,'green')
ax.set(xlabel='Specific Conductance (uS/cm)', ylabel='Depth (m)',
       title='Malaspina')
ax.grid()

# fig, ax = plt.subplots()
keys=Sspcon_map.keys()
for key in keys:
    x=Sspcon_map[key]
    y=Sdepth_map[key]
    x = np.asarray(x, dtype=np.float64)
    x = np.array(x)
    y = np.asarray(y, dtype=np.float64)
    y = np.array(y)
    y = y*-1
    ax.plot(x, y,'red')
ax.set(xlabel='Specific Conductance (uS/cm)', ylabel='Depth (m)',
       title='Sitkagi')
ax.grid()

# lake='B'
# fig, ax = plt.subplots()
# keys=lake+'spcon_map'.keys()
# for key in keys:
#     y=Bdepth_map[key]
#     x = np.array(np.asarray(Bspcon_map[key], dtype=np.float64))
#     y = np.array(np.asarray(Bdepth_map[key], dtype=np.float64))*-1
#     ax.plot(x, y,'blue')
# ax.set(xlabel='Specific Conductance (uS/cm)', ylabel='Depth (m)',title='Backdoor')
# ax.grid()

# fig, ax = plt.subplots()
keys=Ispcon_map.keys()
for key in keys:
    x=Ispcon_map[key]
    y=Idepth_map[key]
    x = np.asarray(x, dtype=np.float64)
    x = np.array(x)
    y = np.asarray(y, dtype=np.float64)
    y = np.array(y)
    y = y*-1
    ax.plot(x, y,'blue')
ax.set(xlabel='Specific Conductance (uS/cm)', ylabel='Depth (m)',
       title='Malaspina Triangle')
ax.grid()

# fig, ax = plt.subplots()
keys=Bspcon_map.keys()
for key in keys:
    x=Bspcon_map[key]
    y=Bdepth_map[key]
    x = np.asarray(x, dtype=np.float64)
    x = np.array(x)
    y = np.asarray(y, dtype=np.float64)
    y = np.array(y)
    y = y*-1
    ax.plot(x, y,'orange')
ax.set(xlabel='Specific Conductance (uS/cm)', ylabel='Depth (m)',
       title='Backdoor')
ax.grid()

#Legend
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
red_patch = mpatches.Patch(color='red', label='Sitkagi Lagoon')
green_patch = mpatches.Patch(color='green', label='Malaspina Lake')
blue_patch = mpatches.Patch(color='blue', label='unnamed lake')
orange_patch = mpatches.Patch(color='orange', label='Backdoor Lake')
plt.legend(handles=[red_patch, orange_patch, green_patch, blue_patch])

ax.set(xlabel='Specific Conductance (uS/cm)', ylabel='Depth (m)', title='Saltwater Intrusion')

#fig.savefig("test.png")
plt.show()

print(keys)


##Temperature Profile
fig, ax = plt.subplots()
keys=Mtemp_map.keys()
for key in keys:
    x=Mtemp_map[key]
    y=Mdepth_map[key]
    x = np.asarray(x, dtype=np.float64)
    x = np.array(x)
    y = np.asarray(y, dtype=np.float64)
    y = np.array(y)
    y = y*-1
    ax.plot(x, y,'green')
ax.set(xlabel='Specific Conductance (uS/cm)', ylabel='Depth (m)',
       title='Malaspina')
ax.grid()

# fig, ax = plt.subplots()
keys=Itemp_map.keys()
for key in keys:
    x=Itemp_map[key]
    y=Idepth_map[key]
    x = np.asarray(x, dtype=np.float64)
    x = np.array(x)
    y = np.asarray(y, dtype=np.float64)
    y = np.array(y)
    y = y*-1
    ax.plot(x, y,'blue')
ax.set(xlabel='Specific Conductance (uS/cm)', ylabel='Depth (m)',
       title='Malaspina Triangle')
ax.grid()

# fig, ax = plt.subplots()
keys=Btemp_map.keys()
for key in keys:
    x=Btemp_map[key]
    y=Bdepth_map[key]
    x = np.asarray(x, dtype=np.float64)
    x = np.array(x)
    y = np.asarray(y, dtype=np.float64)
    y = np.array(y)
    y = y*-1
    ax.plot(x, y,'orange')
ax.set(xlabel='Specific Conductance (uS/cm)', ylabel='Depth (m)',
       title='Backdoor')
ax.grid()

# fig, ax = plt.subplots()
keys=Stemp_map.keys()
for key in keys:
    x=Stemp_map[key]
    y=Sdepth_map[key]
    x = np.asarray(x, dtype=np.float64)
    x = np.array(x)
    y = np.asarray(y, dtype=np.float64)
    y = np.array(y)
    y = y*-1
    ax.plot(x, y,'red')
ax.set(xlabel='Temp', ylabel='Depth (m)',
       title='Sitkagi')
ax.grid()

#Legend
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
red_patch = mpatches.Patch(color='red', label='Sitkagi Lagoon')
green_patch = mpatches.Patch(color='green', label='Malaspina Lake')
blue_patch = mpatches.Patch(color='blue', label='unnamed lake')
orange_patch = mpatches.Patch(color='orange', label='Backdoor Lake')
plt.legend(handles=[red_patch, orange_patch, green_patch, blue_patch])

ax.set(xlabel='Temperature (\N{DEGREE SIGN}C)', ylabel='Depth (m)', title='Temperature Profiles')

#fig.savefig("test.png")
plt.show()