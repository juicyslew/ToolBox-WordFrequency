""" Analyzes the word frequencies in a book downloaded from
Project Gutenberg """

import string
from collections import Counter
import operator

def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """
    f = open(file_name, 'r') #Open file
    lines = f.readlines() #read lines from file
    curr_line = 0 # start line iterator
    while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1: #while not find the line 'START OF THIS PROJECT GUTENBERG EBOOK'
      curr_line += 1 #add to iterator
    lines = lines[curr_line+1:] #return lines after the start of ebook
    joined_lines = "\n".join(lines) #put back together lines into string
    joined_lines.replace(string.punctuation, "").lower() #replace punctuation and make all lowercase
    return joined_lines.split() #split text into list


def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequently occurring
    """
    c = Counter(word_list) #get dictionary counting frequency of words
    word_sort = sorted(c.items(), key=operator.itemgetter(1), reverse=True) #sort dictionary into list of decreasing frequency
    return word_sort[:n] #return the values up to the nth word.

if __name__ == "__main__":
    w_list = get_word_list('pg32325.txt') # get word list from Gutenberg text
    print(get_top_n_words(w_list, 100)) #print the 100 most common words.
