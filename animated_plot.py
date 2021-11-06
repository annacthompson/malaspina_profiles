import matplotlib.animation as ani
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df1 = pd.read_csv('FallSit_salinity.csv', delimiter=',', header='infer')
# columns = df1.columns
# first_row = df1.head(1).to_numpy()

depth_906 = df1['Logger_1081906_m'].to_numpy()
depth_083 = df1['Logger_1082083_m'].to_numpy()
depth_894 = df1['Logger_1081894_m'].to_numpy()

salinity_906 = df1['Logger_1081906_PSS'].to_numpy()
salinity_083 = df1['Logger_1082083_PSS'].to_numpy()
salinity_894 = df1['Logger_1081894_PSS'].to_numpy()

# fig = plt.figure(1)

# def buildmebarchart(i=int):
#     # plt.legend(df1.columns)
#     plt.clf()
#     plt.xlabel('Salinity')
#     plt.ylabel('Depth')
#     plt.xlim(0,30)
#     y1=[depth_906[0:i],depth_083[0:i],depth_894[0:i]]
#     x1=[salinity_906[0:i],salinity_083[0:i],salinity_894[0:i]]
#     plt.plot(x1, y1, 'xkcd:sky blue', alpha=0.2)
#     y=[depth_906[i+1],depth_083[i+1],depth_894[i+1]]
#     x=[salinity_906[i+1],salinity_083[i+1],salinity_894[i+1]]
#     plt.plot(x, y, 'blue')

# animator = ani.FuncAnimation(fig, buildmebarchart, 50) #df1.size)


df1 = pd.read_csv('FallSit_temperature.csv', delimiter=',', header='infer')

temp_906 = df1['Logger_1081906_C'].to_numpy()
temp_393 = df1['SN_21099393'].to_numpy()
temp_365 = df1['SN_21099365'].to_numpy()
temp_398 = df1['SN_21099398'].to_numpy()
temp_083 = df1['Logger_1082083_C'].to_numpy()
temp_399 = df1['SN_21099399'].to_numpy()
temp_394 = df1['SN_21099394'].to_numpy()
temp_894 = df1['Logger_1081894_C'].to_numpy()

# depth_906 = df1['Logger_1081906_m'].to_numpy()
depth_393 = np.full((len(depth_906)), -3.7825)
depth_365 = np.full((len(depth_906)), -7.255)
depth_398 = np.full((len(depth_906)), -10.7275)
# depth_083 = df1['Logger_1082083_m'].to_numpy()
depth_399 = np.full((len(depth_906)), -19.2)
depth_394 = np.full((len(depth_906)), -21.7)
# depth_894 = df1['Logger_1081894_m'].to_numpy()

fig = plt.figure()

def buildmebarchart(i=int):
    # plt.legend(df1.columns)
    plt.clf()
    plt.xlabel('Temperature (C)')
    plt.ylabel('Depth (m)')
    plt.xlim(-1,30)
    y1=[depth_906[0:i],depth_393[0:i],depth_365[0:i],depth_398[0:i],depth_083[0:i],depth_399[0:i],depth_394[0:i],depth_894[0:i]]
    x1=[temp_906[0:i],temp_393[0:i],temp_365[0:i],temp_398[0:i],temp_083[0:i],temp_399[0:i],temp_394[0:i],temp_894[0:i]]
    plt.plot(x1, y1, 'xkcd:sky blue', alpha=0.1)
    y=[depth_906[i+1],depth_393[i+1],depth_365[i+1],depth_398[i+1],depth_083[i+1],depth_399[i+1],depth_394[i+1],depth_894[i+1]]
    x=[temp_906[i+1],temp_393[i+1],temp_365[i+1],temp_398[i+1],temp_083[i+1],temp_399[i+1],temp_394[i+1],temp_894[i+1]]
    plt.plot(x, y, 'blue')
    y2=[depth_906[i+1],depth_083[i+1],depth_894[i+1]]
    x2=[salinity_906[i+1],salinity_083[i+1],salinity_894[i+1]]
    plt.plot(x2, y2, 'orange')

animator = ani.FuncAnimation(fig, buildmebarchart, df1.size)

plt.show()
