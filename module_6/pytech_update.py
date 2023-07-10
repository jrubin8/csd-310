#to update pytech
from pymongo import MongoClient
#required modules^

url = "mongodb+srv://admin:admin@cluster0.guokdam.mongodb.net/"
#MongoDB connection URL^

client = MongoClient(url)
#MongoDB cluster connection^

db = client.pytech
#pytech database^

students = db.students
#the students collection^
 
student_list = students.find({})
#the list of students is found using the find() query^
 
print("\n  - Displaying requested document from find() query -")
#a message communicating to the user^
 
for doc in student_list:
    print("Student ID: " + doc["student_id"] + "\nFirst Name: " + doc["first_name"] + "\nLast Name: " + doc["last_name"] + "\n")
#searching for entries that are found in the student list
    
update_result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Boltington"}})
#updating student 1007^

usain = students.find_one({"student_id": "1007"})
jesse = students.find_one({"student_id": "1008"})
fred = students.find_one({"student_id": "1009"})
#to find the updated student (in this instance we will just be finding "usain")

print("\n  - Displaying Student 1007 Document -")
#a message commmunicating to the user^

print("Student ID: " + usain["student_id"] + "\nFirst Name: " + usain["first_name"] + "\nLast Name: " + usain["last_name"] + "\n")
#printing the updated entry^

input("\n\n Please press the enter key to finish the program.")
#entry of a key concludes/terminates the program.

