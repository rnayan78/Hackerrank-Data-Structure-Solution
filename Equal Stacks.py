"""
ou have three stacks of cylinders where each cylinder has the same diameter, but they may vary in height. You can change the height of a stack by removing and discarding its topmost cylinder any number of times.

Find the maximum possible height of the stacks such that all of the stacks are exactly the same height. This means you must remove zero or more cylinders from the top of zero or more of the three stacks until they're all the same height, then print the height. The removals must be performed in such a way as to maximize the height.

Note: An empty stack is still a stack.

Input Format

The first line contains three space-separated integers, , , and , describing the respective number of cylinders in stacks , , and . The subsequent lines describe the respective heights of each cylinder in a stack from top to bottom:

The second line contains  space-separated integers describing the cylinder heights in stack . The first element is the top of the stack.
The third line contains  space-separated integers describing the cylinder heights in stack . The first element is the top of the stack.
The fourth line contains  space-separated integers describing the cylinder heights in stack . The first element is the top of the stack.
Constraints

Output Format

Print a single integer denoting the maximum height at which all stacks will be of equal height.

Sample Input

5 3 4
3 2 1 1 1
4 3 2
1 1 4 1
Sample Output

5"""
#!/bin/python3

import os
import sys

#
# Complete the equalStacks function below.
#
def equalStacks(h1, h2, h3):
    sum1, sum2, sum3 = 0, 0, 0

    for i in range(n1):
        sum1 += h1[i]
    
    for i in range(n2):
        sum2 += h2[i]
    
    for i in range(n3):
        sum3 += h3[i]
    
    top1 , top2, top3 = 0, 0, 0
    ans = 0
    while(True):

        if(top1 == n1 or top2 == n2 or top3 == n3):
            return 0

        if (sum1 == sum2 and sum2 == sum3):
            return sum1

        if (sum1 >= sum2 and sum1 >= sum3): 
            sum1 -= h1[top1] 
            top1=top1+1
        elif (sum2 >= sum3 and sum2 >= sum3): 
            sum2 -= h2[top2] 
            top2=top2+1
        elif (sum3 >= sum2 and sum3 >= sum1): 
            sum3 -= h3[top3] 
            top3=top3+1


        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)
    print(result)

    fptr.write(str(result) + '\n')

    fptr.close()
