#If this exercise we will create a set of unique word from given documents
#It is very often utilized method of data pre-processing in natural language processing 

#Make sure you have installed following packages
#import nltk
#import collections 
#import string
#import re

# Download dataset - Movie Review Polarity Dataset (polarity dataset v2.0).
#Copy the contents of the downloaded archive to your working directory
#Take a look at the content (read a few reviews)


# Preapare a function to read a text from file

def load_doc(filename):
    # open the file as read only
    file = open(filename, 'r')
    # read all text
    text = file.read()
    # close the file
    file.close()
    return text

# Try it
test1 = load_doc('txt_sentoken/neg/cv000_29416.txt')
print(test1)

# Preapare a function to read all files from directory

# listdir is a command that returns a list containing the names of the files in the directory
from os import listdir

def process_docs(directory):
    # for all files in the folder
    for filename in listdir(directory):
        # skip files that do not have the right extension
        if not filename.endswith(".txt"):
            next
        # create the full path of the file to open
        path = directory + '/' + filename
        # load document
        doc = load_doc(path)
        print('Loaded %s' % filename)

# Try to load all negative reviews
directory = 'txt_sentoken/neg'
process_docs(directory)

# Try to load all positive reviews
directory = 'txt_sentoken/neg'
process_docs(directory)

# Now we want to create tokens. Each word is a separable position in a table
# We will use white space
tokens = test1.split()
print(tokens)

# As you can see there are a lot of unwanted positions, like punctuation marks ('.', '?',...)
# stopwords ('a', 'the', ...), numbers ('7/10', '10/10',...)

# To clear it we will use nltk package

# Mayby you will have to download stopwords file manually. You can do that by the following commands
# As you do that once, you don't have to repeat that in next scripts 
import nltk
nltk.download('stopwords')

# "NLTK is a leading platform for building Python programs to work with human language data"
# More about nltk you can find in http://www.nltk.org/book/

# Take a look at available text datasets http://www.nltk.org/nltk_data/


# As a stopwords we will use a set of words established in a  nltk package
from nltk.corpus import stopwords
print(stopwords.words('english'))

# Moreover we use string package which make easier strings manipulations
import string
# and re package which allow to use regular expression
import re

# Define a function to clear unwanted 'words' from text
def clean_doc(doc):
    # split into tokens by white space
    tokens = doc.split()
    # prepare regex for char filtering
    re_punc = re.compile('[%s]' % re.escape(string.punctuation))
    # remove punctuation from each word
    tokens = [re_punc.sub('', w) for w in tokens]
    # remove remaining tokens that are not alphabetic
    tokens = [word for word in tokens if word.isalpha()]
    # filter out stop words
    stop_words = set(stopwords.words('english'))
    tokens = [w for w in tokens if not w in stop_words]
    # filter out short tokens
    tokens = [word for word in tokens if len(word) > 1]
    return tokens

# Now let us try it 
tokens = clean_doc(test1)
print(tokens)

# Counter is dict subclass for counting hashable objects (in this case words)
from collections import Counter
#We use it to create a set of words and the number of their occurrence
vocab = Counter()

#We will create a function to add words from file to vocab

def add_doc_to_vocab(filename, vocab):
    # load doc
    doc = load_doc(filename)
    # clean doc
    tokens = clean_doc(doc)
    # update counts
    vocab.update(tokens)

#and a function adding all word from all files in a given folder

def process_docs(directory, vocab):
    # walk through all files in the folder
    for filename in listdir(directory):
    # skip files that do not have the right extension
        if not filename.endswith(".txt"):
            next
        # create the full path of the file to open
        path = directory + '/' + filename
        # add doc to vocab
        add_doc_to_vocab(path, vocab)

# add all words from negative reviews to vocab
process_docs('txt_sentoken/neg', vocab)
# add all words from positive reviews to vocab
process_docs('txt_sentoken/pos', vocab)
# print the size of the vocab
print(len(vocab))
print(vocab.most_common(50))

# Take a look at the most rare words. 
min_occurane = 5

rare = [[k,c] for k,c in vocab.items() if c < min_occurane]
print(rare)
len(rare)
# Many of them do not have any meaning and we prefer to reject them

# Now we want to have only the words that occurred more than 5 times

tokens = [k for k,c in vocab.items() if c >= min_occurane]
print(len(tokens))

# Define the function to save tokens to a file (each token in a new line)
def save_list(lines, filename):
    data = '\n'.join(lines)
    file = open(filename, 'w')
    file.write(data)
    file.close()

#Save tokens to 'vocab.txt'
save_list(tokens, 'vocab.txt')

