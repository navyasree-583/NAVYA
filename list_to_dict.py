def dictionary():
    # Declare hash function
    key_value = {}
 
# Initializing value
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323
 
    print("Task 1:-\n")
 
    print("key_value", key_value)
 
    # iterkeys() returns an iterator over the
    # dictionary’s keys.
    for i in sorted(key_value.keys()):
        print(i, end=" ")
    print("\n")
    for i in sorted(key_value.values()):
        print(i, end=" ")
    
dictionary()
 
