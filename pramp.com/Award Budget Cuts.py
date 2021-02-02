# 4/6 cases solved
# def find_grants_cap(grantsArray, newBudget):
#   # your code goes here
#   capAlloted = []
#   count = 0
#   for i in grantsArray:
#     #print("numerator", newBudget)
#     #print("denominator", (len(grantsArray)-count))
#     #print("num/den", float(newBudget) / float(len(grantsArray)-count))
#     atTheMostForEachGrant = float(newBudget) / float(len(grantsArray)-count)
#     capForIthGrant = min(atTheMostForEachGrant, i)
#     capAlloted.append(capForIthGrant)
#     newBudget -= capForIthGrant
#     #print(newBudget, i, atTheMostForEachGrant, capForIthGrant)
#     count += 1
#   print(capAlloted)
#   return capForIthGrant

'''
OUTPUT:
Actual:
[170.0, 170.0, 150, 173.33333333333334, 130, 110, 208.88888888888889, 208.88888888888886, 117]
117
Expected: 211
'''

# REFERRED FROM LEETCODE
# https://leetcode.com/discuss/interview-question/351313/Google-or-Phone-Screen-or-Salary-Adjustment/318386
def find_grants_cap(grantsArray, newBudget):
    grantsArray.sort(reverse=True)
    skipped, i = 1, 0
    while i+1 < len(grantsArray):
        k = float(newBudget - sum(grantsArray[i+1:])) / float(skipped)
        if not k < grantsArray[i+1]:
            return k
        skipped += 1
        i += 1
    if i < len(grantsArray) and k < grantsArray[i]:
        k = float(newBudget) / float(skipped)
    return k


# print(find_grants_cap([2, 4], 3)) #1.5
# print(find_grants_cap([2,4,6], 3)) #1
# print(find_grants_cap([2,100,50,120,167], 400)) #128
# print(find_grants_cap([2,100,50,120,1000], 190)) #47
# print(find_grants_cap([21,100,50,120,130,110], 140)) #23.8
# print(find_grants_cap([210,200,150,193,130,110,209,342,117], 1530))

# TRY THIS OUT
# https://leetcode.com/discuss/interview-question/351313/Google-or-Phone-Screen-or-Salary-Adjustment/318336