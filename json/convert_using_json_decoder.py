"""
Demonstrates how to convert Python object to JSON and vice versa using JSONDecoder

Created: 2023-09-20
"""

import json

class Student(object):
    def __init__(self, rollNumber, name, marks):
        self.rollNumber = rollNumber
        self.name = name
        self.marks = marks

def studentDecoder(obj):
    if '__type__' in obj and obj['__type__'] == 'Student':
        return Student(obj['rollNumber'], obj['name'], obj['marks'])
    return obj

studentObj = json.loads('{"__type__": "Student", "rollNumber":1, "name": "Ault kelly", "marks": 78}',
           object_hook=studentDecoder)

print("Type of decoded object from JSON Data")
print(type(studentObj))
print("Student Details")
print(studentObj.rollNumber, studentObj.name, studentObj.marks)