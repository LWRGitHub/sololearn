"""

Secret Message


You are trying to send a secret message, and you've decided to encode it by replacing every letter in your message with its corresponding letter in a backwards version of the alphabet. 
What do your messages look like?

Task: 
Create a program that replaces each letter in a message with its corresponding letter in a backwards version of the English alphabet.

Input Format: 
A string of your message in its normal form.

Output Format: 
A string of your message once you have encoded it (all lower case).

Sample Input: 
Hello World

Sample Output: 
svool dliow


Explanation: 
If you replace each letter in 'Hello World' with the corresponding letter in a backwards version of the alphabet, you get 'svool dliow'. 


SoloLearn (2023) Secret Message: https://www.sololearn.com

"""


message = str(input()).lower()
backwards_alphabet = {'a':'z','b':'y', 'c':'x','d':'w','e':'v','f':'u','g':'t','h':'s','i':'r','j':'q','k':'p','l':'o','m':'n','n':'m','o':'l','p':'k','q':'j','r':'i','s':'h','t':'g','u':'f','v':'e','w':'d','x':'c','y':'b','z':'a',}
secret_message = ''

for c in message:
	if c in backwards_alphabet:
		secret_message += backwards_alphabet[c]
	else: 
		secret_message += c
	
print(secret_message)

	
	
