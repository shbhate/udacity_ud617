#!/usr/bin/python

# Mapper- tag answer:question ratio - Stage 2 (find the answer:question ratio for a tag)
# Expected input record format from Stage 1 - <questionId>	<number of answers for this question>	<string containing tags associated with this question> 
# Output record format - <tag>	<number of answers>
# Key is tag, value is the number of answers to a question containing this tag.

import sys

for line in sys.stdin:
	fields = line.strip().split('\t')
	if (len(fields) != 3):
		# Unexpected input, skip to next record. Check the code for reducer of stage 1.
		continue

	# Split the tag string to get the list of tags for this question. For each tag in this list, print the tag and the answer count for this question. 
	answerCount = fields[1] 
	tagString = fields[2]
	tags = tagString.strip().split()
	for  tag in tags:
		print "{0}\t{1}".format(tag, answerCount)
