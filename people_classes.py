class Person:
    def __init__(self, name, egn, date_of_birth):
        self.name = name
        self.egn = egn
        self.date_of_birth = date_of_birth

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"EGN: {self.egn}")
        print(f"Date of birth: {self.date_of_birth}")

class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")
        print(f"Genre: {self.genre}")

class Student:
    def __init__ (self, class_number, name, average_grade):
        self.class_number = class_number
        self.name = name
        self.average_grade = average_grade

    def display_info(self):
        print(f"Class number: {self.class_number}")
        print(f"Name: {self.name}")
        print(f"Average Grade: {self.average_grade}")
        

Person1 = Person("John Pork", "9876543210", "1978-03-14")
Person2 = Person("Jaquavius Pork", "9876543211", "1982-11-09")
Person3 = Person("Marvin Beak", "9876543212", "1995-07-22")
Person4 = Person("Xiang Pork", "9876543213", "2001-01-17")
Person5 = Person("Pietro Pork", "9876543214", "1968-05-03")

Book1 = Book("Mein  Kamph", "Adolf Hitler", 1925, "Autobiography")
Book2 = Book("The Communist Manifesto", "Karl Marx & Friedrich Engels", 1848, "Political Theory")
Book3 = Book("The Prince", "Niccolò Machiavelli", 1532, "Political Philosophy")
Book4 = Book("The Origin of Species", "Charles Darwin", 1859, "Scientific Theory")
Book5 = Book("The Republic", "Plato", "380 BC", "Philosophy")

Student1 = Student("22411", "John Pork", 5.9)
Student2 = Student("22413", "Jaquavius Pork", 3.8)
Student3 = Student("22410", "Marvin Beak", 4.2)
Student4 = Student("22223", "Xiang Pork", 3.9)
Student5 = Student("22207", "Pietro Pork", 4.7)

# PEOPLES
print("\nPeople Information:")
Person1.display_info()
Person2.display_info()
Person3.display_info()
Person4.display_info()
Person5.display_info()

# BOOKS
print("\nBooks Information:")
Book1.display_info()
Book2.display_info()
Book3.display_info()
Book4.display_info()
Book5.display_info()

# STUDENTS
print("\nStudents Information:")
Student1.display_info()
Student2.display_info()
Student3.display_info()
Student4.display_info()
Student5.display_info()

