# must be O(log(n)) therefore binary search
def firstInstance(nums,target):
    left,right,sol = 0,len(nums) - 1,0
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
    left,right,sol = 0,len(nums) - 1,0
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

nums = [1,4,9,10,13,17,17,19,21]
nums2 = [12,45,98,102,102,102,179,192,210]
# first couple of bugs were because of the not sorted array => yikes
target = 102

print(f"This is the first instance: {firstInstance(nums2,target)}")
print(f"This is the last instance: {lastInstance(nums2,target)}")


