"""

YouTube Link Finder


You and your friends like to share YouTube links all throughout the day. You want to keep track of all the videos you watch in your own personal notepad, but you find that keeping the entire link is unnecessary. 
Keep the video ID (the combination of letters and numbers at the end of the link) in your notepad to slim down the URL.

Task: 
Create a program that parses through a link, extracts and outputs the YouTube video ID.

Input Format: 
A string containing the URL to a YouTube video. The format of the string can be in "https://www.youtube.com/watch?v=kbxkq_w51PM" or the shortened "https://youtu.be/KMBBjzp5hdc" format.

Output Format: 
A string containing the extracted YouTube video id.

Sample Input: 
https://www.youtube.com/watch?v=RRW2aUSw5vU

Sample Output: 
RRW2aUSw5vU


Note that the input can be in two different formats.


SoloLearn (2023) YouTube Link Finder: https://www.sololearn.com

"""

url = str(input())

if "=" in url:
	print(url.split('=')[1])
else: 
	url_arr = url.split('/')
	print(url_arr[len(url_arr)-1])

	
	
