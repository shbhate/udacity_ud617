# Tag AnswerToQuestionRatio overview

## Problem description

For the discussion forum data represented by the input file 'student_test_posts.csv', we are interested in checking if questions marked with certain tags get more attention from students (in the form of answer posts), i.e. we need to **find the (number of answers: number of questions) ratio for a particular tag** found in the discussion forum questions.

## Solution using MapReduce

This problem requires two MapReduce stages. This is because for an answer post, the string containing the tags found in its parent question node is not directly accessible.

### MapReduce Stage 1

This stage finds the number of answer posts to a particular question node and the tag string associated with the question. 

The mapper will process the file records and will produce an output in this format (records pertaining to comment posts will be ignored) – 
**<id of parent question> <marker to indicate question / answer> 	<if marker is a question, string of tags found in this question>**

e.g.
11789	Q	lessons
11765	Q	cs101	homework
11765	A
7789	Q	cs253
11765	A

The reducer will count the total number of answers for a key (question node); store the tag string for that question and then print output in below format – 
**<Question node id>	<number of answers to this question>	<string containing tags found in this question>**

e.g.
11765	2	cs101	homework

### Interlude between stage 1 and stage 2: Combine reducer outputs into a single file

Many reducers may independently work in parallel during stage 1 and each produce a separate output file by the name “part-<part number>” (e.g part-00001). To concatenate these results into a single file, the getmerge command can be used as follows - 
hadoop fs -getmerge <stage_1_outputdir path>    <local path to new file which will contain concatenated results>

After executing this command, the output file can be uploaded to HDFS using the put command
hadoop fs –put    <stage_1_combined_input_file>    <path to inputdir for stage 2>


### MapReduce Stage 2

This stage takes the output of stage 1 to find the (number of answers: number of questions) ratio for each tag found in the discussion forum questions.  

The mappers process the output of stage 1 line by line to produce key-value pairs in the following format – 
**<tag present in  a particular question>	<number of answers to this question>**

e.g.
cs101	2
homework 4
cs101	4

The count of key-value pairs for a particular key (tag) thus represents the total number of questions containing this tag, and the sum of all the values for a particular key will represent the total number of answers posts to all the questions containing this key (tag). The reducers for this stage make these computations to arrive at the (number of answers: number of questions) ratio for this tag. For each key (tag), the reducer output record looks like – 
**<tag>	<number of questions>	<number of answers>	<answers:questions ratio>**

e.g. 	cs101	2	6	3.0

## Relevant files

### Input file - student_test_posts.csv

### Mappers - tag_AnswerToQuestionRatio_stage1_mapper.py, tag_AnswerToQuestionRatio_stage2_mapper.py

### Reducers - tag_AnswerToQuestionRatio_stage1_reducer.py, tag_AnswerToQuestionRatio_stage2_reducer.py

### Output / Result files - tag_AnswerToQuestionRatio_stage1_output.txt, tag_AnswerToQuestionRatio_stage2_output.txt