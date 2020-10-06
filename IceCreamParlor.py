"""unny and Johnny like to pool their money and go to the ice cream parlor. Johnny never buys the same flavor that Sunny does. The only other rule they have is that they spend all of their money.

Given a list of prices for the flavors of ice cream, select the two that will cost all of the money they have.

For example, they have  to spend and there are flavors costing . The two flavors costing  and  meet the criteria. Using -based indexing, they are at indices  and .

Function Description

Complete the icecreamParlor function in the editor below. It should return an array containing the indices of the prices of the two flavors they buy, sorted ascending.

icecreamParlor has the following parameter(s):

m: an integer denoting the amount of money they have to spend
cost: an integer array denoting the cost of each flavor of ice cream
Input Format

The first line contains an integer, , denoting the number of trips to the ice cream parlor. The next  sets of lines each describe a visit. Each trip is described as follows:

The integer , the amount of money they have pooled.
The integer , the number of flavors offered at the time.
 space-separated integers denoting the cost of each flavor: .
Note: The index within the cost array represents the flavor of the ice cream purchased.

Constraints

, ∀ 
There will always be a unique solution.
Output Format

For each test case, print two space-separated integers denoting the indices of the two flavors purchased, in ascending order."""















t = input()
t = int(t)
for i in range(0,t):
    m = input()
    m = int(m)
    n = input()
    n = int(n)
    li = input()  #list of elements from input
    li = [int(i) for i in li.split(' ')]
    for i in range(0,len(li)):
        if (m-li[i]) in li[i+1:len(li)]: #check if the difference of m and element in the list exist, if yes then pick the index of those two elements.
            li1 = li[i+1:len(li)] #if the same element appears twice, for example m=4 and the list has 2 2 4 1, this line helps in picking the next '2' at the position 1(starting from 0)
            x = li1.index(m-li[i]) #position of the next element which forms the sum equal to m.
            print (i+1, i+x+2) #Since index starts from 0 add 1 to i, to print the second index, remember we have copied all the elements after position i, so i+x, since the index starts from 0, i+x+1, we left the element at position i while copying to li1, hence i+x+2
            break
