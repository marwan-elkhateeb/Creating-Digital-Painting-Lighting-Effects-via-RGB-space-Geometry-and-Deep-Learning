
from typing import Collection
from itertools import count
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import math
from scipy.spatial import ConvexHull, Delaunay
from scipy.sparse import coo_matrix
from os import sep
from PIL import Image, ImageFilter
import matplotlib.pyplot as plt
import cv2

#Extract Pixel 
with open('.txt', 'w') as writefile:
    im = Image.open('A1.png')
    im = im.convert("RGB")
    im = im.resize((512, 512))
    r,g,b = 0,0,0
    for x in range(im.width):
        for y in range(im.height):
            #print(im.getpixel((x,y)))
            
            writefile.write(str(im.getpixel((x,y))))
            writefile.write("\n")
im.save('Image.jpg')
plt.imshow(im)
plt.show()

#Read the file of each pixel in the image
with open("_RemovedDuplicatePixels.txt") as f_in:
    lines = [line.rstrip() for line in f_in] # All lines including the blank ones
    lines = [line for line in lines if line] # Non-blank lines

#split between lines ',' 
arr = [np.array(line.split(',')).astype(np.float) for line in lines]
# save all points in array 
arr = np.array(arr)
print(arr)

#get the convexhull form the array(pixels of image RGB) in file 
convex_hull = ConvexHull(arr)
convex_hull_vertices = [convex_hull.points[i] for i in convex_hull.vertices]

# number of points for convexhull vertices
L = len(convex_hull_vertices)

# print convexhull vertices points === and i was the points from convexhull
with open('_ConvexHullVertices.txt', 'w') as writefile:
    for i in range(L) :
      print (convex_hull_vertices[i][0], convex_hull_vertices[i][1],convex_hull_vertices[i][2], sep = ",")
      writefile.write(str(convex_hull_vertices[i][0])+","+str(convex_hull_vertices[i][1])+","+str(convex_hull_vertices[i][2]))
      writefile.write("\n")

print('################################')
print(L)

#get the simplices(triangles) from convexhull 
#Code with comprestion loop
#//////////////////////////////////////////////#
with open('_Simplices(Triangles).txt', 'w') as writefile:
  simplices = [ list(face) for face in convex_hull.simplices ]
  for i in  range(len(simplices)):
    print(simplices[i])
    writefile.write(str(simplices[i]))
    writefile.write("\n")
    print(i)

#2 - Geting (G) centroid of convexHull

# set a point with a variable to make an area of triangles 
k = 0
a = np.array
b = np.array
c = np.array

        
counter = 1     
areas = []
AreaFinal = 0
TotalMultiTriangleX = 0
TotalMultiTriangleY = 0
TotalMultiTriangleZ = 0
with open('_Triangles.txt', 'w') as writefile:
    for i in simplices:
      a,b,c = i
      a,b,c = arr[a] , arr[b], arr[c]
      x = np.array(a)
      y = np.array(b)
      z = np.array(c)

      xy = np.sqrt(np.sum(np.square(x-y)))
      xz = np.sqrt(np.sum(np.square(x-z)))
      yz = np.sqrt(np.sum(np.square(y-z)))

      SemiParameter = (xy + xz + yz)/2

      #The area of the triangle
      area = np.sqrt(SemiParameter * (SemiParameter - xy) * (SemiParameter - xz) * (SemiParameter - yz))


      areas.append(area)
      areadivide = area/3
      

      print("Triangle " + str(counter))
      
      #Show the points of the triangle
      print("a = " +str(a[0]),str(a[1]),str(a[2]),sep = ",")
      print("b = " +str(b[0]),str(b[1]),str(b[2]),sep = ",")
      print("c = " +str(c[0]),str(c[1]),str(c[2]),sep = ",")
      writefile.write(str(a))
      writefile.write("\n")
      writefile.write(str(b))
      writefile.write("\n")
      writefile.write(str(c))
      writefile.write("\n")

      
      print("area : " + str(area))
      print("area after divide 3 :" + str(areadivide))


      #Sumution for the points of the triangle
      p1 = a[0] + b[0] + c[0]
      p2 = a[1] + b[1] + c[1]
      p3 = a[2] + b[2] + c[2]
      SumofTriangle = (p1,p2,p3)
      print("SumOfTriangle =" + str (SumofTriangle))


      #Multipuly the sumtion of the points with area after divide 3
      SumofTriangle = np.asarray(SumofTriangle)
      multiTriangle = SumofTriangle * areadivide
      
      print("Multiply areadivide * sumofTriangle = " + str((multiTriangle)))
      
      print("==========")


      #collect all triangles to get the convex hull(s)

      TotalMultiTriangleX += multiTriangle[0] 
      convex1 = TotalMultiTriangleX
      TotalMultiTriangleY += multiTriangle[1] 
      convex2 = TotalMultiTriangleY
      TotalMultiTriangleZ += multiTriangle[2] 
      convex3 = TotalMultiTriangleZ
      convexhulll = (convex1,convex2,convex3)

      #Area of convexhull = Sum of area triangle 
      
      AreaFinal += area
      counter +=1


    sum(areas)
    if sum(areas) == AreaFinal:
      print("true") 
      print("areas = "+str(sum(areas)))
    ConvexFinal = convexhulll/AreaFinal
    print("area of convex hull = "+ str(AreaFinal))
    with open('Poster_CentroidOfConvex.txt', 'w') as writefile:
        print("The centroid point of the convex hull = " +str(ConvexFinal))
        writefile.write(str(ConvexFinal))
        writefile.write("\n")



    #print("sumofarea = " + str(1/area) )
    #print(multiTriangle[1])

#4 - The Ray(centroid , Direction)
#The Direction of centroid(convexFinal) and all pixels
with open('.txt', 'w') as writefile:
    for i in arr:
      Direct = i - ConvexFinal
      Directx =  np.sqrt(np.sum(np.square(Direct)))
      Direction = Direct/Directx
      #print(Direction)
      writefile.write(str(Direction[0]*255)+","+str(Direction[1]*255)+","+str(Direction[2]*255))
      writefile.write("\n")

print(len(areas))

#Centroid of all points
totx =0
toty =0
totz =0
for i in arr:
    totx += i[0]
    toty += i[1]
    totz += i[2]
print("x = " + str(totx))
print("y = " + str(toty))
print("z = " + str(totz))
x = totx / len(arr)
y = toty / len(arr)
z = totz / len(arr)

center = x,y,z
print("center of colors" + str(center))

with open("_Hitting.txt") as f_in:
    Hlines = [line.rstrip() for line in f_in] # All lines including the blank ones
    Hlines = [line for line in Hlines if line] # Non-blank lines

#split between lines ',' 
Harr = [np.array(line.split(',')).astype(np.float) for line in Hlines]
# save all points in array 
Harr = np.array(Harr)
print(Harr)

# Get the K using Hitting points 
from scipy.spatial import distance
ct = 1
with open('Mapp_K.txt', 'w') as writefile:
    for i, j in zip( arr , Harr):
        Knumerator = i - j  
        Mag_Knumerator =  np.sqrt(np.sum(np.square(Knumerator)))
        Kdenominator = ConvexFinal - j
        Mag_Kdenominator =  np.sqrt(np.sum(np.square(Kdenominator)))
        Map_K = (Mag_Knumerator) / (Mag_Kdenominator) 
        #print("counter = " + str(ct) + ", Map_K = " + str(Map_K * 255)) 
        writefile.write(str(Map_K * 255))
        writefile.write("\n")
        ct = ct + 1

#Save mapK in array
with open("_KImage.txt") as f_in:
    Maplines = [line.rstrip() for line in f_in] # All lines including the blank ones
    Maplines = [line for line in Maplines if line] # Non-blank lines

#split between lines ',' 
MapK = [np.array(line.split(',')) for line in Maplines]
# save all points in array 
MapK = np.array(MapK)
#MapK = np.around(MapK)
#MapK = MapK.astype(int)
print(MapK)
len(MapK)

from PIL import Image
import numpy as np

pixels = np.array(MapK)

pixels=pixels.reshape(-1,512,1)
print(pixels.shape)

array = np.array(pixels)
#Use PIL to create an image from the new array of pixels

new_image = Image.fromarray(array,mode='L')
new_image.save('_DienstyK.jpg')

#Save image RGB in array
with open("Imagee.txt") as f_in:
    Imlines = [line.rstrip() for line in f_in] # All lines including the blank ones
    Imlines = [line for line in Imlines if line] # Non-blank lines

#split between lines ',' 
Original = [np.array(line.split(',')) for line in Imlines]
# save all points in array 
Original = np.array(Original)
print(Original)
len(Original)

# Opening the image 
# (R prefixed to string in order to deal with '\' in paths)
image = Image.open('1.PNG')
  
# Blurring image by sending the ImageFilter.
# GaussianBlur predefined kernel argument
image = image.filter(ImageFilter.GaussianBlur)
  
#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Displaying the image
image.show()
plt.imshow(image)


#Extract Gaussian image pixels
with open('imageBlur.txt', 'w') as writefile:
    image = image.convert("RGB")
    for x in range(image.width):
        for y in range(image.height):
            #print(im.getpixel((x,y)))
            writefile.write(str(image.getpixel((x,y))))
            writefile.write("\n")
        
plt.imshow(image)
plt.show()

#def gaussianFilter(image, k_size, sigma, progress):
image = Image.open('1.PNG')
#dimensions = img.shape
height ,width = image.size
dst_height = height - 64 + 1
dst_width = width - 64 + 1

image_array = np.zeros((dst_height * dst_width, 64 * 64))
row = 0
for i, j in np.product(range(dst_height), range(dst_width)):
    np.progress.value += int((row+1)/100)
    window = np.ravel(image[i : i + 64, j : j + 64])
    image_array[row, :] = window
    row += 1

gaussian_kernel = np.gen_gaussian_kernel(64, 16)
filter_array = np.ravel(gaussian_kernel)

dst = np.dot(image_array, filter_array).reshape(dst_height, dst_width).astype(uint8)

cv2.imwrite('gaussianFilter.jpg', dst)

import cv2
import cv2
from skimage import io, img_as_float
from skimage.filters import gaussian


img_gaussian_noise = img_as_float(io.imread('1.PNG', as_gray=True))
img_salt_pepper_noise = img_as_float(io.imread('1.PNG', as_gray=True))

img = img_gaussian_noise

gaussian_using_cv2 = cv2.GaussianBlur(img, (3,3), 0, borderType=cv2.BORDER_CONSTANT)

gaussian_using_skimage = gaussian(img, sigma=16, mode='constant', cval=0.0)
#sigma defines the std dev of the gaussian kernel. SLightly different than 
#how we define in cv2


plt.show("Original", img)
#plt.show("Using cv2 gaussian", gaussian_using_cv2)
#plt.show("Using skimage", gaussian_using_skimage)
#cv2.imshow("Using scipy2", conv_using_scipy2)

import matplotlib, cv2
import numpy as np
import matplotlib.pyplot as plt

# read an image
img = cv2.imread('1.PNG')

# show image format (basically a 3-d array of pixel color info, in BGR format)
print(img)

# convert image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# grayscale image represented as a 2-d array
print(gray_img)

# have to convert grayscale back to RGB for plt.imshow()
plt.imshow(cv2.cvtColor(gray_img, cv2.COLOR_GRAY2RGB))

#def gausskernel(size,k,sigma):
gray_img = np.zeros((64,64),np.float32)
for i in range (64):
    for j in range (64):
        norm = math.pow(i-k,2) + pow(j-k,2)
        gray_img[i,j] = math.exp(-norm/(2*math.pow(16,2)))/2*math.pi*pow(16,2)
sum = np.sum(gray_img)
kernel = gray_img/sum

print(kernel)

from google.colab.patches import cv2_imshow
from itertools import product
import cv2
from cv2 import COLOR_BGR2GRAY, cvtColor, imread, imshow, waitKey
from numpy import dot, exp, mgrid, pi, ravel, square, uint8, zeros
import numpy
from PIL import Image, ImageOps

def fspecial_gauss(size, sigma):

    """Function to mimic the 'fspecial' gaussian MATLAB function
    """

    x, y = numpy.mgrid[-size//2 + 1:size//2 + 1, -size//2 + 1:size//2 + 1]
    g = numpy.exp(-((x**2 + y**2)/(2.0*sigma**2)))
    return g/g.sum()


if __name__ == "__main__":
    # read original image
    img = imread("A1.png")

    image2 = img.copy()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    

    kernal = fspecial_gauss(64, 16)
    convv = cv2.filter2D(gray,-1,kernal)

    normalizedgray = convv.copy()

    minn = int(convv.min())
    maxx = int(convv.max())
    
    print(minn,maxx,convv[0][0])
    
    graycDenimorator = (maxx - minn)
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            graycNuminrator = (convv[x][y] - minn)
            Grayc = ((graycNuminrator) / (graycDenimorator))
            normalizedgray[x][y] = Grayc


    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            r,g,b = img[x][y]
            cn = int(convv[x][y])
            gy = int(gray[x][y])
            if gy != 0: 
                newr = int((r * cn) / gy)
                newg = int((g * cn) / gy)
                newb = int((b * cn) / gy)
              
            else:
                newr = int((r * cn))
                newg = int((g * cn))
                newb = int((b * cn))
            image2[x][y] = (numpy.max([numpy.min([newb,255]),0]) ,  numpy.max([numpy.min([newg,255]),0]) , numpy.max([numpy.min([newr,255]),0]))

    print(r,g,b , cn, gy, image2[381][409], newr , newg , newb )

    plt.imshow(image2)
    imgtosave = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
    cv2.imwrite('Nc.png',imgtosave)
    cv2_imshow(normalizedgray)

def plot_img(img, disp_size=(7, 7)):
    from matplotlib import pyplot
    pyplot.figure(figsize = disp_size, dpi=80)
    display(pyplot.imshow(img,cmap="gray"))

img = cv2.imread("1.PNG")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

orig_image = img.copy()

original_size = img.shape

im = img.copy()

def padding(im, kernel_size, padding_type = 'full'):
    try:
        padding_type = str(padding_type).lower()
    except:
        padding_type = 'full'
    
    img_w, img_h = im.shape[0], im.shape[1]
    krnl_w, krnl_h = kernel_size, kernel_size
    
    if(padding_type == 'full'):
        pad = np.zeros( (img_w + krnl_w - 1, img_h + krnl_h - 1))

        pad[krnl_w//2: img_w + krnl_w//2, krnl_h//2: img_h + krnl_h//2] = im.copy()
    if(padding_type == 'same'):
        pad = np.zeros( (img_w + krnl_w//2 , img_h + krnl_h//2 ))

        pad[krnl_w//2: img_w + krnl_w//2, krnl_h//2: img_h + krnl_h//2] = im.copy()
    if(padding_type == 'valid'):
        pad = im.copy()
    return pad

def apply_2D_filter(im, Filter, img_name = 'new_image', padding_type = 'full'):
    try:
        img_name = str(img_name)
    except:
        img_name = 'new_image'
    
    kernel = Filter.copy()
    img_w, img_h = im.shape[0], im.shape[1]
    krnl_w, krnl_h = kernel.shape[0], kernel.shape[1]

    pad = padding(im,krnl_h,padding_type)
    new_image = np.zeros((img_w, img_h))

    for r in range(0, pad.shape[0] - krnl_w + 1):
        for c in range(0, pad.shape[1] - krnl_h +1):
            matrix = pad[r: r + krnl_w, c: c + krnl_h]
            new_image[ r , c ] = np.sum(np.multiply(matrix, kernel))
    
    cv2.imwrite(img_name+'.png', new_image)
    new_image = cv2.imread(img_name+'.png')
    new_image = cv2.cvtColor(new_image, cv2.COLOR_BGR2GRAY)
    return new_image

def dnorm(x, mu, sd):
    return 1 / (np.sqrt(2 * np.pi) * sd) * np.e ** (-np.power((x - mu) / sd, 2) / 2)

def gaussian_kernel(size, sigma=16):
    kernel_1D = np.linspace(-(size // 2), size // 2, size)
    for i in range(size):
        kernel_1D[i] = dnorm(kernel_1D[i], 0, sigma)
    kernel_2D = np.outer(kernel_1D.T, kernel_1D.T)

    kernel_2D *= 1.0 / kernel_2D.max()

    
    
    return kernel_2D/(kernel_2D.shape[0]*kernel_2D.shape[1])

def gaussian_blur(image, kernel_size = 64):
    kernel = gaussian_kernel(kernel_size, sigma=16)
    return apply_2D_filter(image, kernel)


plot_img(gaussian_blur(img, 64))

from google.colab.patches import cv2_imshow
from itertools import product
from cv2 import COLOR_BGR2GRAY, cvtColor, imread, imshow, waitKey
from numpy import dot, exp, mgrid, pi, ravel, square, uint8, zeros
import numpy
import cv2
from PIL import Image, ImageOps

def fspecial_gauss(size, sigma):

    """Function to mimic the 'fspecial' gaussian MATLAB function
    """

    x, y = numpy.mgrid[-size//2 + 1:size//2 + 1, -size//2 + 1:size//2 + 1]
    g = numpy.exp(-((x**2 + y**2)/(2.0*sigma**2)))
    return g/g.sum()


if __name__ == "__main__":
    # read original image
    img = imread("A1.png")


    Channal0 = img[ : , : ,0]
    Channal1 = img[ : , : ,1]
    Channal2 = img[ : , : ,2] 
    #print(Channal2,img)
    image2 = img.copy()

    
    kernal = fspecial_gauss(64, 16)

    convv0 = cv2.filter2D(Channal0,-1,kernal)
    convv1 = cv2.filter2D(Channal1,-1,kernal)
    convv2 = cv2.filter2D(Channal2,-1,kernal)

    normalizedgray0 = convv0.copy()
    normalizedgray1 = convv1.copy()
    normalizedgray2 = convv2.copy()

    minn0 = int(convv0.min())
    maxx0 = int(convv0.max())

    minn1 = int(convv1.min())
    maxx1 = int(convv1.max())

    minn2 = int(convv2.min())
    maxx2 = int(convv2.max())
    
    #print(minn,maxx,convv[0][0])
    
    graycDenimorator0 = (maxx0 - minn0)
    graycDenimorator1 = (maxx1 - minn1)
    graycDenimorator2 = (maxx2 - minn2)

    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            graycNuminrator0 = (convv0[x][y] - minn0)
            Grayc0 = ((graycNuminrator0) / (graycDenimorator0))
            normalizedgray0[x][y] = Grayc0

            graycNuminrator1 = (convv1[x][y] - minn1)
            Grayc1 = ((graycNuminrator1) / (graycDenimorator1))
            normalizedgray1[x][y] = Grayc1

            graycNuminrator2 = (convv2[x][y] - minn2)
            Grayc2 = ((graycNuminrator2) / (graycDenimorator2))
            normalizedgray2[x][y] = Grayc2

    result = numpy.stack([normalizedgray0, normalizedgray1,normalizedgray2], axis = 2)

    plt.imshow(result)
    imgtosave = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
    #cv2.imwrite('Nc.png',imgtosave)
    #cv2_imshow(normalizedgray)

