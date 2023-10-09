import sys

fname1 = sys.argv[1]
print(fname1)
fname2 = sys.argv[2]
print(fname2)


# dict format required for csv
myDict = [{'word': 'a', 'frequency': 1000}, {'word':'the', 'frequency': 700}, {'word': 'me', 'frequency':20} ]
# code to write above dict to csv
import csv
with open('sampleScriptOutput.csv', 'w') as csvop:
	# creating dictionary writer object
	writerObj = csv.DictWriter(csvop, fieldnames =
	['word', 'frequency'])
	# write fieldnames
	writerObj.writeheader()
	writerObj.writerows(myDict)
