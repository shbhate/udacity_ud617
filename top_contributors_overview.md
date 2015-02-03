# Top Contributors overview

## Problem description

Find the top 5 contributors in the discussion forum represented by the input file 'student_test_posts.csv'. 
Every question / answer / comment made by a student is considered as a contribution, i.e. we want to find the students who have the largest presence on the forum.

## Solution using MapReduce

The Mappers would process each record assigned to them and output the author for each node post. 

To find the top 5 contributors in the whole forum, the outputs from all mappers must be processed at a single place, i.e. only one reducer is to be used to process all the keys (authors). The reducer will count the number of posts created by an author and keep a running list of the top 5 contributing authors found so far. After processing all the keys, this list will contain the top 5 contributors in this forum.

## Relevant files

### Input file - student_test_posts.csv

### Mapper - top_contributors_mapper.py

### Reducer - top_contributors_reducer.py

### Output / Result file - top_contributors_output.txt