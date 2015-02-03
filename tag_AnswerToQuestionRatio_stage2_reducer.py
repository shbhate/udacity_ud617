#!/usr/bin/python

# Reducer- tag- answer:question ratio - Stage 2 (find the answer:question ratio for each tag)
# Expected input record format - <tag> <number of answers>
# Key is tag, value is number of answers to a question containing this tag
# Output - For each key (tag) processed by this reducer, output the number of questions containing this tag, the number of answers to questions containing this tag, and the average ratio of answers:questions.
# Output record format - <tag>	<number of questions>	<number of answers>	<answers:questions ratio>

import sys

# Initialize the tracking and accumulator
totalAnswers = 0
totalQuestions = 0
previousTag = None

for line in sys.stdin:
	fields = line.strip().split('\t')
	if (len(fields) != 2):
		# Unexpected input. Skip to next record. Check the code for mapper stage 2.
		continue

	# Get the key (tag) and value (number of answers) for this record
	currentTag, answerCount = fields
	
	# Check if processing has completed for the key in previousTag. if yes, print the tag, the number of questions, the number of answers and the answers:questions ratio.
	# Reset the accumulator variables for the new key.
	if (previousTag and previousTag != currentTag):
		print "{0}\t{1}\t{2}\t{3}".format(previousTag, totalQuestions, totalAnswers, (totalAnswers/float(totalQuestions)))
		totalAnswers = 0
		totalQuestions = 0

	totalAnswers += int(answerCount)
	totalQuestions += 1
	previousTag = currentTag

# Last key (tag) for this reducer. Like other keys, print the tag, number of questions, number of answers and the answers:questions ratio
if (previousTag):
	print "{0}\t{1}\t{2}\t{3}".format(previousTag, totalQuestions, totalAnswers, float(totalAnswers/float(totalQuestions)))
