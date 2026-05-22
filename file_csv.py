import csv

# with open ("data.csv", "r") as file:
#     csv_reader = csv.reader(file)
#     # header = next(csv_reader)
 
#     for row in csv_reader:
#         print(row[1])


# with open("output.csv", 'w', newline= "") as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerow(["Name", "Age", "City"])

#     no_of_data = int(input("How many data do you want to write: "))
#     while no_of_data != 0:
#         data = []
#         name = input("Enter your name: ")
#         age = input("Enter your age: ")
#         city = input("Enter your city: ")
#         data.append(name)
#         data.append(age)
#         data.append(city)
#         csv_writer.writerow(data)
#         no_of_data -= 1

#     print(csv_writer)


# with open("data.csv", "w", ) as file:
#     csv_reader = csv.DictReader(file)
#     for row in csv_reader:
#         print(row)


import csv

# def roll_checker(roll, details):

#     while True:
#         found = False

#         with open("details.csv", "r") as f:
#             data = csv.reader(f)

#             for row in data:
#                 if row[3] == str(roll):
#                     found = True
#                     break

#         if found == False:
#             details.append(roll)
#             return

#         roll = int(input("Enter a unique roll number: "))


# def marks_checker(marks, details):

#     while True:
#         if marks >= 0 and marks <= 100:
#             details.append(marks)
#             return

#         marks = int(input("Enter a valid marks: "))


# with open("details.csv", "a", newline="") as f:
#     csv_writer = csv.writer(f)

#     if f.tell() == 0:
#         csv_writer.writerow([
#             "name", "age", "address", "rollno",
#             "science", "maths", "english",
#             "totalmarksobtained", "percentage", "status"
#         ])

#     no_of_details = int(input("How many students details do you want to add? "))

#     while no_of_details > 0:

#         details = []

#         name = input("Enter your name: ")
#         details.append(name)

#         age = int(input("Enter your age: "))
#         details.append(age)

#         address = input("Enter your address: ")
#         details.append(address)

#         rollno = int(input("Enter your roll number: "))
#         roll_checker(rollno, details)

#         science_marks = int(input("Enter your marks in science: "))
#         marks_checker(science_marks, details)

#         maths_marks = int(input("Enter your marks in mathematics: "))
#         marks_checker(maths_marks, details)

#         english_marks = int(input("Enter your marks in English: "))
#         marks_checker(english_marks, details)

#         totalmarksobtained = science_marks + maths_marks + english_marks
#         details.append(totalmarksobtained)

#         percent = f"{(totalmarksobtained / 300) * 100:.2f}%"
#         details.append(percent)

#         if science_marks >= 40 and maths_marks >= 40 and english_marks >= 40:
#             status = "Pass"

#         else:
#             status = "Fail"

#         details.append(status)

#         csv_writer.writerow(details)
#         f.flush()

#         no_of_details -= 1

task = int(input("Enter a roll no and I will give you every details of that person: "))
with open("details.csv", "r") as f:
    data = f.read()
    for row in data:
        if row[1] == str(task):
            print(row[1])