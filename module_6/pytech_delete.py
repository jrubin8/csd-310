#to insert and delete from pytech
from pymongo import MongoClient
#required modules

url = "mongodb+srv://admin:admin@cluster0.guokdam.mongodb.net/"
#MongoDB connection URL^
 
client = MongoClient(url)
#connecting to the MongoDB cluster

db = client.pytech
#connecting pytech
 
students = db.students
#students collection
 
student_list = students.find({})
#finding students via find()
 
print("\nDisplaying results from the requested find() query:")
#a display message to users^

for doc in student_list:
    print("\nStudent ID: " + doc["student_id"] + "\nFirst Name: " + doc["first_name"] + "\nLast Name: " + doc["last_name"] + "\n")
#looping over the collection^

test_doc ={
    "student_id": "1010",
    "first_name": "Yoshihide",
    "last_name": "Kiryu"
}
#test doc
 
test_doc_id = students.insert_one(test_doc).inserted_id
#inserting the doc

print("\nA statement regarding requested insertion: ")
print("\nThe request was processed, and a new record was added to the students collection with document_id " + str(test_doc_id))
#a message to users regarding the test doc

student_test_doc = students.find_one({"student_id": "1010"})
#find_one for the new student to be added
 
print("\nThe added (test) record, which will now be deleted, is as follows: ")
print("\nStudent ID: " + student_test_doc["student_id"] + "\nFirst Name: " + student_test_doc["first_name"] + "\nLast Name: " + student_test_doc["last_name"] + "\n")
#displaying the test doc

deleted_student_test_doc = students.delete_one({"student_id": "1010"})
#delete_one to delete test doc
new_student_list = students.find({})
#finding students^

 
print("\nDisplaying requested document(s) from find() query, showing the test was removed: ")
#a message to users
 
for doc in new_student_list:
    print("\nStudent ID: " + doc["student_id"] + "\nFirst Name: " + doc["first_name"] + "\nLast Name: " + doc["last_name"] + "\n")
#looping over the collection
 
input("\nThe test student has been added and deleted. \n\nYou are in control. \n\nPlease press the enter key to conclude the program.")
#the program is over.
