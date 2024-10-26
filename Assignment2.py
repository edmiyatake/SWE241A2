# must be O(log(n)) therefore binary search
def firstInstance(nums,target):
    left,right,sol = 0,len(nums) - 1,-1
    while left <= right:
        mid = (left + right) // 2
        if target > nums[mid]:
        # if the target is in the upper half of the array
        # change left pointer
            left = mid + 1
        elif target < nums[mid]:
            right = mid - 1
        # if the target is in the lower half of the array
        # change right pointer
        else:
            sol = mid
            # but to guarantee that this is the first instance we keep should keep going down
            right = mid - 1
        # this should be the first instance?
    return sol

def lastInstance(nums,target):
    left,right,sol = 0,len(nums) - 1,-1
    while left <= right:
        mid = (left + right) // 2
        if target > nums[mid]:
        # if the target is in the upper half of the array
        # change left pointer
            left = mid + 1
        elif target < nums[mid]:
            right = mid - 1
        # if the target is in the lower half of the array
        # change right pointer
        else:
            sol = mid
            # but to guarantee that this is the last instance we keep should keep going up
            left = mid + 1

    return sol

def task1(nums,target):
    return [firstInstance(nums,target),lastInstance(nums,target)]

print("Assignment Examples")
nums = [4,9,10,13,17,17,19,21]
target = 17
print(f"nums = {nums}, target = {target} ")
print(f"Solution is {task1(nums,target)}\n")
nums1 = [2,4,6,8,10,14,16]
target1 = 12
print(f"nums = {nums1}, target = {target1} ")
print(f"Solution is {task1(nums1,target1)}\n")
nums2 = []
target2 = 0
print(f"nums = {nums2}, target = {target2} ")
print(f"Solution is {task1(nums2,target2)}\n")

print("Custom Test Cases")
print("Test both edges of the array")
print(f"nums = {[42,2,25,65,42]}, target = {42} ")
print(f"Solution is {task1([42,2,25,65,42],42)}\n")

print("Test one target instance in the array")
print(f"nums = {[22,2,25,65,76]}, target = {25} ")
print(f"Solution is {task1([22,2,25,65,76],25)}\n")

print("Test if target is not found")
print(f"nums = {[22,2,25,65,76]}, target = {72} ")
print(f"Solution is {task1([22,2,25,65,76],72)}\n")

print("Test two targets in the back of the array")
print(f"nums = {[22,2,25,65,76,97,97]}, target = {97} ")
print(f"Solution is {task1([22,2,25,65,76,97,97],97)}\n")

print("Test empty array")
print(f"nums = {[]}, target = {2} ")
print(f"Solution is {task1([],2)}\n")

