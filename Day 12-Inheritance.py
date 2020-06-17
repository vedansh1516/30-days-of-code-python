#Task
#Given two classes, Person and Student, where Person is the base class and Student is the derived class. 
#Student inherits all the properties of Person.
class Student(Person):
    def __init__(self, firstName, lastName, idNumber,scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    def calculate(self):
        l= len(scores)
        s=sum(scores)
        avg=s/l
        if (avg>=90 and avg<=100):
            return "O"
        elif (avg>=80 and avg<90):
            return "E"
        elif (avg>=70 and avg<80):
            return "A"
        elif (avg>=55 and avg<70):
            return "P"
        elif (avg>=40 and avg<55):
            return "D"
        elif ( avg<40):
            return "T" 
