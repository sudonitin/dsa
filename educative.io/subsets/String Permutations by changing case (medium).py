def generatePermutations(string):
    result = [string]
    charIndex = 0
    while charIndex < len(string): # O(n) Traversing original string of length n
        resultLen = len(result)
        for i in range(resultLen): # O(2^N) result array size increase by 2^N for each string
            if result[i][charIndex].isalpha():
                temp = list(result[i])
                temp[charIndex] = temp[charIndex].swapcase()
                result.append(''.join(temp))
            else:
                break
        charIndex += 1
    return result

# print(generatePermutations("ad52"))
print(generatePermutations("ab7c"))
