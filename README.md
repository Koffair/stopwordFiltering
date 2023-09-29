# Stopword filtering
Filtering our stopwords from a given text.

+ Stopwords should be in plain text file, all lower-cased,
one word per line
+ Input files should be plain text files,
preprocessed be our tools. I.e. text cannot
contain any punctuation marks, and etc,
all words should be in lower case and
words should be separated by spaces

```bash
python main.py --input data/in --output data/out --stopfile data/hungarian_swear_words.txt
```