import matplotlib.animation as ani
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#source data directly from the web
df1 = pd.read_csv('FallSit_salinity.csv', delimiter=',', header='infer')
#columns = df1.columns
#first_row = df1.head(1).to_numpy()

depth_906 = df1['Logger_1081906_m'].to_numpy()
depth_083 = df1['Logger_1082083_m'].to_numpy()
depth_894 = df1['Logger_1081894_m'].to_numpy()
salinity_906 = df1['Logger_1081906_PSS'].to_numpy()
salinity_083 = df1['Logger_1082083_PSS'].to_numpy()
salinity_894 = df1['Logger_1081894_PSS'].to_numpy()



# plt.plot(x, y,'green')
plt.xlabel('Salinity')
plt.ylabel('Depth')
fig = plt.figure()

def buildmebarchart(i=int):
    # plt.legend(df1.columns)
    y=[depth_906[i],depth_083[i],depth_894[i]]
    x=[salinity_906[i],salinity_083[i],salinity_894[i]]
    p = plt.plot(x, y, 'blue')

animator = ani.FuncAnimation(fig, buildmebarchart, 10)
plt.show()