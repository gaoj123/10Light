import math
from display import *

AMBIENT = 0
DIFFUSE = 1
SPECULAR = 2
LOCATION = 0
COLOR = 1
SPECULAR_EXP = 4

#lighting functions
def get_lighting(normal, view, ambient, light, areflect, dreflect, sreflect ):
    illu=[]
    ambient=calculate_ambient(ambient,areflect)
    diffuse=calculate_diffuse(light,dreflect,normal)
    specular=calculate_specular(light,sreflect,view,normal)
    for i in range(3):
        illu.append(ambient[i]+diffuse[i]+specular[i])
    limit_color(illu)
    return [illu[0],illu[1],illu[2]]
        
def calculate_ambient(alight, areflect):
    return [alight[0]*areflect,alight[1]*areflect,alight[2]*areflect]

def calculate_diffuse(light, dreflect, normal):
    p=light[1] ##light color (r,g,b)
    normalize(normal)
    normalize(light)
    dotP=dot_product(normal,light[0])
    return [p[0]*dreflect*dotP,p[1]*dreflect*dotP,p[2]*dreflect*dotP]

def calculate_specular(light, sreflect, view, normal):
    p=light[1]
    normalize(normal)
    normalize(light)
    normalize(view)
    dot1=2*dot_product(normal,light)*normal-light
    dot2=dot_product(dot1,view)
    toRet=[]
    for i in range(3):
        toRet.append(p[i]*sreflect*(dot2**SPECULAR_EXP))
    return toRet

def limit_color(color):
    if color[0]>255:
        color[0]=255
    if color[1]>255:
        color[1]=255
    if color[2]>255:
        color[2]=255

#vector functions
def normalize(vector):
    mag=Math.sqrt(a[0]**2+a[1]**2+a[2]**2)
    vector[0]=vector[0]/mag
    vector[1]=vector[1]/mag
    vector[2]=vector[2]/mag

def dot_product(a, b):
    val=a[0]*b[0]+a[1]*b[1]+a[2]*b[2]
    return val

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
