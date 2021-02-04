# a[:i+1] + [newElem] + a[i+1:]
def getPermuatationOfSet(result, givenSet):
    if len(result[0]) == len(givenSet):
            # print(result)
            return result
    elif len(result[0]) == 0:
        return getPermuatationOfSet([[givenSet[0]]], givenSet)
    else:
        newResult = []
        newElem = givenSet[len(result[0])]
        for i in range(len(result)):
            for j in range(-1, len(result[i])):
                newResult.append(result[i][:j+1] + [newElem] + result[i][j+1:])
        # print(newResult, "#")
        return getPermuatationOfSet(newResult, givenSet)

print(getPermuatationOfSet([[]], [1,2,3]))