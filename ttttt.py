f=open('D:\hedge\Desktop\cplex_out.txt')

outfilename='process_out.txt'
text=f.read()
text=text.replace('0\n                 ','0 ').replace('1\n                 ','1 ')
open(outfilename,'w').write(text)
