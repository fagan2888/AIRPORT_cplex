import re
infile='cp_out.txt'
f=open(infile,'r')
lines=f.readlines()
count=0
car_rout=[[0] for i in range(40)]
for line in lines:
    ijk=re.findall('(?<=\[)\d.*?(?=\])',line)[0]
    ijk_list=ijk.split(' ')
    try:
        k=ijk_list.index('1')
        i=int(count/102)
        j=int(count%102)+1
        string='|'+str(i)+','+str(j)
        car_rout[k].append(string)
        print 'line=',count
        print i,j,k
    except:
        pass
    count+=1
    #if count>102:
    #    break
for i in range(40):
    print car_rout[i]