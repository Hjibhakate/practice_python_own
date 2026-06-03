#Exercise : Write and read a file 

with open("example.txt","w") as f:
    f.write("Hello Python \nLearning is fun!")

with open("example.txt","r") as f:
    content = f.read()
    print(content)