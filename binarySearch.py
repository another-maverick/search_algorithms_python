# O(logn) -- basically, how many times can n be divided by 2 until we get 1
# assumption is that list would be sorted
def binary_search(sorted_list, low, high, elem):
    if high >= 1:
        mid = (low + (high -1))//2
        if sorted_list[mid] == elem:
            return mid
        elif sorted_list[mid] > elem:
            return binary_search(sorted_list, low, mid-1, elem)
        else:
            return binary_search(sorted_list, mid+1, high, elem)
    else:
        return -1

if __name__ == '__main__':
    test = [1,2,3,4,5,6,7,8,9,10,11,12,13,4,15,16,17]
    elem = 16
    list_length = len(test)
    res = binary_search(test, 0,list_length-1, elem)
    print(f"Position of  {elem} on {test} is -----  {res}")
