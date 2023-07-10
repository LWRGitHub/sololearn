""" PY: SoloLearn 

Multiples

Task: 
Given an integer number, output the sum of all the multiples of 3 and 5 below that number. 
If a number is a multiple of both, 3 and 5, it should appear in the sum only once.

Input Format: 
An integer.

Output Format: 
An integer, representing the sum of all the multiples of 3 and 5 below the given input.

Sample Input: 
10

Sample Output:
23


Explanation: 
The numbers below 10 that are multiples of 3 or 5 are 3, 5, 6 and 9.
The sum of these numbers is 3+5+6+9=23


SoloLearn (2023) Multiples: https://www.sololearn.com 

"""

num = int(input())
sum = 0

while num > 0:
	num -= 1
	if num % 3 == 0 or num % 5 == 0: 
		sum += num

print(sum)


	
