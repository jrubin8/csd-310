
from pymongo import MongoClient
#required modules
url = "mongodb+srv://admin:admin@cluster0.guokdam.mongodb.net/"
#MongoDB connection URL
client = MongoClient(url)

db = client.pytech
 
students = db.students
 
student_list = students.find({})
 
print("\n  - Displaying requested document from find() query -")
 
for doc in student_list:
    print("Student ID: " + doc["student_id"] + "\nFirst Name: " + doc["first_name"] + "\nLast Name: " + doc["last_name"] + "\n")
#searching for entries that are found in the student list

usain = students.find_one({"student_id": "1007"})
jesse = students.find_one({"student_id": "1008"})
fred = students.find_one({"student_id": "1009"})
#to find each student_id by query
print("\n  - Displaying requested document from find_one() query -")
print("Student ID: " + usain["student_id"] + "\nFirst Name: " + usain["first_name"] + "\nLast Name: " + usain["last_name"] + "\n")
#the usain entry is returned in this instance, as a part of the requirements
input("\n\n Please press the enter key to finish the program.")
#entry of a key concludes/terminates the program.
#please note, it was difficult to achieve the required functions and format the output the same as the provided example without making this code extremely similar to the example provided in the course repository.
