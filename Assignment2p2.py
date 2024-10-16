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
    # what would mid be so that i can traverse both vertically and laterally in a matrix array
    # can i assume that every column array is the same size?
    row = len(matrix)
    # only works if n array size is fixed if not then it has to be O(n) to iterate through the different sizes
    col = len(matrix[0])
    # i need to know the total number of elements in the matrix from 0 to len(matrix2D)
    len1d = row * col - 1
    # now I can start the binary search to achieve log(m*n) time
    left,right = 0,len1d
    while left <= right:
        mid = (left + right) // 2
        # i need a sway to split the arrays into row/col
        # first iteration would be the max len of 2d matrix by the number of columns to get rows
        currRow = mid // col
        # columns is just the max length of the 2d matrix mod the size of the column
        currCol = mid % col
        # first if the target is in the upper bracket
        if target > matrix[currRow][currCol]:
            left = mid + 1
        # if the target is in the lower bracket
        elif target < matrix[currRow][currCol]:
            right = mid - 1
        # finally if the target is at the perfect place
        else:
            return True
    
    return False

# test cases given in the assigneemnt
matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target1 = 3 # works all good
target2 = 23 # checking edges of arrays front/back
target3 = 1
target4 = 60 # checking if edge case doesn't go out of bounds
target5 = 4 #checking if invalid values return -1
print(binarySearch(matrix1,target1))
print(binarySearch(matrix1,target2))
print(binarySearch(matrix1,target3))
print(binarySearch(matrix1,target4))
print(binarySearch(matrix1,target5))
# all test cases returned the correct answer pog


