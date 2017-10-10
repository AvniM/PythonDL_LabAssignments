# ---------------------------------------------------------------------
#   Lab Assignment 3 - Task 4
#   Summarize a text file using Natural Language Processing
#   Avni Mehta, Class Id: 15
# ---------------------------------------------------------------------

# Importing Libraries
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
import textwrap
import operator


# Read the file
def read_data(filename):
    input_file = file(filename).read()
    print "\n1. Reading the file.."
    print "---------------------\n"
    print textwrap.fill(input_file, 180)   # to word wrap in the console
    return input_file


# Apply Lemmatization
def lemmatization(words):
    lemmatizer = WordNetLemmatizer()
    print "\n\n2. Applying Lemmatization.."
    print "---------------------------\n"

    for w in words:
        lemm = lemmatizer.lemmatize(w)
        print " Word = " + w.ljust(20) + "|  Lemmatization = " + lemm.ljust(20)  # for left justification
    return


# Apply POS, remove the verbs
def pos_remove_verbs(inputfile):
    tokenized_words = word_tokenize(inputfile)
    pos_words = pos_tag(tokenized_words)

    print "\n\n3. Using POS, removing verbs.."
    print "-----------------------------"

    print "\nPOS on the input file:"
    print textwrap.fill(str(pos_words), 180)

    noverbs = []     # to store non-verbs from input file
    verbs = []       # to store verbs from input file
    for x in pos_words:
        if x[0] not in [',','.','(', ')']:   # removing noise of special characters
            # tag for verbs are 'VB', 'VBZ', 'VBD' etc..
            # if tag does not contain substring 'VB" - add to noverbs list
            if x[1].find('VB') == -1:
                noverbs.append(x[0])
            else:
                verbs.append(x[0])

    print "\nNon verbs :"
    print textwrap.fill(", ".join(noverbs), 180)
    print "\nVerbs :"
    print textwrap.fill(", ".join(verbs), 180)

    return noverbs


# Word frequency of remaining words
def word_frequency(wordslist):
    frequency = {}    # dictionary for word count (key = word, value = count)
    for w in wordslist:
        # removing the noise in the words like , . ( ) etc..
        w = w.replace(',', '').replace('.', '').replace('(', '').replace(')', '').replace('\n', '')
        if w != '':
            if w in frequency:
                frequency[w] += 1
            else:
                frequency[w] = 1

    # sorting the dictionary and storing as list of tuples
    sorted_frequency = sorted(frequency.items(), key=operator.itemgetter(1), reverse=True)

    # printing the wordcount dictionary
    print "\n\n4. Word frequency of non-verbs.."
    print "--------------------------------\n"

    for i in sorted_frequency:
        print " Word = " + i[0].ljust(20) + "|  Count = " + str(i[1]).ljust(20)  # for left justification

    return sorted_frequency


# Top 5 words
def most_common(mylist, n):
    common_words = []
    for i in range(len(mylist)):
        if i < n:
            common_words.append(mylist[i][0])
        else:
            break

    print "\n\n5. Most common 5 words.."
    print "------------------------\n"
    print ", ".join(common_words)

    return common_words


# Sentences with most repeated words
def summarize_text(inputfile, commonlist):
    # Tokenizing sentences from input file
    sentences = sent_tokenize(inputfile)

    # Searching sentences with most common words
    sent_having_common = []
    for s in sentences:
        if any(x in word_tokenize(s) for x in commonlist):
            sent_having_common.append(s)

    print "\n\n6. Summarizing the file (sentences with most common words)"
    print "----------------------------------------------------------\n"
    # Concatenating sentences with common-words to make summary
    summary = ""
    summary += " ".join(sent_having_common)
    print textwrap.fill(summary, 180)
    return

# -------------
# Main Activity
# -------------

# Step 1: Read the file
filedata = read_data('input.txt').lower()

# Step 2: Perform lemmatization
wordlist = filedata.split()
lemmatization(wordlist)

# Step 3: Using POS, remove verbs
wordlist_noverbs = pos_remove_verbs(filedata)

# Step 4: Word Frequency of remaining words
word_freq = word_frequency(wordlist_noverbs)

# Step 5: Top 5 most repeated words
top5 = most_common(word_freq, 5)

# Step 6: Sentences with most repeated words
summarize_text(filedata, top5)