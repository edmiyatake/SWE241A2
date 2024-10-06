nums = [17,4,9,10,13,17,17,19,21]
target = 17


# must be O(log(n))
def search(nums,target):
    sol1,sol2 = None,None
    for i in range(0,len(nums) - 1):
        if nums[i] == target:
            sol1 = i
            break
    for i in range(len(nums) - 1,0,-1):
        if nums[i] == target:
            sol2 = i
            break
    return sol1,sol2

print(search(nums,target))
