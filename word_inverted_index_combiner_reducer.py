#!/usr/bin/python

# Combiner / Reducer - word inverted index

# Combiner input record format - <word>	<node id>
# Key is word, value is id of node which contains this word.
# Combiner output - For each key (word) processed by combiner, output is the number and list of nodes containing that word.# Combiner output record format - <word>	<number of nodes>	<list of nodes>

# Reducer input record format - <word>     <number of nodes>       <list of nodes>
# Key is word, value is list of nodes containing this word (as produced by combiner)
# Reducer output - For each key (word) processed by reducer, output is the number and list of nodes containing that word.
# Reducer output record format - <word>     <number of nodes>       <list of nodes> 

import sys
import string

# Initialize the tracking and accumulator variables.
oldKey = None
nodeList = []

for line in sys.stdin:
	fields = line.strip().split('\t')

	# For combiner, input record is like - <word>	<node id>
	# For reducer, input record is like - <word>	<number of nodes>	<list of nodes>
	if ((len(fields) != 2) and (len(fields) != 3)):
		# Unexpected input. Skip to next record.
		continue
	
	# Get the key (word) and value (node id / list of node ids) for this record.
	if (len(fields) == 2):
		thisKey, thisValue = fields
	else:
		thisKey = fields[0]
		thisValue = fields[2]
	# Check if processing has completed for the key in oldKey. If yes, print this key (word), the number of nodes (posts) containing this word, and the list of nodes containing this word.
	if (oldKey and oldKey != thisKey):
		nodeList.sort()
		print "{0}\t{1}\t{2}".format(oldKey, len(nodeList), nodeList)
		#print "{0}\t{1}".format(oldKey, nodeList)
		nodeList = []
	
	# For the reducer, the node list in the input record will contain characters '[],'. Replace these characters by whitespace and then split on whitespace to access each of the nodes in the list.
	nodes = thisValue.translate(string.maketrans('[],','   ')).split()
	for node in nodes:
		nodeList.append(int(node))
	oldKey = thisKey	

# Last key for this reducer. Like previous keys, print this key (word), the number of nodes (posts) containing this word, and the list of nodes containing this word.
if (oldKey):
	nodeList.sort()
        print "{0}\t{1}\t{2}".format(oldKey, len(nodeList), nodeList)
	#print "{0}\t{1}".format(oldKey, nodeList)
