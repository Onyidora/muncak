# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}



def read_file_content(filename):
    open_file = open("./story.txt","r")
    file = open_file.read()
    open_file.close()
    return file

print(read_file_content("./story.txt"))


def count_words():
    text = read_file_content("./story.txt")
    text = text.strip()
    splited_text = text.split()
    word_count = {}
    for word in splited_text:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

    