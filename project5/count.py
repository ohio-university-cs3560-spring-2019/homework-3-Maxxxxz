#
#	Michael Cooper
#	Ohio University CS3560
#	count.py
#	Counts the number of lines, words, and characters in all files in a directory
#

from os import listdir
import os
import sys

lines = 0
words = 0
chars = 0

dir = str(sys.argv[1])

if not os.path.isdir(dir):		#should never happen
	print "Invalid Directory"
	sys.exit(1)

files = []

for f in listdir(dir):						#for every string item f returned by listdir(dir)
	if os.path.isfile(os.path.join(dir, f)):		#if the item f is a file (not a dir)
		files.append(os.path.join(dir, f))		#append item f to files list


#for file in files:						
#	print file

for inFile in files:						#this might not be entirely correct because it will count symbols as words. This should not matter, though.
	with open(inFile, 'r') as o:
		for line in o:
			contents = line.split()			#split line into an array of words
			lines += 1				#one line at a time
			words += len(contents)			#words will equal the length of the contents array after split
			chars += len(line)			#characters will equal the total length of the line

print("Lines: ", lines)
print("Words: ", words)
print("Chars: ", chars)