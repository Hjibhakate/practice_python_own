#Append new lines to the file 
with open("notes.txt","a") as f:
    f.write("\n Python is easy to learn . ")
    f.write("\n File handling is important . ")

#Read the file and count words 
with open("notes.txt","r")as f:
    content = f.read()

word_count = len(content.split())

print("Total words in file: ", word_count)