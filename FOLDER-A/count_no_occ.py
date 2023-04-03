with open("C:/Users/navyasree.lv/Desktop/FOLDER-A/demofile2.txt","r") as file: 
     data= file.read()
     no_of_occ = data.count("line")
     print(f'Number of occurrences of the word line is:', no_of_occ)