# put your code here.

def count_words(file_name):
    """Count words inside file and prints words

        Return dictionary of the words and counts"""

    input_file = open(file_name)

    #Create dict
    words = {}
    #iterate + + rstrip () + split by spaces
    for line in input_file:
        line = line.rstrip()
        words_line = line.split()
    #count each word
        for word in words_line:
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


count_words("test.txt")
#count_words("twain.txt")
