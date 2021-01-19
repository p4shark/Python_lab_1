import glob
import sys
wr = open('test\output.txt','w+')
i=0
path ='test\*.dat'
for f in glob.glob(path):
     max = sys.float_info.min
     with open(f, 'r') as f1:
      for s in f1:
       s=s[15:28]
       s = s.replace('D', 'E')
       s = float(s)
       print s
       if (s>max): max=s
     i=i+1
     wr.write('Max in 2 column in '+str(i)+' file: '+str(max)+'\n')
wr.close()
