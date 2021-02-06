# read the logic and framed the solution by myself

from copy import deepcopy
def find_balanced_parantheses(n):
    result = [{"braces": "(", "openCount": n - 1, "closedCount": n}]
    while True:
        resultLen = len(result)
        newResult = []
        for i in range(resultLen):
            temp = deepcopy(result[i])
            # check if open brace can be pushed
            if temp["openCount"] > 0:
                temp["braces"] += "("
                temp["openCount"] -= 1
                newResult.append(temp)
            temp = deepcopy(result[i])
            # check if closed condition matches
            if temp["closedCount"] > temp["openCount"]:
                temp["braces"] += ")"
                temp["closedCount"] -= 1
                newResult.append(temp)
        result = newResult
        if result[0]["openCount"] == 0 and result[0]["closedCount"] == 0:
            return [res["braces"] for res in result]

print(find_balanced_parantheses(4))