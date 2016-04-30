import random
from algolib.share.commons import less, exch

class Shuffle(object):
    
    '''
        Implements knuth shuffleing
    '''
    
    @classmethod
    def shuffle(cls, a):
        N = len(a)
        for i in xrange(N):
            r = random.randint(0, i)
            exch(a, i, r)

class Selection(object):
    
    @classmethod
    def sort(cls, a):
        N = len(a)
        for i in xrange(N):
            min = i
            for j in xrange(i + 1, N):
                if less(a[j], a[min]):
                    min = j
            exch(a, i, min) 

class Insertion(object):
        
    @classmethod
    def sort(cls, a):
       N = len(a)
       for i in xrange(0, N):
           for j in xrange(i, 0, -1): # i - 1 down to 0
               if less(a[j - 1], a[j]):
                   break
               else:
                   exch(a, j - 1, j)

'''
    TODO : fix mergesort not to return a
'''
class Mergesort(object):
    
    '''
        Mergesort using array slicing instead of separate index passing
    '''
    
    @classmethod
    def sort(cls, a):
        if len(a) == 1:
            return a
        else:
            mid = len(a) // 2 # integer division
            left = Mergesort.sort(a[ : mid])
            right = Mergesort.sort(a[mid : ])
            return Mergesort.__merge(left, right)
    
    @classmethod
    def __merge(cls, left, right):
        
        L = len(left)
        R = len(right)
        a = [None] * (L + R) # one way to create fixed sized (pre-allocate) array in python
        
        l = r = k = 0
        while((l < L) and (r < R)):
            if left[l] < right[r]:
                a[k] = left[l]
                l += 1
            elif left[l] > right[r]:
                a[k] = right[r]
                r += 1
            else:
                a[k] = left[l]
                k += 1
                l += 1
                a[k] = right[r]
                r += 1
            k += 1

        while(l < L):
            a[k] = left[l]
            l += 1
            k += 1
            
        while(r < R):
            a[k] = right[r]
            r += 1
            k += 1
            
        return a
        
class MergesortFix(object):
        
    @classmethod
    def sort(cls, a):
        aux = a[:]
        Mergesort.__sort(a, aux, 0, len(a) - 1)
        
    @classmethod
    def __sort(cls, a, aux, low, high):
        if high > low: 
            mid = (high - low) // 2 + low
            Mergesort.__sort(a, aux, low, mid)
            Mergesort.__sort(a, aux, mid + 1, high)
            Mergesort.__merge(a, aux, low, mid, high)
    
    @classmethod
    def __merge(cls, a, aux, low, mid, high):        
        i = low
        j = mid + 1
        for k in xrange(low, high + 1):
            if i > mid:
                a[k] = aux[j]
                j += 1
            elif j > high:
                a[k] = aux[i]
                i += 1
            elif Mergesort.__less(aux[j], aux[i]):
                a[k] = aux[j]
                j += 1
            else:
                a[k] = aux[i]
                i += 1
    
    @classmethod
    def __less(cls, v, w):
        return v < w

