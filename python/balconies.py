"""

Balconies

You are trying to determine which of two apartments has a larger balcony. Both balconies are rectangles, and you have the length and width, but you need the area.

Task 
Evaluate the area of two different balconies and determine which one is bigger.

Input Format 
Your inputs are two strings where the measurements for height and width are separated by a comma. The first one represents apartment A, the second represents apartment B.

Output Format: 
A string that says whether apartment A or apartment B has a larger balcony.

Sample Input 
'5,5'
'2,10'

Sample Output 
Apartment A


Explanation 
Since the area of apartment A's balcony is 25 and the area of apartment B's balcony is 20, Apartment A is the correct answer.


SoloLearn (2023) Balconies: https://www.sololearn.com

"""


balconie_a = str(input()).split(',')
balconie_b = str(input()).split(',')

for i in range(2):
	balconie_a[i] = int(balconie_a[i])
	balconie_b[i] = int(balconie_b[i])
	
area_a = balconie_a[0] * balconie_a[1]
area_b = balconie_b[0] * balconie_b[1]

if area_a > area_b:
	print('Apartment A')
else:
	print('Apartment B')

