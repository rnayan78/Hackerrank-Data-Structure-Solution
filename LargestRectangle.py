"""
Skyline Real Estate Developers is planning to demolish a number of old, unoccupied buildings and construct a shopping mall in their place. Your task is to find the largest solid area in which the mall can be constructed.

There are a number of buildings in a certain two-dimensional landscape. Each building has a height, given by . If you join  adjacent buildings, they will form a solid rectangle of area .

For example, the heights array . A rectangle of height  and length  can be constructed within the boundaries. The area formed is .

Function Description

Complete the function largestRectangle int the editor below. It should return an integer representing the largest rectangle that can be formed within the bounds of consecutive buildings.

largestRectangle has the following parameter(s):

h: an array of integers representing building heights
Input Format

The first line contains , the number of buildings.
The second line contains  space-separated integers, each representing the height of a building.

Constraints

Output Format

Print a long integer representing the maximum area of rectangle formed.

Sample Input

5
1 2 3 4 5
Sample Output

9
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.
def largestRectangle(h):
    stack = list ()

    index = 0
    max_area = 0
    while index < len(h):

        if (not stack) or (h[stack[-1]] <= h[index]):
            stack.append(index)
            index += 1

        else:
            top_of_stack = stack.pop()

            area = (h[top_of_stack]* ((index - stack[-1] -1) if stack else index))

            max_area = max(max_area, area) 
        
    while stack: 
          
        
        top_of_stack = stack.pop() 
  
         
        area = (h[top_of_stack] * 
              ((index - stack[-1] - 1)  
                if stack else index)) 
        
        max_area = max(max_area, area)

    return max_area
 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)
    print(result)

    fptr.write(str(result) + '\n')

    fptr.close()
