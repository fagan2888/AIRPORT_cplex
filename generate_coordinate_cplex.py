import random
import matplotlib.pyplot as plt
from matplotlib.pyplot import Line2D
import numpy as np


def get_time_window(dist):
    global dat_string
    twa=[0]
    twb=[tot*5+100]
    for i in range(tot):
        twa.append(float(str(dist[0][i+1]*3+time_list[i+1])))
        twb.append(float(str(dist[0][i+1]*3*1.3+time_list[i+1])))
    twa.append(tot*5)
    twb.append(float(str(tot*5+100)[0:5]))
    dat_string+='time_window_a='+str(twa)+';'
    dat_string+='\ntime_window_b='+str(twb)+';'
    '''
    print 'float time_window_a[I]=',
    print twa,
    print ';\n\nfloat time_window_b[I]=',
    print twb,
    print ';'
    '''
def get_dist():
    global dat_string
    dist = [[0] * (tot + 1) for i in range(tot + 1)]
    for i in range(tot):
        for j in range(tot):
            dist[i + 1][j + 1] = round(np.sqrt(
                np.square(coord_list[i][0] - coord_list[j][0]) + np.square(coord_list[i][1] - coord_list[j][1])), 2)

    for j in range(tot):
        dist[0][j + 1] = round(np.sqrt(np.square(coord_list[j][0]) + np.square(coord_list[j][1])), 2)
    dat_string +='\ndistance=['
    for i in range(tot + 1):
        dat_string+='['
        for j in range(tot + 1):
            dat_string+= str(dist[i][j])+ ','
        dat_string+= '0],\n'
    dat_string+= '[' + '0.0, ' * (tot + 1) + '0]];\n'
    '''
    #####output the dist array
    print '\nfloat distance[0..tot+1][0..tot+1]=['
    for i in range(tot + 1):
        print'[',
        for j in range(tot+1):
            print dist[i][j],',',
        print '0],'
    print '['+'0, '*(tot+1)+'0]];\n'
    f = open('coordinate_cplex.txt', 'a')
    f.write(str(dist))
    '''
    get_time_window(dist)

def plot():
    figure, ax = plt.subplots()
    ax.set_xlim(left=0, right=tot*1.3)
    ax.set_ylim(bottom=0, top=tot*1.3)
    for i in range(tot):
        ax.scatter(coord_list[i][0], coord_list[i][1])
    plt.plot()
    plt.show()
def get_time_list():
    global dat_string
    tot_time = tot * 5
    time_list = [0]
    for i in range(tot):
        time_list.append(random.randint(0, tot_time))
    time_list.append(0)
    #print 'float arrive_time[I]=',time_list,';'
    dat_string +='\narrive_time='+str(time_list)+';'
    return time_list

###################
tot=10
dat_file='D:\hedge\opl\learn_cplex\\vrptw_airport.dat'
###################
coord_list=[]
for i in range(tot):
    x=random.randint(round(tot*0.2),round(tot*1.2))
    y=random.randint(round(tot*0.2),round(tot*1.2))
    coord_list.append([x,y])
#print 'coordinate=======',coord_list
f=open('coordinate_cplex.txt','w')
f.write(str(coord_list))
f.close()

global dat_string
dat_string='//*************************************\n//coordinate='+str(coord_list)+'\n//*************************************'

time_list=get_time_list()
get_dist()
print dat_string

f=open(dat_file,'w')
f.write(dat_string)
f.close()


