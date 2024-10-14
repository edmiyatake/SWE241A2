# give an m by n int matrix
# - non decreasing order
# - the first in is guaranteed higher than the last index of the lower array
# first I want to iterate through the whole array
matrix = [[1,2,3,4],[5,7,9,11,13,23],[24,28,32,64,65],[77,102,232,444]]
target = 3
# for row in matrix:
#     for num in row:
#         print(num)
def binarySearch(matrix,target):
    left,right,down = 0,len(matrix),0
    # Check base case
    if high >= low:

        mid = low + (high - low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, low, mid-1, x)

        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, high, x)

    # Element is not present in the array
    else:
        return -1


