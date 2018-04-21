import matplotlib.pyplot as plt
from matplotlib.pyplot import Line2D
import numpy as np
'''2,6
4,5
10,9
5,8
7,5
9,3
8,8
4,8
1,9
5,10'''
x=[2,4,10,5,7,9,8,4,1,5]
y=[6,5,9,8,5,3,8,8,9,10]
#labels='frogs','hogs','dogs','logs'
sizes=15,20,45,10
#colors='yellowgreen','gold','lightskyblue','lightcoral'
#explode=0,0.1,0,0
#plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=50)
#plt.axis('equal')
#x = np.linspace(0, 10, 1000)
#fig=plt.figure(figsize=(10,10))

figure,ax=plt.subplots()
ax.set_xlim(left=0,right=11)
ax.set_ylim(bottom=0,top=11)
line1=[(x[1],y[1]),(x[5],y[5])]
(line1_xs,line1_ys)=zip(*line1)
ax.add_line(Line2D(line1_xs,line1_ys,linewidth=1,color='blue'))
for i in range(10):
    ax.scatter(x[i],y[i])#,color='red',label='point'+str(i))
plt.plot()
plt.show()