# My fn handles the code if intervals are interchanged
def findIntersection(nums1, nums2):
    if nums1[0][0] > nums2[0][0]:
        nums1,nums2 = nums2,nums1
    p1, p2 = 0, 0
    size1, size2 = len(nums1), len(nums2)
    result = []
    # apply condition if b.start <= a.end
    # intersection = [max(a.start, b.start), min(a.end, b.end)]
    while p1 < size1 and p2 < size2:
        if nums2[p2][0] <= nums1[p1][1]:
            result.append([max(nums1[p1][0], nums2[p2][0]), min(nums2[p2][1], nums1[p1][1])])
            p2 += 1
        p1 += 1
    while p1 < size1:
        if nums2[size2-1][0] <= nums1[p1][1]:
            result.append([max(nums1[p1][0], nums2[size2-1][0]), min(nums2[size2-1][1], nums1[p1][1])])
        p1 += 1
    while p2 < size2:
        if nums2[p2][0] <= nums1[size1-1][1]:
            result.append([max(nums1[size1-1][0], nums2[p2][0]), min(nums2[p2][1], nums1[size1-1][1])])
        p2 += 1
    return result


def main():
    nums1 = [[1, 3], [5, 7], [9, 12]]
    nums2 = [[5, 10]]
    # nums1 = [[1, 3], [5, 6], [7, 9]]
    # nums2 = [[2, 3], [5, 7]]
    nums = findIntersection(nums1, nums2)
    print(nums)

main()