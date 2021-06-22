class Libary:
    def __init__(self,listofbook):
        self.book = listofbook


    def displaylistofBook(self):
        print(" Books available are ")
        for books in self.book:
            print(" --" +books)
            

    def borrowabook(self,bookname):
        if bookname in self.book:
            print(f"You have issued this book {bookname}. Please keep this book safe and return the book in 30 days")
            self.book.remove(bookname)
            return True
        else:
            print("Sorry this book in not availabe or the book is issued to someone eles. Pleases apply after some days")
            return False

    def returnabook(self,bookname):
        self.book.append(bookname)
        print("Thanks for returning the book on time. Hope you have learn something great......!")


class Student:

    def requestabook(self):
        self.book = input("Enter a book name to make a request:")
        return self.book

    def returnabook(self):
        self.book = input("Enter a book name to return:")
        return self.book



if __name__=="__main__":
    studentlibary =Libary(["Web Development", "Django", "Python", "Java","Pandas"])
    student = Student()

while True:
    welcome = '''====== WELCOME IN STUDENT LIBRARY OF OXFORD TOKIYO ======

    1.LIST OF ALL BOOK 
    2.REQUEST A BOOK
    3.ADD OR RETURN A BOOK
    4.EXIT

    '''
    print(welcome)
    user = int(input("Enter your choice: "))
    if user == 1:
        print(studentlibary.displaylistofBook())
    elif user == 2:
        print(studentlibary.borrowabook(student.requestabook()))
    elif user == 3:
        print(studentlibary.returnabook(student.returnabook()))
    elif user == 4:
        print("Thanks for chosing Student libary. Have a nice day ahead...!")
        exit()