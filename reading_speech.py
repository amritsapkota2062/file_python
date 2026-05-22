no_of_words = 0
no_of_lines = 0

with open("details.csv", "r") as f:
    speech = f.readlines()
    
    for i in speech:
        no_of_lines += 1

        for j in i:
            while " " not in j:
                no_of_words += 1

print(no_of_words)
print(no_of_lines)