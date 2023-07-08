""" PY: SoloLearn 

Isogram Detector 

An isogram is a word that has no repeating letters, whether they are consecutive or non-consecutive.  
Your job is to find a way to detect if a word is an isogram.

Task: Write a program that takes in a string as input, detects if the string is an isogram and outputs true or false based on the result.
 
Input Format: 
A string containing one word.

Output Format: 
A string: true or false.

Sample Input: 
turbulence

Sample Output: 
false 


Explanation: 
The word turbulence has multiple "u" and "e" in it, which would mean it is not an isogram.


SoloLearn (2023) Isogram Detector: https://www.sololearn.com 

"""

def isogram(word):

	letter_count = set()
	for l in word:
	
		if l in letter_count:
			return 'false'
			
		letter_count.add(l)

	return 'true'

print(isogram(str(input())))



	
	
