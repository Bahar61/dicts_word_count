# put your code here.
file_to_count = open('test.txt')

def word_count(file_to_count):
    """take a file and return each word count"""
    final_count = {}

    for line in file_to_count:
        line = line.rstrip() 
        words_splited = line.split(' ')

        for word in words_splited:
            final_count[word] = final_count.get(word, 0) + 1
        
    return final_count

print(word_count(file_to_count))
