# put your code here.
import string 

def count_words(file_name):
    """Count words inside file and prints words

        Return dictionary of the words without punctuation and counts"""

    input_file = open(file_name)

    #create a list of punctuation
    exclude = string.punctuation 

    #Create dict
    words = {}
    #iterate + + rstrip () + split by spaces
    for line in input_file:
        line = line.rstrip()
        line = line.lower()
        words_line = line.split()
        words_line = words_line
    #count each word
        for word in words_line:
            word = word.rstrip(exclude)
            word = word.lstrip(exclude)
    # if in dic, increase by 1
            if word in words:
                words[word] += 1
    # if not, init
            else:
                words[word] = 1

    print "Words in", file_name
    for key, value in words.iteritems():
        print key, value

    return words


# count_words("test.txt")
count_words("twain.txt")
