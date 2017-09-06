# Calculate word frequency for each word in a given file


# Return wordcount for the given word.
# If word not present in the list, return 0
def get_word_count(w):
    for i in myList:
        if i[0] == w:
            cnt = int(i[1])
            return cnt
    return 0


# Split the file line by line and extracts each word
# Add each word to a list along with the wordcount (nested list)
# If word already present in the list, replace with new wordcount (remove+insert)
# lower() makes the program case insensitive
# Special characters from the word are replaced to clean the word: ( ) , .
def add_to_list():
    line = infile.readline().lower()

    while line != '':
        for word in line.split(' '):
            word = word.replace(',', '').replace('.', '').replace('(', '').replace(')', '').replace('\n', '')

            if word != '-' and word != '' and word != '\n':
                count = get_word_count(word)

                if count == 0:
                    myList.append([word, 1])
                else:
                    indx = myList.index([word, count])
                    myList.remove([word, count])
                    myList.insert(indx, [word, count + 1])

        line = infile.readline().lower()


# Write the list containing word and wordcount to output file
# The word frequency is added to the file in two formats : list and sorted list
def write_to_file():
    outfile = open(outputFileName, 'w+')
    outfile.truncate()

    # As nested list format
    outfile.write('List of words with their wordcount in ' + inputFileName + ':\n\n')
    outfile.write(str(myList))

    # As Sorted list
    outfile.write('\n\nSorted list of words with their wordcount in ' + inputFileName + ':\n\n')
    # key=lambda x: x[1] is to sort by 2nd element(count)
    # reverse=True sorts in desc order
    myList.sort(key=lambda x: x[1], reverse=True)

    for i in range(len(myList)):
        outfile.write(myList[i][0] + ' : ' + str(myList[i][1]) + '\n')

    print('\nWord frequency of each word in '+ inputFileName + ' can be found in ' + outputFileName)

# main
print('\n*** Calculate word frequency of all the words in a file ***')

inputFileName = input('\nEnter file name : ')
infile = open(inputFileName, 'r')

outputFileName = 'OutputFile01.txt'
myList = []

add_to_list()
write_to_file()