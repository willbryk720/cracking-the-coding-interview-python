'''
Write function to rotate an NxN matrix by 90 degrees. 
'''

from PIL import Image

# matrix is an array of row arrays
def rotate_matrix_in_place(mat):
    N = len(mat)
    rotate_side_length = N
    for i in range(N/2):
        row_length = N - 2 * i - 1
        for depth in range(row_length):
            x = i + row_length - depth
            temp = mat[i][i + depth]
            mat[i][i + depth] = mat[x][i]
            mat[x][i] = mat[i + row_length ][x]
            mat[i + row_length][x] = mat[i + depth][i + row_length]
            mat[i + depth][i + row_length] = temp    
    return mat
    

# prove that the function works by rotate an image
def rotate_image(image_path):
    im = Image.open(image_path)
    pixels = im.load()
    width, height = im.size

    # convert image to matrix
    mat = [[pixels[col, row] for col in range(width)] for row in range(height)]
    new_mat = rotate_matrix_in_place(mat)

    # modify image using new rotated matrix
    for row in range(height):
        for col in range(width):
            pixels[col, row] = new_mat[row][col]
    
    return im



assert rotate_matrix_in_place([[1,2], [3,4]]) == [[3, 1], [4, 2]]

image_path = 'image1.png'
original_image = Image.open(image_path)
new_image = rotate_image(image_path)
original_image.show()
new_image.show()



        