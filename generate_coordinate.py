import random
import matplotlib.pyplot as plt
from matplotlib.pyplot import Line2D
import numpy as np

def get_dist():
    dist = [[0] * (tot + 1) for i in range(tot + 1)]

    for i in range(tot):
        for j in range(tot):
            dist[i + 1][j + 1] = round(np.sqrt(
                np.square(coord_list[i][0] - coord_list[j][0]) + np.square(coord_list[i][1] - coord_list[j][1])), 2)

    for j in range(tot):
        dist[0][j + 1] = round(np.sqrt(np.square(coord_list[j][0]) + np.square(coord_list[j][1])), 2)

    for i in range(tot + 1):
        for j in range(tot + 1):
            print dist[i][j],
        print ''
    f = open('coordinate.txt', 'a')
    f.write(str(dist))
def plot():
    figure, ax = plt.subplots()
    ax.set_xlim(left=0, right=tot*1.3)
    ax.set_ylim(bottom=0, top=tot*1.3)
    for i in range(tot):
        ax.scatter(coord_list[i][0], coord_list[i][1])
    plt.plot()
    plt.show()

tot=100
coord_list=[]
for i in range(tot):
    x=random.randint(tot*0.2,tot*1.2)
    y=random.randint(tot*0.2,tot*1.2)
    coord_list.append([x,y])
print coord_list
f=open('coordinate.txt','w')
f.write(str(coord_list))
f.close()
get_dist()



