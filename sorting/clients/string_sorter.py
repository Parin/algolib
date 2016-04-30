import sys
import time 
from sort import Mergesort

if __name__ == '__main__':
    
    input = sys.stdin.read() # read everything
    a = input.split() # tokenize to list
    
    tic = time.time()  
    Mergesort.sort(a)
    toc = time.time()
    
    # print first few elements of sorted elements
    for e in a:
        print(e)
        
    print "Processing Time : %f s" % float(toc - tic)
