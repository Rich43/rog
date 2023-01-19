'''
In this challenge, you will be given a set of circles, defined by their centers and radii.
Your goal is to find the bounding rectangle which will contain all of the circles completely.

Write a program that determines the vertices of the bounding rectangle with sides parallel to the axes.
Input Description

Each line will contain a comma separated center and radius for a circle.
Output Description

The format of the output will be comma separated coordinates, rounded to 3 decimal places.
Challenge Input

1,1,2
2,2,0.5
-1,-3,2
5,2,1

'''
import re

data = '''1,1,2
2,2,0.5
-1,-3,2
5,2,1'''
data = data.splitlines()

x_y_r_data = []
x_data = []
y_data = []
r_data = []
for line in data:
    x = re.findall('[+-]?[0-9*\.[0-9]+', line)
    x_y_r_data.append(x)

for l in x_y_r_data:
    x_data.append((float(l[0]), float(l[2])))
    y_data.append((float(l[1]), float(l[2])))
    r_data.append(float(l[2]))
print(x_y_r_data)
print(x_data)
print(y_data)
print(r_data)

x_min = min(x_data)
x_min = x_min[0] - x_min[1]
x_min = '{0: .3f}'.format(x_min)
x_max = max(x_data)
x_max = x_max[0] + x_max[1]
x_max = '{0: .3f}'.format(x_max)
y_min = min(y_data)
y_min = y_min[0] - y_min[1]
y_min = '{0: .3f}'.format(y_min)
y_max = max(y_data)
y_max = y_max[0] + y_max[1]
y_max = '{0: .3f}'.format(y_max)

print('{0}{3}{2}{4}{1}{0}{3}{2}{6}{1}{0}{5}{2}{6}{1}{0}{5}{2}{4}{1}'
      .format('(', '), ', ', ', x_min, y_min, x_max, y_max))


#part2    @MartínVacasVignolo the new coordinates after rotation of the cordinates at an angle f for a point (x,y)
# {x = Xcos(f) - Ysin(f)}{y = Xcos(f) + Ysin(f)}