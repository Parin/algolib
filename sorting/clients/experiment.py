import random
import sys
import time
from algolib.sorting.sort import Selection, Insertion, Mergesort

if __name__ == '__main__':
    
    random.seed(0)
    N = int(sys.argv[1])
    a = []
    
    for i in xrange(N):
        #a.append(random.uniform(0, 1))
        a.append(random.randint(0, 1000))
                  
    tic = time.time()  
    Mergesort.sort(a)
    toc = time.time()
    
    # print first few elements of sorted elements
    for e in a:
        print(e)
        
    print "Processing Time : %f s" % float(toc - tic)
        
        