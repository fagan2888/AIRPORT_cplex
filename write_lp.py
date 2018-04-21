import numpy
length=10
filename='vrp.lp'
infilename='small.csv'
fin=open(infilename,'r')
lines=fin.readlines()

point_list=[[0]*3 for i in range(length+2)]
i=1
point_list[0][1]=0
point_list[0][2]=0
for line in lines:
    paras=line.split(',')
    point_list[i][0]=int(paras[1])##  time
    point_list[i][1]=int(paras[2])##  x
    point_list[i][2]=int(paras[3])##  y
    i+=1
point_list[11][1]=0
point_list[11][2]=0
print point_list

distance=[]
for i in range(length+1):
    distance.append(numpy.sqrt(numpy.square(point_list[i][1])+numpy.square(point_list[i][2])))
print distance

bdistance=[[0]*12 for i in range(12)]
for i in range(12):
    for j in range(12):
        bdistance[i][j]=str(numpy.sqrt(numpy.square(point_list[i][1]-point_list[j][1])+numpy.square(point_list[i][2]-point_list[j][2])))[0:4]
        #bdistance[i][j]=0
    for j in range(12):
        print bdistance[i][j]+',',
    print ''
#print bdistance
f=open(filename,'w')
f.truncate()
f.close()
f=open(filename,'a')
string='''
\ENCODING=ISO-8859-1
\Problem name: VRP'
Minimize
obj: '''
'''
for i in range(10):
    for j in range(10):
        for k in range(10):
            string+=(str(bdistance[i][j])+' x'+str(i)+str(j)+str(k)+'+')
string=string[:-1]+'\nSubject To'
print string

for i in range(10):
    for j in range(10):
        if i>j:
            for k in range(10):
                #print bdistance[i][j],'*x',i,j,k
                pass
                '''
'''
Minimize
 obj: x1 + 2 x2 + 3 x3
Subject To
 c1: - x1 + x2 + x3  = 20
 c2: x1 - 3 x2 + x3 <= 30
 c3: x1 + x2 + x3 >= 40
Bounds
 0 <= x1 <= 40
 0 <= x2 <= 60
 0 <= x3 <= 90
End

'''