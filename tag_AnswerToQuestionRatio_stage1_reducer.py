#!/usr/bin/python

# Reducer- tag answer:question ratio - Stage 1 ()
# Expected input record format - <questionId>	<marker>	<if marker is 'Q', string of tags associated with this question> 
# Key is id of question node, value is tag string (for question nodes- marker 'Q') or 1 (for answer nodes- marker 'A')
# Output - For each key (question id) processed by this reducer, output contains the number of answers to this question and the string containing the tags associated with this question.
# Output record format - <questionId>	<number of answers to this question>	<tags found in this question>

import sys

# Initialize the tracking and accumulator variables.
answerCount = 0
prevQuestion = None
tagString = None 

for line in sys.stdin:
	# Records with marker 'Q' have 3 fields- <questionId>	'Q'	<tags>
	# Records with marker 'A' have 2 fields- <questionId>	'A'
	fields = line.strip().split('\t')
	if(len(fields) != 2 and len(fields) != 3):
		# Unexpected input. Skip to next record.
		continue

	# Get the key (question id) and marker for this record.
	currQuestion = fields[0] 
	marker = fields[1]
	
	# Check if processing has finished for the key (question) in prevQuestion. If yes, print this key (question id), number of answers, and the tag string fro this question.
	# Reset the variables for the new key.
	if (prevQuestion and prevQuestion != currQuestion):
		print "{0}\t{1}\t{2}".format(prevQuestion, answerCount, tagString)
		answerCount = 0
		tagString = None
	
	# For records with marker 'A', increment the answer count with the value (1)
	# For records with marker 'Q', store the tag string.
	if (marker == 'A'):
		answerCount += 1
	else:	# marker == 'Q'
		tagString = fields[2]
	prevQuestion = currQuestion

# Last key for this reducer. Like previous keys, print the question id, number of answers, and the tag string.
if (prevQuestion):
	print "{0}\t{1}\t{2}".format(prevQuestion, answerCount, tagString)
