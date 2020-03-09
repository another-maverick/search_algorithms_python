# O(n)
def linear_search(inp_list, elem):
    list_length = len(inp_list)
    for i in range(list_length):
        if inp_list[i] == elem:
            return i
    return -1



if __name__ == '__main__':
    test = [1,2,3,4,5,6,7,8,9,10,11,12,13,4,15,16,17]
    elem = 16
    res = linear_search(test, elem)
    print(f"Position of  {elem} on {test} is -----  {res}")

