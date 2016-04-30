import os
import sys
import time 
from sort import Mergesort

if __name__ == '__main__':
    
    a = [f for f in os.listdir('.') if os.path.isfile(f)] # build array of files in current dir
    
    tic = time.time()  
    a = Mergesort.sort(a)
    toc = time.time()
    
    for e in a:
        print e
        
    print "Processing Time : %f s" % float(toc - tic)