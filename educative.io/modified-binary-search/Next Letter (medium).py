def next_letter(string, key):
    if key >= string[len(string)-1]:
        return string[0]
    start, end = 0, len(string)-1
    middle = (start+end)//2
    smallest_greater = " "
    while start <= end:
        # b >= c
        if key >= string[middle]:
            start = middle + 1
            middle = (start+end)//2
        elif key < string[middle]:
            smallest_greater = max(smallest_greater, string[middle])
            end = middle-1
            middle = (start+end)//2
    return smallest_greater

print(next_letter(['a', 'c', 'f', 'h'], "f"))
print(next_letter(['a', 'c', 'f', 'h'], "b"))
print(next_letter(['a', 'c', 'f', 'h'], "m"))
print(next_letter(['a', 'c', 'f', 'h'], "h"))