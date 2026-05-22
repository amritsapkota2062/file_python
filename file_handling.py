'''
reading files
'''

# f = open("file.txt", 'r') # -> If we open by this method we should close it
# value = f.read()
# print(value)
# f.close()

# file_path = "file.txt" #-> Automatically closes the file 
# with open (file_path, 'r') as file:
#     content = file.read()
#     output = "Hi" + content[5:43] + " " + "tested" + "\n" + "Bad Luck!"

#     print(output)


'''
readline() and readlines()
'''

# with open("file.txt", 'r') as file:
#     row = file.readlines()
#     # row = file.readline()
#     # for x in file:
#         # print(x, end="")

#     new_row = [i.strip("\n") for i in row]
#     print(new_row)



'''
WRITING
'''
import csv
# with open('writing_file.txt', "w") as f:
#     lines = f.write(output)
#     print(lines)

# import csv

# with open("data.csv", "r") as f:
#     csv_reader = csv.reader("data.csv")
#     header = next(csv_reader)
#     print(header)
#     # for row in csv_reader:
#     #     print(row)

with open("details.csv", "r") as f:
    data = csv.reader(f)
    for row in data:
        print(row["age"])