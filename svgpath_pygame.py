from __future__ import division  # we need floating division
import pygame
import sys
from xml.dom import minidom
from svg.path import Path, Move, Line, Arc, CubicBezier, QuadraticBezier, Close, parse_path
import argparse


#if (len(sys.argv) == 1):
#    print('Utilisation:', sys.argv[0],
#          'nombre_de_points_par_courbes ','\n -i input svg file','\n -o output txt file')
#    exit(1)

parserargs = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')

parserargs.add_argument('resolution_courbe')
parserargs.add_argument('-i','--inputFile')
parserargs.add_argument('-o','--outputFile')

args=parserargs.parse_args()

print(args)
print(int(args.resolution_courbe))
print("\n\n\n") # 

# svg.path point method returns a complex number p, p.real and p.imag can pull the x, and y
# # on 0.0 to 1.0 along path, represent percent of distance along path
n = int(args.resolution_courbe)  # number of line segments to draw
#nomOutput=

scaling=5
x0=0
y0=950

file1 = open(args.outputFile, "w")
file1.write("")
file1.close()

mydoc = minidom.parse(args.inputFile)
print(mydoc)
pygame.init()                                  # init pygame
surface = pygame.display.set_mode((1000,1000)) # get surface to draw on
surface.fill(pygame.Color('white'))            # set background to white

path_tag = mydoc.getElementsByTagName("path")
print(path_tag)



for j in range(len(path_tag)):

    if path_tag[j].hasAttribute('nom')==False:
            print("\n",path_tag[j])
            continue
    

    style_string = path_tag[j].attributes['style'].value

    print("on continue la for")
# getting index of substrings
    idx1 = style_string.find("stroke:")
    idx2 = idx1+14
# length of substring 1 is added to
# get string from next character
    color = style_string[idx1 + len("stroke:"): idx2]
    
    d_string = path_tag[j].attributes['d'].value
    string=path_tag[j].attributes['nom'].value
    
    Path_elements = parse_path(d_string)

   
    pts = [ ((p.real/scaling)+x0,(p.imag/scaling)+y0) for p in (Path_elements.point(i/n) for i in range(0, n+1))]
        
    print_pts = [ (str(p.real)+';'+str(-1*p.imag)) for p in (Path_elements.point(i/n) for i in range(0, n+1))]
        
    string = string + '\n' + "Xp ; Yp"

    for i in range(0,n+1):
        string= string + '\n' + str(print_pts[i])# + ' ' + str(print_pts[i]) 
    
    pygame.draw.aalines( surface,pygame.Color(color), False, pts) # False is no closing
    print(string)
    file1 = open(args.outputFile, "a")
    file1.write(string)
    file1.close()

pygame.display.update() # copy surface to display




# pts = []
# for i in range(0,n+1):
#     f = i/n  # will go from 0.0 to 1.0
#     complex_point = path.point(f)  # path.point(t) returns point at 0.0 <= f <= 1.0
#     pts.append((complex_point.real, complex_point.imag))






while True:  # loop to wait till window close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

