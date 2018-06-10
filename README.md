# Text_summarization

## Types of Extraction-based Methods

### 1) Statistical Method : 
Text summarization based on this approach relies on the 
statistical distribution of certain features and it is done
without understanding whole document. Models rank the sentences
of the original text to appear in the summary in the order of impor-
tance. We are using average TF-ISF, title Word, sentence length, sen-
tence feature, thematic word and numerical data as statistical features
in our proposal.

### 2) Linguistic Method: 
In this, method needs to be aware of and knowdeeply the 
linguistic knowledge, so that the computer will be able to
analyse the sentences and then decide which sentence to be selected.
We are using proper noun feature and sentence to sentence similarity
as linguistic features in our proposal.

### 3) Hybrid Method: 
It is the combination of statical and Linguistic methods.
It optimizes best of both the previous methods for meaningful and
short summary.

## Model Overview Steps

1. Read Input text file.

2. Preprocess the file. (Processing step)
  I Sentence Segmentation.
  II Tokenisation of each sentence to words.
  III StopWords Removal.
  IV Stemming of Words.

3. Processing Step (feature extraction + sentence ranking)
  I Extract following features from “O” file
  
    i.  Average TF-ISF
        <code>AvgT FISF(S t ) = ∑ T F ∗ ISF</code>
  
    ii. Sentence Length
    
    iii.Sentence Position
    
    iv. Sentence Similarity
    
    v. Numerical Data
  II Sentence Ranking to rank sentences in range of “0 to 1” with 1 in-
  dicating most important and 0 indicating not important sentence
  based on the each feature’s normalised scores.

4. Generate Summary (Extraction Step)
  I While (Sentences in Summary file “S” does not exceed maximum
  limit as per given by compression ratio) extract all sentences from
  “S” sort by sentence rank of Maximum rank (rank5) to minimum
  (rank1).

5. Display Output Summary “S”

