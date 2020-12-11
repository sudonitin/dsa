# another solution is to fill array from end (descending order) i.e. 
# both pointers will start from extreme points

# I fill array from beginning (ascending order)
# pointers start from middle
def ownLogic(nums):
    result = []
    positive, negative = 0,0
    if nums[0] < 0:
        while nums[negative] < 0:
            negative += 1
        positive = negative
        negative -= 1

        while negative >= 0 and positive < len(nums):
            if nums[negative] * -1 > nums[positive]:
                result.append(nums[positive])
                positive += 1
            elif nums[negative] * -1 == nums[positive]:
                result.append(nums[negative])
                result.append(nums[positive])
                positive += 1
                negative -= 1
            else:
                result.append(nums[negative])
                negative -= 1
        while positive < len(nums):
            result.append(nums[positive])
            positive += 1
        while negative >= 0:
            result.append(nums[negative])
            negative -= 1
        result = [i*i for i in result]
    else:
        result = [i*i for i in nums]
    return result

def main():
    nums = list(map(int, input().split(', ')))
    print(ownLogic(nums))
    return 1

main()