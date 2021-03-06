"""
An array is a type of data structure that stores elements of the same type in a contiguous block of memory. In an array, , of size , each memory location has some unique index,  (where ), that can be referenced as  (you may also see it written as ).

Given an array, , of  integers, print each element in reverse order as a single line of space-separated integers.

Note: If you've already solved our C++ domain's Arrays Introduction challenge, you may want to skip this.

Input Format

The first line contains an integer,  (the number of integers in ).
The second line contains  space-separated integers describing .

"""




import sys
n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
#The following passed the test
print(*reversed(arr))
