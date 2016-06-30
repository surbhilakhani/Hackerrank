# Hackerrank
Algorithms


Given an array of integers, calculate which fraction of its elements are positive, which fraction of its elements are negative, and which fraction of its elements are zeroes, respectively. Print the decimal value of each fraction on a new line.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

Input Format

The first line contains an integer, , denoting the size of the array. 
The second line contains  space-separated integers describing an array of numbers .

Output Format

You must print the following  lines:

A decimal representing of the fraction of positive numbers in the array.
A decimal representing of the fraction of negative numbers in the array.
A decimal representing of the fraction of zeroes in the array.

Solution:

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
count = [0,0,0]
for i in xrange(len(arr)):
    if arr[i]>0: count[0]+=1
    elif arr[i]<0: count[1]+=1
    else: count[2]+=1
print float(count[0])/len(arr)
print float(count[1])/len(arr)
print float(count[2])/len(arr)
