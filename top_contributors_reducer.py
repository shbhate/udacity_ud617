#!/usr/bin/python

# Reducer - top contributors
# Input record format - <authorId>
# Key is authorId, value is 1 for all records.
# Output - Top 5 contributors and the number of posts authored by them (postCount), in descending order of the postCount. 
# Output record format - <authorId>	<number of posts authored by this user>

import sys
import bisect

# Initialize the tracking and accumulator variables.
topContributorsList = []
prevAuthor = None
postCount = 0

for line in sys.stdin:
	# Get the key for this record.
	currAuthor = line.strip()

	# Check if we are finished with processing all records for the key (author) in prevAuthor. If needed, insert this key's tuple into the topContributorsList (if required) in a sorted fashion and then prune the list to only contain the top 5 contributors found so far. Reset the accumulator variable for the new author.
	if (prevAuthor and  prevAuthor != currAuthor):
		tuple = [postCount, prevAuthor]
		if (len(topContributorsList) < 5):			
			bisect.insort(topContributorsList, tuple)		
		else:
			lowest = topContributorsList[0][0]
			if (postCount > lowest):
				bisect.insort(topContributorsList, tuple)
				topContributorsList = topContributorsList[-5:]
		postCount = 0

	# Increment this author's contribution count by the value(1)
	postCount += 1
	prevAuthor = currAuthor

# Completed processsing all the records. If needed, add the last key tuple in the topContributorrsList in a sorted fashion. If the length of the list exceeds 5, prune the list to only contain the top 5 contributors in it.
if(prevAuthor):
	tuple = [postCount, prevAuthor]
        if (len(topContributorsList) < 5):
                bisect.insort(topContributorsList, tuple)
        else:
                lowest = topContributorsList[0][0]
                if (postCount > lowest):
			bisect.insort(topContributorsList, tuple)
        	        topContributorsList = topContributorsList[-5:]

# Done with processing all the keys. The topContributorsList now contains the top 5 contributors, in ascending order of the number of posts authored.  Reverse the list and then print each author and the number of posts contributed by him/her. 
topContributorsList.reverse()
for tuple in topContributorsList:
	print "{0}\t{1}".format(tuple[1], tuple[0])	
