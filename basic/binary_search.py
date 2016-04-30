import numpy as np

class BinarySearch(object):
    
    @classmethod
    def search(cls, sorted_array, key):
        #return BinarySearch.__search_rec__(sorted_array, 0, len(sorted_array) - 1, key)
        return BinarySearch.__search__(sorted_array, key)
        
    # Iterative method
    @classmethod
    def __search__(cls, a, key):
        low = 0
        high = len(a) - 1
        while not (high < low):
            mid = (high - low) // 2 + low
            if key < a[mid]:
                high = mid - 1 # look in left subproblem
            elif key > a[mid]:
                low = mid + 1 # look in right subproblrm
            else:
                return mid # sreach hit
        return low # sreach miss - return index where not found key would get inserted
        
    
    # recursive method  
    @classmethod
    def __search_rec__(cls, a, low, high, key):
        if high < low:
            return low
        else:
            mid = (high - low) // 2 + low
            if key < a[mid]:
                return BinarySearch.__search_rec__(a, low, mid - 1, key)
            elif key > a[mid]:
                return BinarySearch.__search_rec__(a, mid + 1, high, key)
            else:
                return mid
        
if __name__ == '__main__':
    
    np.random.seed(0)
    low = 0
    high = 99
    samples = 10
    
    sorted_array = list(np.sort(np.random.randint(low, high, samples)))
    print sorted_array
    key = BinarySearch.search(sorted_array, 100)
    print(key)