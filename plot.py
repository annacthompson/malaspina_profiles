import csv
import matplotlib.pyplot as plt
import numpy as np
from ctd import * 

m=read_matrix('CC1838007_20210628_211915.csv')
m=profile_data(m)

# Data for plotting
x = makecolumn(m,4)
y = makecolumn(m,0)

x = np.asarray(x, dtype=np.float64)
x = np.array(x)
y = np.asarray(y, dtype=np.float64)
y = np.array(y)
y = y*-1

print(x)
print(y)

fig, ax = plt.subplots()
ax.plot(x, y)

ax.set(xlabel='Specific Conductance (uS/cm)', ylabel='Depth (m)',
       title=filename)
ax.grid()

#fig.savefig("test.png")
plt.show()

