import re

f=open('D:\hedge\Desktop\cplex_out.txt')

outfilename='process_out.txt'
text=f.read()
text=text.replace('0\n                 ','0 ').replace('1\n                 ','1 ')
open(outfilename,'w').write(text)

infile='process_out.txt'
f=open(infile,'r')
lines=f.readlines()
count=0
driver_count=50
car_rout=[[0] for i in range(driver_count)]
for line in lines:
    ijk=re.findall('(?<=\[)\d.*?(?=\])',line)[0]
    ijk_list=ijk.split(' ')
    try:
        i=int(count/102)
        j=int(count%102)
        if i==0 and j==101:
            k=0
            for ijk in ijk_list:
                if ijk =='1':
                    string = '|' + str(i) + ',' + str(j)
                    car_rout[k].append(string)
                    print 'line=', count,
                    print 'i=', i, 'j=', j, 'k=', k
                k+=1

        else:
            k = ijk_list.index('1')
            string='|'+str(i)+','+str(j)
            car_rout[k].append(string)
            print 'line=',count,
            print 'i=',i,'j=',j,'k=',k
    except:
        pass
    count+=1
    #if count>102:
    #    break
for i in range(driver_count):
    print car_rout[i]