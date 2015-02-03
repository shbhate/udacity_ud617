#!/usr/bin/python

# Reducer- tag - answer:question ratio - stage 1 (find the tags and number of answers for each question)
# Expected input record format - Row format as in student_test_posts.csv
# Output record format - <questionId>	<marker>	<if node is a question, string containing tags associated with this question>
# For question nodes, marker is 'Q'. For answers, the marker is 'A'. Comment nodes are ignored.
# Key is question id, value is the tag string (for question nodes) or 1 (for answer nodes, each answer increments the answer count by 1) 

import sys
import csv

# Each iteration of the reader shall contain a list of strings obtained by splitting the corresponding row by the delimiter string.
reader = csv.reader(sys.stdin, delimiter = '\t')

# Ignore the first row, it only contains the attribute names, not actual attribute data.
reader.next()
for row in reader:
	if(len(row) != 19):
		# Unexpected input. Continue to next row.
		continue
	
	# For answer nodes, print the parent question node id and the marker string
	# For question nodes, print the question node id, the marker string and the string containing the tags associated with this question. 
	nodeType = row[5]
	if (nodeType == 'answer'):
		questionId = row[7]
		marker = 'A'
		print "{0}\t{1}".format(questionId, marker)
	else:
		if(nodeType == 'question'):
               		questionId = row[0]
               		tagString = row[2]
               		marker = 'Q'
               		print "{0}\t{1}\t{2}".format(questionId, marker, tagString)
