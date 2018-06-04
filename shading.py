import arcpy
from arcpy import env
import numpy as np
import sys
inras="D:/case_Apr/maps/height_layer" #building layer with terrain
a=arcpy.RasterToNumPyArray(inras)
zz=np.loadtxt("D:\case_Apr\maps\z_grid.txt",skiprows=1)
data=np.loadtxt("D:\case_Apr\maps\sun_Feb.txt",skiprows=1)
patch=np.loadtxt("D:\case_Apr\maps\patch1.txt",skiprows=1)
fo = open('D:/case_Apr/maps/MN02/sun9.txt','wt') #output file here
sys.stdout=fo
print "{:>2}{:>5}{:>10}{:>2}{:>2}".format("#H","BID","PID","S","B")
row_d=12
while row_d<=12:
    alpha=data[row_d,1]
    row_p=0
    while row_p<=1475429: #depends on the number of patches
        x=int(patch[row_p,2]-1)
        y=int(patch[row_p,3]-1)
        z1=int(patch[row_p,4])
        z=int(zz[z1])
        nx=patch[row_p,6]
        ny=patch[row_p,7]
        nz=patch[row_p,8]
        if alpha>0 and alpha<90:
            if nx==-1 or ny==1 or nz==1:
                x2=x-1
                while x2>=0:
                    y2=int(y+(x-x2)/(np.tan(np.deg2rad(90-alpha))))
                    if x2>=0 and x2<=1199 and y2<=799 and y2>=0:       #depends on the limit of domain
                        h2=a[x2,y2]
                    if x2<0 or x2>1199 or y2<0 or y2>799:
                        h2=0
                    eletangle1=np.degrees(np.arctan((h2-z)/np.sqrt(((x2-x)*10)**2+((y2-y)*10)**2)))
                    if eletangle1>=data[row_d,2]:
                        break
                    x2-=1
                if x2==-1:
                    print "{:>2}{:>5}{:>10}{:>2}{:>2}".format(int(data[row_d,0]),101,int(patch[row_p,1]),1,1)
                else:
                    print "{:>2}{:>5}{:>10}{:>2}{:>2}".format(int(data[row_d,0]),101,int(patch[row_p,1]),0,0)
            if nx==1 or ny==-1:
                print "{:>2}{:>5}{:>10}{:>2}{:>2}".format(int(data[row_d,0]),101,int(patch[row_p,1]),0,0)
        if alpha>270 and alpha<360:
            if nx==-1 or ny==-1 or nz==1:
                x2=x-1
                while x2>=0:
                    y2=int(y-(x-x2)*(np.tan(np.deg2rad(360-alpha))))
                    if x2>=0 and x2<=1199 and y2<=799 and y2>=0:
                        h2=a[x2,y2]
                    if x2<0 or x2>1199 or y2<0 or y2>799:
                        h2=0
                    eletangle1=np.degrees(np.arctan((h2-z)/np.sqrt(((x2-x)*10)**2+((y2-y)*10)**2)))
                    if eletangle1>=data[row_d,2]:
                        break
                    x2-=1
                if x2==-1:
                    print "{:>2}{:>5}{:>10}{:>2}{:>2}".format(int(data[row_d,0]),101,int(patch[row_p,1]),1,1)
                else:
                    print "{:>2}{:>5}{:>10}{:>2}{:>2}".format(int(data[row_d,0]),101,int(patch[row_p,1]),0,0)
            if nx==1 or ny==1:
                print "{:>2}{:>5}{:>10}{:>2}{:>2}".format(int(data[row_d,0]),101,int(patch[row_p,1]),0,0)
        if alpha>90 and alpha<180:
            if nx==1 or ny==1 or nz==1:
                x2=x+1
                while x2<=1199:
                    y2=int(y+(x2-x)*(np.tan(np.deg2rad(alpha-90))))
                    if x2>=0 and x2<=1199 and y2<=799 and y2>=0:
                        h2=a[x2,y2]
                    if x2<0 or x2>1199 or y2<0 or y2>799:
                        h2=0
                    eletangle1=np.degrees(np.arctan((h2-z)/np.sqrt(((x2-x)*10)**2+((y2-y)*10)**2)))
                    if eletangle1>=data[row_d,2]:
                        break
                    x2+=1
                if x2==1200:
                    print "{:>2}{:>5}{:>10}{:>2}{:>2}".format(int(data[row_d,0]),101,int(patch[row_p,1]),1,1)
                else:
                    print "{:>2}{:>5}{:>10}{:>2}{:>2}".format(int(data[row_d,0]),101,int(patch[row_p,1]),0,0)
            if nx==-1 or ny==-1:
                print "{:>2}{:>5}{:>10}{:>2}{:>2}".format(int(data[row_d,0]),101,int(patch[row_p,1]),0,0)
        if alpha>180 and alpha<270:
            if nx==1 or ny==-1 or nz==1:
                x2=x+1
                while x2<=1199:
                    y2=int(y-(x2-x)*(np.tan(np.deg2rad(alpha-180))))
                    if x2>=0 and x2<=1199 and y2<=799 and y2>=0:
                        h2=a[x2,y2]
                    if x2<0 or x2>1199 or y2<0 or y2>799:
                        h2=0
                    eletangle1=np.degrees(np.arctan((h2-z)/np.sqrt(((x2-x)*10)**2+((y2-y)*10)**2)))
                    if eletangle1>=data[row_d,2]:
                        break
                    x2+=1
                if x2==1200:
                    print "{:>2}{:>5}{:>10}{:>2}{:>2}".format(int(data[row_d,0]),101,int(patch[row_p,1]),1,1)
                else:
                    print "{:>2}{:>5}{:>10}{:>2}{:>2}".format(int(data[row_d,0]),101,int(patch[row_p,1]),0,0)
            if nx==-1 or ny==1:
                print "{:>2}{:>5}{:>10}{:>2}{:>2}".format(int(data[row_d,0]),101,int(patch[row_p,1]),0,0)

        row_p+=1
    row_d+=1
fo.close()
