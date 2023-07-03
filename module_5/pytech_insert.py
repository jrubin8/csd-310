
from pymongo import MongoClient
#required modules
url = "mongodb+srv://admin:admin@cluster0.guokdam.mongodb.net/"
#MongoDB Connection URL
client = MongoClient(url)

db = client.pytech

usain = {
    "student_id": "1007",
    "first_name": "Usain",
    "last_name": "Bolt",
    "enrollments": [
        {
            "term": "Summer",
            "gpa": "3.0",
            "start_date": "June 3, 2023",
            "end_date": "August 19, 2023",
            "courses": [
                {
                    "course_id": "CYBR310",
                    "description": "Network Defense",
                    "instructor": "C Johnson",
                    "grade": "A"
                },
                {
                    "course_id": "CYBR420",
                    "description": "Penetration Testing",
                    "instructor": "J Hermann",
                    "grade": "C"
                },
                {   "course_id": "MA101",
                    "description": "Intro to Algebra",
                    "instructor": "B James",
                    "grade": "B"
                }
            ]
        }
    ]

}
 #usain bolt student entry
jesse = {
    "student_id": "1008",
    "first_name": "Jesse",
    "last_name": "Owens",
    "enrollments": [
        {
            "term": "Summer",
            "gpa": "4.0",
            "start_date": "June 3, 2023",
            "end_date": "August 19, 2023",
            "courses": [
                {
                    "course_id": "CYBR310",
                    "description": "Network Defense",
                    "instructor": "C Johnson",
                    "grade": "A"
                },
                {
                    "course_id": "CYBR420",
                    "description": "Penetration Testing",
                    "instructor": "J Hermann",
                    "grade": "A"
                },
                {   "course_id": "MA101",
                    "description": "Intro to Algebra",
                    "instructor": "B James",
                    "grade": "A"
                }
                
            ]
        }
    ]
}
#jesse owens student entry
fred = {
    "student_id": "1009",
    "first_name": "Fred",
    "last_name": "Kerley",
    "enrollments": [
        {
            "term": "Summer",
            "gpa": "2.0",
            "start_date": "June 3, 2023",
            "end_date": "August 19, 2023",
            "courses": [
                {
                    "course_id": "CYBR310",
                    "description": "Network Defense",
                    "instructor": "C Johnson",
                    "grade": "C"
                },
                {
                    "course_id": "CYBR420",
                    "description": "Penetration Testing",
                    "instructor": "J Hermann",
                    "grade": "C"
                },
                {   "course_id": "MA101",
                    "description": "Intro to Algebra",
                    "instructor": "B James",
                    "grade": "C"
                }
            ]
        }
    ]
}
 #fred kerley student entry
students = db.students
 
print("\n  -- INSERT STATEMENTS --")
usain_student_id = students.insert_one(usain).inserted_id
print("\n Student record for Usain Bolt inserted into the students collection with document_id " + str(usain_student_id))
#printing message for creation of Usain record
jesse_student_id = students.insert_one(jesse).inserted_id
print("\n Student record for Jesse Owens inserted into the students collection with document_id " + str(jesse_student_id))
#printing message for creation of Jesse record
fred_student_id = students.insert_one(fred).inserted_id
print("\n Student record for Fred Kerley inserted into the students collection with document_id " + str(fred_student_id))
#printing message for creation of Fred record
input("\n\n\n Please press the enter key to finish the program.")
#input closes/ends the application.
#please note, it was difficult to achieve the required functions and format the output the same as the provided example without making this code extremely similar to the example provided in the course repository.
