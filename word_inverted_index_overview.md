# Word inverted index with Combiners - Overview

## Problem Description

An inverted index was constructed for the input file 'forum_node.tsv' using MapReduce during one of the course exercises. In the word inverted index created, each word present in the discussion forum posts has a list of ids of posts which contained that word, along with the total length of this list.  I have suggessted an improvement to the index building process by using combiners during the index computation.

## Solution

The index building process can be made more efficient by using Combiners.
In this case, the combiner has similar logic as the reducer, as it will receive its input sorted by key and then locally process each record to get a list of nodes containing a word. Without the combiners, each input record for the reducer would be as follows  

**'word'    'single node post containing the word'**  

With the combiner, the input record for the reducer would be as follows  

**'word'    'length of the following node list'    'list of nodes containing the word, as computed by a combiner' **  

Thus, with the combiner, the reducer receives lesser number of input records, i.e. lesser data is sent over the network to transfer records from the mapper to the reducer. The introduction of the combiner thus improves the network bandwidth performance and therefore makes the index building process much more efficient.

## Relevant files

### Input file

'forum_node.tsv' file is too big to be uploaded to GitHub. One can download this file from the Udacity course page.

### Mapper

##### word_inverted_index_mapper.py

### Reducer (and combiner)

##### word_inverted_index_combiner_reducer.py

### Output / Result files

Output file which contains the word inverted index is too large to be uploaded to GitHub. 

Instead, a zip file 'word_inverted_index_output_screenshots' has been pushed to this repository. It contains screenshots taken while running the index computation with and without combiners. Of particular interest are the screenshots that show the MapReduce Framework statistics on the jobTracker page.