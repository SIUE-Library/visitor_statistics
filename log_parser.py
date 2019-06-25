#Programmer: Jacob Grubb (jagrubb@siue.edu)
#Organization: Lovejoy Library
#Gist: Regex Gatherer

import re
import os
import sys

if(len(sys.argv) < 4):
	print("Invalid syntax:\nCorrect syntax: python3 log_parser.py [directory] [regex file] [output file]")
	sys.exit(1)

dirName = sys.argv[1]
#Get active directory of log files (dir)
listOfFiles = [file for file in os.listdir(dirName) if os.path.isfile(os.path.join(dirName, file))]
#source: https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory

regexFileName = sys.argv[2]
#import regex statement
regexStatements = []
with open(regexFileName, 'r') as regFile:
	regexStatements = regFile.readlines()
regexList = []
for statement in regexStatements:
	regexList.append(re.compile(statement[:-1]))
#create outputfile (OF)
outputFileName = sys.argv[3]
with open(outputFileName, 'w') as outFile:
#for each file (f) in active directory (dir)
	for file in listOfFiles:
		#load file (f)
		with open((dirName + file), 'r') as inFile:
		#for each line (l) in file (f)
			for line in inFile:
			#parse the timestamp and ip address > string s
				for reggie in regexList:
					results = reggie.findall(line)
					if(results):
						for result in results:
							outFile.write(result + '\n')
							#append s > OF
