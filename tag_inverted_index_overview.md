# Tag inverted index overview

## Problem Description

An inverted index was constructed for the file 'forum_node.tsv' using MapReduce during the course exercises.The constructed inverted index provided a search lookup for the forum posts which contained the particular word. I suggested an improvement to this search functionality by instead creating an inverted index for the tags found in the forum posts, i.e. instead of words, the index shall contain the list of forum posts which contain a specific tag.

## Solution using MapReduce

The index building process for the tags would be similar to the one followed during the construction of the word inverted index. The mapper would process each record from the file to produce a key-value pair in the below format  
**'tag' 'id of the node containing the tag'**  

The combiners / reducers would receive the mapper / combiner output respectively sorted byt the key (tag). For each key (tag), they will print the list of nodes containing the tag and also the length of this list  
**'tag' 'length of following node list' 'list of nodes containing the tag'**

## Relevant files

### Input file

'forum_node.tsv' file is too big for uploading on GitHub. One can download this file from the Udacity course page.

### Mapper

##### tag_inverted_index_mapper.py

### Reducer

##### tag_inverted_index_combiner_reducer.py

### Output / Result file

##### tag_inverted_index_output.txt