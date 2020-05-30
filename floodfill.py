'''
Flood fill
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.
'''

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newcolor = 2

def floodFill(image,sr,sc,newcolor):
    startcolor = image[sr][sc]
    floodFillHelper(image,sr,sc,startcolor,newcolor)
    return image

def floodFillHelper(image,sr,sc,startcolor,newcolor):
    if image[sr][sc] != newcolor:
        image[sr][sc] = newcolor
        bottom = bool((sr+1)<len(image))
        top = bool((sr-1)>=0)
        right = bool(((sc+1)<len(image[0])))
        left = bool((sc-1)>=0)
        if bottom:
            if image[sr+1][sc] == startcolor:
                floodFillHelper(image,sr+1,sc,startcolor,newcolor)
        if top:
            if image[sr-1][sc] == startcolor:
                floodFillHelper(image,sr-1,sc,startcolor,newcolor)
        if right:
            if image[sr][sc+1] == startcolor:
                floodFillHelper(image,sr,sc+1,startcolor,newcolor)
        if left:
            if image[sr][sc-1] == startcolor:
                floodFillHelper(image,sr,sc-1,startcolor,newcolor)

print(floodFill(image,sr,sc,newcolor))
