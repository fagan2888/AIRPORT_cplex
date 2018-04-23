import random
import matplotlib.pyplot as plt
from matplotlib.pyplot import Line2D
import numpy as np


coord_list=[]
for i in range(20):
    x=random.randint(2,12)
    y=random.randint(2,12)
    coord_list.append([x,y])
print coord_list

figure,ax =plt.subplots()
ax.set_xlim(left=0,right=13)
ax.set_ylim(bottom=0,top=13)
for i in range(20):
    ax.scatter(coord_list[i][0],coord_list[i][1])
plt.plot()
plt.show()