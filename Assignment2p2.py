# give an m by n int matrix
# - non decreasing order
# - the first in is guaranteed higher than the last index of the lower array
# first I want to iterate through the whole array
def binarySearch(matrix,target):
    row = len(matrix)
    col = len(matrix[0])
    len1d = row * col - 1
    left,right = 0,len1d
    while left <= right:
        mid = (left + right) // 2
        currRow = mid // col
        currCol = mid % col
        if target > matrix[currRow][currCol]:
            left = mid + 1
        elif target < matrix[currRow][currCol]:
            right = mid - 1
        else:
            return True
    return False

# test cases given in the assigneemnt
print("Assignment Examples")
matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target1 = 3 # works all good
target2 = 23 # checking edges of arrays front/back
target3 = 1
target4 = 60 # checking if edge case doesn't go out of bounds
target5 = 4 #checking if invalid values return -1
print(matrix1)
print("Testing indexes")
print(f"Checking normal case {3}: {binarySearch(matrix1,target1)}")
print(f"Checking edge cases {23}: {binarySearch(matrix1,target2)}")
print(f"Checking edge case {1}: {binarySearch(matrix1,target3)}")
print(f"Checking edge case {60}: {binarySearch(matrix1,target4)}")
print(f"Checking invalid value {4}: {binarySearch(matrix1,target5)}")

print("Custom testcases")
matrix2 = [[],[],[]]
print(matrix2)
print(f"Testing if searching a random number returns error or False: {binarySearch(matrix2,2)}")

# I understand that maybe there needs to be a check if len(row) and len(col) but not sure if that can be done in less than O(n) when the solution needs to be O(log(n))



