# bezier2svg
Converts Bezier's point matrix in csv format into svg file.

Python program created for education purpouse. 
The aim of tis program is to demonstrate Cubic B´ezier Curve formula on python. 

Program takes a file of the following format
<p1_x1>,<p1_y1>,<p1_x2>,<p1_y2>,<p1_x3>,<p1_y3>,<p1_x4>,<p1_y4>
<p2_x1>,<p2_y1>,<p2_x2>,<p2_y2>,<p2_x3>,<p2_y3>,<p2_x4>,<p2_y4>
. . . .
<pN_x1>,<pN_y1>,<pN_x2>,<pN_y2>,<pN_x3>,<pN_y3>,<pN_x4>,<pN_y4>
where each line is the coordinates of a separate B´ezier curve with end points
at (x1, y1) and (x4, y4).
Then creates an SVG (scalable vector graphics) file of the
same name as the input file but with the .svg extention. The SVG file
contain the commands necessary to draw all the B´ezier curves in the
input file
