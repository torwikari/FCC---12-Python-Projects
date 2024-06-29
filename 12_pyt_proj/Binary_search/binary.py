# This program will prove that binary search is faster than naive search.
import random
import time
# naive search: scan entire list and ask if it's equal to the target.
# if yes, return the index
# if no, then return -1

def naive_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1
    
def binary_search(list, target, low=None, high=None):
    if low is None: 
        low = 0
    if high is None:
        high = len(list) - 1
    if high < low:
        return -1
        
    midpoint = (low + high) // 2
    
    if list[midpoint] == target:
        return midpoint
    elif target < list[midpoint]:
        return binary_search(list, target, low, midpoint-1)
    else:
        return binary_search(list, target, midpoint+1, high)
    
if __name__ == '__main__':
    l = [1, 3, 5, 10, 12]
    target = 10
    print(naive_search(l, target))
    print(binary_search(l, target))
    
    
    lenght = 10000
    sorted_list = set()
    while len(sorted_list) < lenght:
        sorted_list.add(random.randint(-3*lenght, 3*lenght))
    sorted_list = sorted(list(sorted_list))
    
start = time.time()
for target in sorted_list:
    naive_search(sorted_list, target)
    end = time.time()
print("Naive search time: ", (end - start)/ lenght, "seconds")

start = time.time()
for target in sorted_list:
    binary_search(sorted_list, target)
    end = time.time()
print("Binary search time: ", (end - start)/ lenght, "seconds")