import math
from display import *

AMBIENT = 0
DIFFUSE = 1
SPECULAR = 2
LOCATION = 0
COLOR = 1
SPECULAR_EXP = 3

#lighting functions
def get_lighting(normal, view, ambient, light, areflect, dreflect, sreflect ):
    illu=[]
    normalize(light[0])
    normalize(normal)
    normalize(view)
    ambient=calculate_ambient(ambient,areflect)
    diffuse=calculate_diffuse(light,dreflect,normal)
    specular=calculate_specular(light,sreflect,view,normal)
    for i in range(3):
        illu.append(ambient[i]+diffuse[i]+specular[i])
    limit_color(illu)
    return illu
 
def calculate_ambient(alight, areflect):
    toRet=[]
    for i in range(3):
        toRet.append(int(alight[i]*areflect[i]))
    return toRet

def calculate_diffuse(light, dreflect, normal):
    p=light[1] ##light color (r,g,b)
    normalize(normal)
    normalize(light[0])
    dotP=dot_product(normal,light[0])
    if dotP<0:
        dotP=0
    toRet=[]
    for i in range(3):
        #print "val "+str(p[i]*dreflect*dotP)
        #print "a "+str(p[i]*dreflect[i]*dotP)
        toRet.append(int(p[i]*dreflect[i]*dotP))
    return toRet

def calculate_specular(light, sreflect, view, normal):
    p=light[1]
    normalize(normal)
    normalize(light[0])
    normalize(view)
    dot1=dot_product(normal,light[0])
    prod1=2*dot1
    normal2=[prod1*normal[0],prod1*normal[1],prod1*normal[2]]
    prod3=subtract_vectors(normal2,light[0])
    dot2=dot_product(prod3,view)
    toRet=[]
    for i in range(3):
        toRet.append(int(p[i]*sreflect[i]*(dot2**SPECULAR_EXP)))
    return toRet

def limit_color(color):
    for i in range(3):
        if color[i]>255:
            color[i]=255
        elif color[i]<0:
            color[i]=0

#vector functions
def normalize(vector):
    mag=math.sqrt(vector[0]**2+vector[1]**2+vector[2]**2)+0.0
    vector[0]=vector[0]/mag
    vector[1]=vector[1]/mag
    vector[2]=vector[2]/mag

def dot_product(a, b):
    val=a[0]*b[0]+a[1]*b[1]+a[2]*b[2]
    return val

def subtract_vectors(a,b):
    toRet=[]
    for i in range(3):
        toRet.append(a[i]-b[i])
    return toRet

def calculate_normal(polygons, i):

    A = [0, 0, 0]
    B = [0, 0, 0]
    N = [0, 0, 0]

    A[0] = polygons[i+1][0] - polygons[i][0]
    A[1] = polygons[i+1][1] - polygons[i][1]
    A[2] = polygons[i+1][2] - polygons[i][2]

    B[0] = polygons[i+2][0] - polygons[i][0]
    B[1] = polygons[i+2][1] - polygons[i][1]
    B[2] = polygons[i+2][2] - polygons[i][2]

    N[0] = A[1] * B[2] - A[2] * B[1]
    N[1] = A[2] * B[0] - A[0] * B[2]
    N[2] = A[0] * B[1] - A[1] * B[0]

    return N
