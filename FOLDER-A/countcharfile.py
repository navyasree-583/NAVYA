# file = open("C:/Users/navyasree.lv/Desktop/FOLDER-A/demofile2.txt","r")
# data = file.read()
# print(data)
# number_of_characters = len(data)
# print('Number of characters in text file :', number_of_characters)

# Count excluding spaces
# file = open("C:/Users/navyasree.lv/Desktop/FOLDER-A/demofile2.txt","r")
# data = file.read().replace(" ","")
# print(data)
# number_of_characters = len(data)
# print('Number of characters in text file :', number_of_characters)

#count number of words in file

file = open("C:/Users/navyasree.lv/Desktop/FOLDER-A/demofile2.txt","r")
data = file.read()
words = data.split()
print(words)
number_of_words = len(words)
print('Number of words in text file :', number_of_words)
