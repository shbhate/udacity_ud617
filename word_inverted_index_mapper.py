#!/usr/bin/python

# Mapper - word inverted index
# Expected input record format - Row format as in file 'forum_node.tsv'
# Output record format - <word>	<node id>
# Key is a word found in the post body, value is the id of the post that contained this word

import sys
import csv
import string

# Each iteration of the reader shall contain a list of strings obtained by splitting the corresponding row by the delimiter character.
reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t')

# Skip the first row as it only contains the attribute names, not the actual attribute data.
reader.next()
for line in reader:
	if (len(line) == 19):
		# Get the node id and the post body for this record.
		body = line[4]
		nodeId = line[0]
	else:
		# Unexpected input. Skip to next row.
		continue
	
	# Remove the punctuation marks from the post body, then split the body on whitespace to get the list of words.
	# For each word in the post body, print the word and the node id of the post.
	body = body.translate(string.maketrans('.,!?:;"()<>#$=-/','                ' ))
	words = body.strip().split()
	for word in words:
		word = word.lower()
		record = [word, nodeId]
		writer.writerow(record)
