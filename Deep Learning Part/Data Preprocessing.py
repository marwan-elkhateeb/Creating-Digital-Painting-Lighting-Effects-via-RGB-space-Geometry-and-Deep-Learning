


from email import header
from PIL import Image
import os
import PIL
import glob
import pandas as pd



def fun1 ():

    listt = []
    i = 17833
    count = 0
    countfile = 1
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    q=0
    ct = 0


    with open ('Input.csv', 'w+') as csvfile:
        fieldnames = ['Width','Height','R','G','B'
                      ,'Neighbour1R','Neighbour1G','Neighbour1B','Neighbour2R','Neighbour2G','Neighbour2B','Neighbour3R','Neighbour3G','Neighbour3B','Neighbour4R','Neighbour4G','Neighbour4B','Neighbour5R','Neighbour5G','Neighbour5B'
                      ,'Neighbour6R','Neighbour6G','Neighbour6B','Neighbour7R','Neighbour7G','Neighbour7B','Neighbour8R','Neighbour8G','Neighbour8B','Neighbour9R','Neighbour9G','Neighbour9B','Neighbour10R','Neighbour10G','Neighbour10B'
                      ,'Neighbour11R','Neighbour11G','Neighbour11B','Neighbour12R','Neighbour12G','Neighbour12B','Neighbour13R','Neighbour13G','Neighbour13B','Neighbour14R','Neighbour14G','Neighbour14B','Neighbour15R','Neighbour15G','Neighbour15B'
                      ,'Neighbour16R','Neighbour16G','Neighbour16B','Neighbour17R','Neighbour17G','Neighbour17B','Neighbour18R','Neighbour18G','Neighbour18B','Neighbour19R','Neighbour19G','Neighbour19B','Neighbour20R','Neighbour20G','Neighbour20B'
                      ,'Neighbour21R','Neighbour21G','Neighbour21B','Neighbour22R','Neighbour22G','Neighbour22B','Neighbour23R','Neighbour23G','Neighbour23B','Neighbour24R','Neighbour24G','Neighbour24B','FR','FG','FB','Direction']
        headers = ",".join(fieldnames)
        csvfile.write(f"{headers}\n")
        for root,dirs,files in os.walk(f''):
            ct += 1
            print("here = " + str(ct) )
            for file in files :
                if( not file.split('.')[-1] == 'png' or not file[:3] == 'img'):
                    continue
                with PIL.Image.open(os.path.join(root,file), "r") as auto:
                    if  file in 'imgHQ'+str(i) +'_00.png':
                        image = auto.resize((64,64))
                        image = image.convert("RGB")
                        #print(file)
                        for q in range(0,4):
                            for x in range(image.width):
                                for y in range(image.height):
                                    #print(x,y)
                                    #print(list(image.getdata()))
                                    #print(image.getpixel((x,y)))
                                    #Average
                                    FR = (image.getpixel((x,y))[0]) / 2000
                                    FG = (image.getpixel((x,y))[1]) / 2000
                                    FB = (image.getpixel((x,y))[2]) / 2000
                                    #Direction
                                    if q == 0:
                                        Direction = 1
                                    if q == 1:
                                        Direction = 2
                                    if q == 2:
                                        Direction = 3
                                    if q == 3:
                                        Direction = 4
                                    #Neighbour 1
                                    if x - 2 < 0 or y + 2 < 0 and x - 2 > 64 or y + 2 > 64:
                                        Neighbour1R = -1
                                        Neighbour1G = -1
                                        Neighbour1B = -1
                                    elif x - 2 >= 0 and y + 2 >= 0 and x - 2 <= 63 and y + 2 <= 63:
                                        Neighbour1R = image.getpixel((x-2,y+2))[0]
                                        Neighbour1G = image.getpixel((x-2,y+2))[1]
                                        Neighbour1B = image.getpixel((x-2,y+2))[2]
                                    ##################################################################
                                    #Neighbour 2
                                    if x - 1 < 0 or y + 2 < 0 and x - 1 > 64 or y + 2 > 64:
                                        Neighbour2R = -1
                                        Neighbour2G = -1
                                        Neighbour2B = -1
                                    elif x - 1 >= 0 and y + 2 >= 0 and x - 1 <= 63 and y + 2 <= 63:
                                        Neighbour2R = image.getpixel((x-1,y+2))[0]
                                        Neighbour2G = image.getpixel((x-1,y+2))[1]
                                        Neighbour2B = image.getpixel((x-1,y+2))[2]
                                    ##########################################################
                                    #Neighbour 3
                                    if x < 0 or y + 2 < 0 and x > 64 or y + 2 > 64:
                                        Neighbour3R = -1
                                        Neighbour3G = -1
                                        Neighbour3B = -1
                                    elif x >= 0 and y + 2 >= 0 and x <= 63 and y + 2 <= 63:
                                        Neighbour3R = image.getpixel((x,y+2))[0]
                                        Neighbour3G = image.getpixel((x,y+2))[1]
                                        Neighbour3B = image.getpixel((x,y+2))[2]
                                    ###########################################################
                                    #Neighbour 4
                                    if x + 1 < 0 or y + 2 < 0 and x + 1 > 64 or y + 2 > 64:
                                        Neighbour4R = -1
                                        Neighbour4G = -1
                                        Neighbour4B = -1
                                    elif x + 1 >= 0 and y + 2 >= 0 and x + 1 <= 63 and y + 2 <= 63: 
                                        Neighbour4R = image.getpixel((x+1,y+2))[0]
                                        Neighbour4G = image.getpixel((x+1,y+2))[1]
                                        Neighbour4B = image.getpixel((x+1,y+2))[2]
                                    ###########################################################
                                    #Neighbour 5
                                    if x + 2 < 0  or y + 2 < 0 and x + 2 > 64 or y + 2 > 64:
                                        Neighbour5R = -1
                                        Neighbour5G = -1
                                        Neighbour5B = -1
                                    elif x + 2 >= 0 and y + 2 >= 0 and x + 2 <= 63 and y + 2 <= 63: 
                                        Neighbour5R = image.getpixel((x+2,y+2))[0]
                                        Neighbour5G = image.getpixel((x+2,y+2))[1]
                                        Neighbour5B = image.getpixel((x+2,y+2))[2]
                                    ###########################################################
                                    #Neighbour 6
                                    if x - 2 < 0 or y + 1 < 0 and x - 2 > 64 or y + 1 > 64:
                                        Neighbour6R = -1
                                        Neighbour6G = -1
                                        Neighbour6B = -1
                                    elif x - 2 >= 0 and y + 1>=0  and x - 2 <= 63 and y + 1 <= 63:
                                        Neighbour6R = image.getpixel((x-2,y+1))[0]
                                        Neighbour6G = image.getpixel((x-2,y+1))[1]
                                        Neighbour6B = image.getpixel((x-2,y+1))[2] 
                                         
                                    ###########################################################
                                    #Neighbour 7
                                    if x - 1 < 0 or y + 1 < 0 and x - 1 > 64 or y + 1 > 64:
                                        Neighbour7R = -1
                                        Neighbour7G = -1
                                        Neighbour7B = -1
                                    elif x - 1 >= 0 and y + 1 >=0  and x - 1 <= 63 and y + 1 <= 63:
                                        Neighbour7R = image.getpixel((x-1,y+1))[0]
                                        Neighbour7G = image.getpixel((x-1,y+1))[1]
                                        Neighbour7B = image.getpixel((x-1,y+1))[2] 
                                    #############################################################
                                    #Neighbour 8
                                    if x < 0 or y + 1 < 0 and x  > 64 or y + 1 > 64:
                                        Neighbour8R = -1
                                        Neighbour8G = -1
                                        Neighbour8B = -1
                                    elif x >= 0 and y + 1 >=0  and x <= 63 and y + 1 <= 63:
                                        Neighbour8R = image.getpixel((x,y+1))[0]
                                        Neighbour8G = image.getpixel((x,y+1))[1]
                                        Neighbour8B = image.getpixel((x,y+1))[2]
                                    #############################################################
                                    #Neighbour 9
                                    if x + 1 < 0 or y + 1 < 0 and x + 1 > 64 or y + 1 > 64:
                                        Neighbour9R = -1
                                        Neighbour9G = -1
                                        Neighbour9B = -1
                                    elif x + 1 >= 0 and y + 1 >=0  and x + 1 <= 63 and y + 1 <= 63:
                                        Neighbour9R = image.getpixel((x+1,y+1))[0]
                                        Neighbour9G = image.getpixel((x+1,y+1))[1]
                                        Neighbour9B = image.getpixel((x+1,y+1))[2]
                                    #############################################################
                                    #Neighbour 10
                                    if x + 2 < 0 or y + 1 < 0 and x + 2 > 64 or y + 1 > 64:
                                        Neighbour10R = -1
                                        Neighbour10G = -1
                                        Neighbour10B = -1
                                    elif x + 2 >= 0 and y + 1 >=0  and x + 2 <= 63 and y + 1 <= 63:
                                        Neighbour10R = image.getpixel((x+2,y+1))[0]
                                        Neighbour10G = image.getpixel((x+2,y+1))[1]
                                        Neighbour10B = image.getpixel((x+2,y+1))[2]
                                    #############################################################
                                    #Neighbour 11
                                    if x - 2 < 0 or y < 0 and x - 2 > 64 or y > 64:
                                        Neighbour11R = -1
                                        Neighbour11G = -1
                                        Neighbour11B = -1
                                    elif x - 2 >= 0 and y >=0  and x - 2 <= 63 and y <= 63:
                                        Neighbour11R = image.getpixel((x-2,y))[0]
                                        Neighbour11G = image.getpixel((x-2,y))[1]
                                        Neighbour11B = image.getpixel((x-2,y))[2]
                                    ###############################################################
                                    #Neighbour 12
                                    if x - 1 < 0 or y < 0 and x - 1 > 64 or y > 64:
                                        Neighbour12R = -1
                                        Neighbour12G = -1
                                        Neighbour12B = -1
                                    elif x - 1 >= 0 and y >=0  and x - 1 <= 63 and y <= 63:
                                        Neighbour12R = image.getpixel((x-1,y))[0]
                                        Neighbour12G = image.getpixel((x-1,y))[1]
                                        Neighbour12B = image.getpixel((x-1,y))[2]
                                    ##################################################################
                                    #Neighbour 13
                                    if x + 1 < 0 or y < 0 and x + 1 > 64 or y > 64:
                                        Neighbour13R = -1
                                        Neighbour13G = -1
                                        Neighbour13B = -1
                                    elif x + 1 >= 0 and y >=0  and x + 1 <= 63 and y <= 63:
                                        Neighbour13R = image.getpixel((x+1,y))[0]
                                        Neighbour13G = image.getpixel((x+1,y))[1]
                                        Neighbour13B = image.getpixel((x+1,y))[2]
                                    #################################################################
                                    #Neighbour 14
                                    if x + 2 < 0 or y < 0 and x + 2 > 64 or y > 64:
                                        Neighbour14R = -1
                                        Neighbour14G = -1
                                        Neighbour14B = -1
                                    elif x + 2 >= 0 and y >=0  and x + 2 <= 63 and y <= 63:
                                        Neighbour14R = image.getpixel((x+2,y))[0]
                                        Neighbour14G = image.getpixel((x+2,y))[1]
                                        Neighbour14B = image.getpixel((x+2,y))[2]
                                    #################################################################
                                     #Neighbour 15
                                    if x - 2 < 0 or y - 1 < 0 and x - 2 > 64 or y - 1 > 64: 
                                        Neighbour15R = -1
                                        Neighbour15G = -1
                                        Neighbour15B = -1
                                    elif x - 2 >= 0 and y - 1 >=0  and x - 2 <= 63 and y - 1 <= 63:
                                        Neighbour15R = image.getpixel((x-2,y-1))[0]
                                        Neighbour15G = image.getpixel((x-2,y-1))[1]
                                        Neighbour15B = image.getpixel((x-2,y-1))[2]
                                    #################################################################
                                     #Neighbour 16
                                    if x - 1 < 0 or y - 1 < 0 and x - 1 > 64 or y - 1 > 64:
                                        Neighbour16R = -1
                                        Neighbour16G = -1
                                        Neighbour16B = -1
                                    elif x - 1 >= 0 and y - 1 >=0  and x - 1 <= 63 and y - 1 <= 63:
                                        Neighbour16R = image.getpixel((x-1,y-1))[0]
                                        Neighbour16G = image.getpixel((x-1,y-1))[1]
                                        Neighbour16B = image.getpixel((x-1,y-1))[2]
                                    #################################################################
                                     #Neighbour 17
                                    if x < 0 or y - 1 < 0 and x > 64 or y - 1 > 64:
                                        Neighbour17R = -1
                                        Neighbour17G = -1
                                        Neighbour17B = -1
                                    elif x >= 0 and y - 1 >=0  and x <= 63 and y - 1 <= 63:
                                        Neighbour17R = image.getpixel((x,y-1))[0]
                                        Neighbour17G = image.getpixel((x,y-1))[1]
                                        Neighbour17B = image.getpixel((x,y-1))[2]
                                    #################################################################
                                     #Neighbour 18
                                    if x + 1 < 0 or y - 1 < 0 and x + 1 > 64 or y - 1 > 64:
                                        Neighbour18R = -1
                                        Neighbour18G = -1
                                        Neighbour18B = -1
                                    elif x + 1 >= 0 and y - 1 >=0  and x + 1 <= 63 and y - 1 <= 63:
                                        Neighbour18R = image.getpixel((x+1,y-1))[0]
                                        Neighbour18G = image.getpixel((x+1,y-1))[1]
                                        Neighbour18B = image.getpixel((x+1,y-1))[2]
                                    #################################################################
                                     #Neighbour 19
                                    if x + 2 < 0 or y - 1 < 0 and x + 2 > 64 or y - 1 > 64:
                                        Neighbour19R = -1
                                        Neighbour19G = -1
                                        Neighbour19B = -1
                                    elif x + 2 >= 0 and y - 1 >=0  and x + 2 <= 63 and y - 1 <= 63:
                                        Neighbour19R = image.getpixel((x+2,y-1))[0]
                                        Neighbour19G = image.getpixel((x+2,y-1))[1]
                                        Neighbour19B = image.getpixel((x+2,y-1))[2]
                                    #################################################################
                                     #Neighbour 20
                                    if x - 2 < 0 or y - 2 < 0 and x - 2 > 64 or y - 2 > 64:
                                        Neighbour20R = -1
                                        Neighbour20G = -1
                                        Neighbour20B = -1
                                    elif x - 2 >= 0 and y - 2 >=0  and x - 2 <= 63 and y - 2 <= 63:
                                        Neighbour20R = image.getpixel((x-2,y-2))[0]
                                        Neighbour20G = image.getpixel((x-2,y-2))[1]
                                        Neighbour20B = image.getpixel((x-2,y-2))[2]
                                    #################################################################
                                     #Neighbour 21
                                    if x - 1 < 0 or y - 2 < 0 and x - 1 > 64 or y - 2 > 64:
                                        Neighbour21R = -1
                                        Neighbour21G = -1
                                        Neighbour21B = -1
                                    elif x - 1 >= 0 and y - 2 >=0  and x - 1 <= 63 and y - 2 <= 63:
                                        Neighbour21R = image.getpixel((x-1,y-2))[0]
                                        Neighbour21G = image.getpixel((x-1,y-2))[1]
                                        Neighbour21B = image.getpixel((x-1,y-2))[2]
                                    #################################################################
                                     #Neighbour 22
                                    if x < 0 or y - 2 < 0 and x > 64 or y - 2 > 64:
                                        Neighbour22R = -1
                                        Neighbour22G = -1
                                        Neighbour22B = -1
                                    elif x >= 0 and y - 2 >=0  and x <= 63 and y - 2 <= 63:
                                        Neighbour22R = image.getpixel((x,y-2))[0]
                                        Neighbour22G = image.getpixel((x,y-2))[1]
                                        Neighbour22B = image.getpixel((x,y-2))[2]
                                    #################################################################
                                     #Neighbour 23
                                    if x + 1 < 0 or y - 2 < 0 and x + 1 > 64 or y - 2 > 64:
                                        Neighbour23R = -1
                                        Neighbour23G = -1
                                        Neighbour23B = -1
                                    elif x + 1 >= 0 and y - 2 >=0  and x + 1 <= 63 and y - 2 <= 63:
                                        Neighbour23R = image.getpixel((x+1,y-2))[0]
                                        Neighbour23G = image.getpixel((x+1,y-2))[1]
                                        Neighbour23B = image.getpixel((x+1,y-2))[2]
                                    #################################################################
                                     #Neighbour 24
                                    if x + 2 < 0 or y - 2 < 0 and x + 2 > 64 or y - 2 > 64:
                                        Neighbour24R = -1
                                        Neighbour24G = -1
                                        Neighbour24B = -1
                                    elif x + 2 >= 0 and y - 2 >=0  and x + 2 <= 63 and y - 2 <= 63:
                                        Neighbour24R = image.getpixel((x+2,y-2))[0]
                                        Neighbour24G = image.getpixel((x+2,y-2))[1]
                                        Neighbour24B = image.getpixel((x+2,y-2))[2]
                                    #################################################################
                                    a += 1
                                    csvfile.write(f"{x},{y},{image.getpixel((x,y))[0]},{image.getpixel((x,y))[1]},{image.getpixel((x,y))[2]},{Neighbour1R},{Neighbour1G},{Neighbour1B},{Neighbour2R},{Neighbour2G},{Neighbour2B},{Neighbour3R},{Neighbour3G},{Neighbour3B},{Neighbour4R},{Neighbour4G},{Neighbour4B},{Neighbour5R},{Neighbour5G},{Neighbour5B},{Neighbour6R},{Neighbour6G},{Neighbour6B},{Neighbour7R},{Neighbour7G},{Neighbour7B},{Neighbour8R},{Neighbour8G},{Neighbour8B},{Neighbour9R},{Neighbour9G},{Neighbour9B},{Neighbour10R},{Neighbour10G},{Neighbour10B},{Neighbour11R},{Neighbour11G},{Neighbour11B},{Neighbour12R},{Neighbour12G},{Neighbour12B},{Neighbour13R},{Neighbour13G},{Neighbour13B},{Neighbour14R},{Neighbour14G},{Neighbour14B},{Neighbour15R},{Neighbour15G},{Neighbour15B},{Neighbour16R},{Neighbour16G},{Neighbour16B},{Neighbour17R},{Neighbour17G},{Neighbour17B},{Neighbour18R},{Neighbour18G},{Neighbour18B},{Neighbour19R},{Neighbour19G},{Neighbour19B},{Neighbour20R},{Neighbour20G},{Neighbour20B},{Neighbour21R},{Neighbour21G},{Neighbour21B},{Neighbour22R},{Neighbour22G},{Neighbour22B},{Neighbour23R},{Neighbour23G},{Neighbour23B},{Neighbour24R},{Neighbour24G},{Neighbour24B},{FR},{FG},{FB},{Direction}\n")
                        i+=1
                        print("count = " + str(ct))
                        print("First image = " + str(a))
                        print("Second image = " + str(b))
                        print("Third image = " + str(c))
                        print("forth image = " + str(d))
                        print("fifth image = " + str(e))
                        print("floder count = " + str(i))





def fun2():
    listt = []
    i = 17833
    count = 0
    countfile = 1
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    q=0
    with open ('Out.csv', 'w+') as csvfile:
        fieldnames = ['OUTR','OUTG','OUTB']
        headers = ",".join(fieldnames)
        csvfile.write(f"{headers}\n")
        for root,dirs,files in os.walk(f''):
            for file in files :
                if( not file.split('.')[-1] == 'png' or not file[:3] == 'img'):
                    continue
                with PIL.Image.open(os.path.join(root,file), "r") as auto:
                    if file in 'imgHQ'+str(i) +'_01.png':
                        image = auto.resize((64,64))
                        image = image.convert("RGB")
                        for x in range(image.width):
                            for y in range(image.height):
                                b += 1
                                csvfile.write(f"{image.getpixel((x,y))[0]},{image.getpixel((x,y))[1]},{image.getpixel((x,y))[2]}\n")
                    if file in 'imgHQ'+str(i) +'_02.png':
                        image = auto.resize((64,64))
                        image = image.convert("RGB")
                        for x in range(image.width):
                            for y in range(image.height):
                                c += 1
                                csvfile.write(f"{image.getpixel((x,y))[0]},{image.getpixel((x,y))[1]},{image.getpixel((x,y))[2]}\n")
                    if file in 'imgHQ'+str(i) +'_03.png':
                        image = auto.resize((64,64))
                        image = image.convert("RGB")
                        for x in range(image.width):
                            for y in range(image.height):
                                d += 1
                                csvfile.write(f"{image.getpixel((x,y))[0]},{image.getpixel((x,y))[1]},{image.getpixel((x,y))[2]}\n")
                    if file in 'imgHQ'+str(i) +'_04.png':
                        image = auto.resize((64,64))
                        image = image.convert("RGB")
                        for x in range(image.width):
                            for y in range(image.height):
                                e += 1
                                csvfile.write(f"{image.getpixel((x,y))[0]},{image.getpixel((x,y))[1]},{image.getpixel((x,y))[2]}\n")
                        i+=1
            print("First image = " + str(a))
            print("Second image = " + str(b))
            print("Third image = " + str(c))
            print("forth image = " + str(d))
            print("fifth image = " + str(e))
            print("floder count = " + str(i))





def main():
    fun1()
    fun2()





if __name__ == "__main__":
    main()






def fun3():

    df1 = pd.read_csv("data.csv",sep=',')
    df2 = pd.read_csv('data2.csv',sep=',')

    print(df1)
    print(df2)

    headers  = ["Width","Height","R","G","B","Direction"
                      ,"Neighbour1R","Neighbour1G","Neighbour1B"
                      ,"Neighbour2R","Neighbour2G","Neighbour2B"
                      ,"Neighbour3R","Neighbour3G","Neighbour3B"
                      ,"Neighbour4R","Neighbour4G","Neighbour4B"
                      ,"Neighbour5R","Neighbour5G","Neighbour5B"
                      ,"Neighbour6R","Neighbour6G","Neighbour6B"
                      ,"Neighbour7R","Neighbour7G","Neighbour7B"
                      ,"Neighbour8R","Neighbour8G","Neighbour8B"
                      ,"Neighbour9R","Neighbour9G","Neighbour9B"
                      ,"Neighbour10R","Neighbour10G","Neighbour10B"
                      ,"Neighbour11R","Neighbour11G","Neighbour11B"
                      ,"Neighbour12R","Neighbour13G","Neighbour12B"
                      ,"Neighbour13R","Neighbour12G","Neighbour13B"
                      ,"Neighbour14R","Neighbour14G","Neighbour14B"
                      ,"OUTR","OUTG","OUTB"]

    df1 = df1.reset_index()
    print(df1)
    df2 = df2.reset_index(drop=True)
    df3 = pd.concat([df1,df2], axis=1)
    df3 = df3.reindex(columns=headers)
    df3.to_csv("result_cleaned.csv",sep=',',index=False)
    print(df3)
    exit()

    df3.to_csv("result_cleaned.csv",sep='\t',index=False)

def test():
    fun3()




