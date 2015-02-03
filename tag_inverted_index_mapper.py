#!/usr/bin/python

# Mapper - tag inverted index
# Expected input record format - Row format as in file 'forum_node.tsv'
# Output record format - <tag> <node id>
# Key is tag , value is the id of the post that contained this tag

import sys
import csv

# Each iteration of the reader shall contain a list of strings obtained by splitting the corresponding row using the delimiter character.
reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t') 

# Skip the first row, it contains only the attribute names, not the attribute data.
reader.next()
for line in reader:
	if (len(line) == 19):
		# Get the node id and the tag string for this post.
		tagString = line[2]
		nodeId = line[0]
	else:
		# Unexpected input. Skip to the next record.
		continue
	
	# Split the tag string to get the list of tags in this post. For each of these tags, print the tag and the node id
	tags = tagString.strip().split()
	for tag in tags:
		record = [tag, nodeId]
		writer.writerow(record)
