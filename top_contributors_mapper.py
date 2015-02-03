#!/usr/bin/python

# Mapper - top contributors
# Input record format - Row format as in file student_posts.csv 
# Output record format - <authorId> 
# Key is authorId. value is 1 for all posts (1 post = 1 contribution) , hence it is not printed. 		
import sys
import csv

# Each iteration of the reader shall fetch a list of strings obtained by splitting the corresponding row using the delimiter character.
reader = csv.reader(sys.stdin, delimiter = '\t')

# Skip the first row, it contains the names of the attributes, and not the actual attribute data
reader.next()
for row in reader:
	if (len(row) != 19):
		# Unexpected input. Continue to next row
		continue

	# Print the key (id of the post author).Value is not printed as it is 1 for all records.
	authorId = row[3]
	print "{0}".format(authorId)
