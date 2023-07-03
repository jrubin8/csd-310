
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.guokdam.mongodb.net/"

client = MongoClient(url)

db = client.pytech
 
students = db.students
 
student_list = students.find({})
 
print("\n  - Displaying requested document from find() query -")
 
for doc in student_list:
    print("Student ID: " + doc["student_id"] + "\nFirst Name: " + doc["first_name"] + "\nLast Name: " + doc["last_name"] + "\n")


usain = students.find_one({"student_id": "1007"})
jesse = students.find_one({"student_id": "1008"})
fred = students.find_one({"student_id": "1009"})
 
print("\n  - Displaying requested document from find_one() query -")
print("Student ID: " + usain["student_id"] + "\nFirst Name: " + usain["first_name"] + "\nLast Name: " + usain["last_name"] + "\n")
 
input("\n\n Please press the enter key to finish the program.")
