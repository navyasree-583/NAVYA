div={'1':'hi','2':'hello','3':'how are you?','4':'I am fine'}
# print(div.items())

# This is the general template you can follow for dictionary comprehension in Python:

# dict_variable = {key:value for (key,value) in dictonary.items()}

print({key :value for (key,value) in div.items()})
