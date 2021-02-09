"""
Number Binary-Repr  XOR-from-1-to-n
1         1           [0001]
2        10           [0011]
3        11           [0000]  <----- We get a 0
4       100           [0100]  <----- Equals to n
5       101           [0001]
6       110           [0111]
7       111           [0000]  <----- We get 0
8      1000           [1000]  <----- Equals to n
9      1001           [0001]
10     1010           [1011]
11     1011           [0000] <------ We get 0
12     1100           [1100] <------ Equals to n
"""
"""
# Approach 1
One straight forward solution can be to use a HashMap kind of data structure and iterate through the input:

If number is already present in HashMap, remove it.
If number is not present in HashMap, add it.
In the end, only number left in the HashMap is our required single number.
"""
# Approach 2
def find_single_number(arr):
    result = arr[0]
    for i in range(1, len(arr)):
        result ^= arr[i]
    return result

print(find_single_number([1, 4, 2, 1, 3, 2, 3])) #4
print(find_single_number([7, 9, 7])) #9