marks = {
"Math": 85,
"Science":90,
"English":78
    }

#Add a new subject 

marks["History"] = 92

#Loop through all  subject and print marks 

for subject,mark in marks.items():
    print(subject,":",mark)