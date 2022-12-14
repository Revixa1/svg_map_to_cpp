from __future__ import division  # we need floating division
from svg.path import Path, Line, Arc, CubicBezier, QuadraticBezier, parse_path
import pygame
import sys
from xml.dom import minidom
from svg.path import Path, Line, Arc, CubicBezier, QuadraticBezier, parse_path


# Si il n'y a pas d'arguments à l'appel du programme, montrer comment utiliser
if (len(sys.argv) == 1):
    print('Utilisation:', sys.argv[0],
          'nombre_de_points_par_courbes ')
    exit(1)

print("\n\n\n") # 

# svg.path point method returns a complex number p, p.real and p.imag can pull the x, and y
# # on 0.0 to 1.0 along path, represent percent of distance along path
n = int(sys.argv[1])  # number of line segments to draw
scaling=5
x0=0
y0=950

file1 = open("points.txt", "w")
file1.write("")
file1.close()

mydoc = minidom.parse("./map.svg")

pygame.init()                                  # init pygame
surface = pygame.display.set_mode((1000,1000)) # get surface to draw on
surface.fill(pygame.Color('white'))            # set background to white

path_tag = mydoc.getElementsByTagName("path")

for j in range(len(path_tag)):
    
    

    style_string = path_tag[j].attributes['style'].value

 
# getting index of substrings
    idx1 = style_string.find("stroke:")
    idx2 = idx1+14
# length of substring 1 is added to
# get string from next character
    color = style_string[idx1 + len("stroke:"): idx2]
    
    d_string = path_tag[j].attributes['d'].value
    string=path_tag[j].attributes['nom'].value+"[""][2]="
    
    Path_elements = parse_path(d_string)
    print_pts = [ (('{'+str(p.real))+','+(str(-1*p.imag)+'}')) for p in (Path_elements.point(i/n) for i in range(0, n+1))]
    for a in range(len(print_pts)):
        if a == 0:
            string= string + '{' 
        string = string + print_pts[a]
        if a<len(print_pts)-1:
            string = string + ','
        
    string = string + '};\n'
    pts = [ ((p.real/scaling)+x0,(p.imag/scaling)+y0) for p in (Path_elements.point(i/n) for i in range(0, n+1))]
    pygame.draw.aalines( surface,pygame.Color(color), False, pts) # False is no closing
    print(string)
    file1 = open("points.txt", "a")
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

