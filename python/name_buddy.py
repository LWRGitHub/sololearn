"""

Name Buddy


You are grouped into groups for a project, and you are supposed to come up with as many famous scientists who have the same first letter of their name as you as possible. 
Will you have to come up with the answers on your own, or is there somebody in your group that you can work with?

Task: 
Determine if anyone in your group has the same first letter of their name as you.

Input Format: 
A string of your group members' names separated by spaces, and then a string of your name.

Output Format: 
A string that says 'Compare notes' if you have a name buddy, or 'No such luck' if you have to work on this alone.

Sample Input: 
Becky Joan Fred Trey
Brad

Sample Output: 
Compare notes


Explanation: 
Congratulations! You have a name buddy since Brad and Becky both start with a 'B'. You can work together. 


SoloLearn (2023) Name Buddy: https://www.sololearn.com

"""


names = str(input()).split(' ')
your_name = str(input())

no_budy = True
for name in names:
	if your_name[0] == name[0]:
		print('Compare notes')
		no_budy = False
		break

if no_budy:
	print('No such luck')

	
	
