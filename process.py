import numpy
length=100
infilename='point_int.csv'
fin=open(infilename,'r')
lines=fin.readlines()

point_list=[[0]*3 for j in range(length+2)]
i=1
point_list[0][1]=0
point_list[0][2]=0
for line in lines:
    if i!=1:
        paras=line.split(',')
        point_list[i-1][0]=int(paras[1])##  time
        point_list[i-1][1]=int(paras[3])##  x
        point_list[i-1][2]=int(paras[4])##  y
    i+=1
point_list[length+1][1]=0
point_list[length+1][2]=0
print point_list
print '\n\n\n>>>>>>>>>>>>>>>>>>>>>>   x'
for i in range(length+2):
    print str(point_list[i][1])+',',

print '\n\n\n>>>>>>>>>>>>>>>>>>>>>>   y'
for i in range(length+2):
    print str(point_list[i][2])+',',

print '\n\n\n>>>>>>>>>>>>>>>>>>>>>>   time'
for i in range(length+2):
    print str(point_list[i][0])+',',

print '\n\n\n>>>>>>>>>>>>>>>>>>>>>>   time+30'
for i in range(length+2):
    print str(point_list[i][0]+30)+',',



distance=[]
for i in range(length+2):
    distance.append(str(numpy.sqrt(numpy.square(point_list[i][1])+numpy.square(point_list[i][2])))[0:5])
print '\n\n\n>>>>>>>>>>>>>>>>>>>>>>distance'
for i in range(length+2):
    print distance[i]+',',


print '\n\n\n>>>>>>>>>>>>>>>>>>>>>>   expect time'
for i in range(length + 2):
    print str(point_list[i][0]+float(distance[i])/3)[0:6] + ',',

print '\n\n\n>>>>>>>>>>>>>>>>>>>>>>   expect time plus'
for i in range(length + 2):
    print str(30+point_list[i][0]+float(distance[i])/3)[0:6] + ',',


print '\n\n\n>>>>>>>>>>>>>>>>>>>>>>between distance'
bdistance=[[0]*(length+2) for i in range(length+2)]
for i in range(length+2):
    for j in range(length+2):
        bdistance[i][j]=str(numpy.sqrt(numpy.square(point_list[i][1]-point_list[j][1])+numpy.square(point_list[i][2]-point_list[j][2])))[0:5]
        #bdistance[i][j]=0
    print '[',
    for j in range(length+2):
        if j==length+1:
            print 0,
        else:
            print bdistance[i][j]+',',
    print '],'

