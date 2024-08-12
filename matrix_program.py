from pytest import mark

@pytest.mark.matrix

def remove_duplicate_element(matrix1): 
    " Removing duplicates in Matrix"
    track = []
    new_matrix = []
    count = 0 
    for row in matrix1:
        new_matrix.append([])
        for ele in row:
            if ele not in track:
                m = new_matrix[count].append(ele)
                print(m)
                track.append(ele)
        count = count+1
    return new_matrix           

#matrix1 = [[5, 6, 8], [8, 5, 3], [9, 10, 3]]
#print(remove_duplicate_element(matrix1))

#matrix2=[[1,3],[2,6],[8,10],[15,18]]



def flipAndInvertImage(matrix):
    """User
Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.

For example, flipping [1,1,0] horizontally results in [0,1,1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.

For example, inverting [0,1,1] results in [1,0,0].
"""

    flipped_image = [rows[::-1] for rows in matrix]
    print(flipped_image)
    inverted_image=[[1-i for i in row] for row in flipped_image]
    return (inverted_image)
matrix = [[1,1,0],[1,0,1],[0,0,0]]
print(flipAndInvertImage(matrix))
