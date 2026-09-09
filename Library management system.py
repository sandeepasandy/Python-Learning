class Book:
    def __init__(self, bookname, ID, Title, Authorname,Status):
        self.bookname = bookname
        self.ID = ID
        self.Title = Title
        self.Authorname = Authorname
        self.Status = Status
    def display_info(self):
        print("\n-------Book details---------")
        print("bookname =", self.bookname)
        print("ID =", self.ID)
        print("Title =", self.Title)
        print("Authorname =", self.Authorname)
        print("Status =", self.Status)
        
book1= Book("Python", 100, "Python programming","Ram","Available")
book2= Book("java", 101, "java programming", "Ramesh","Available")
book3= Book("C ", 102, "C programming", "Prudhvi","Available")
book4= Book("Story", 211,"Arabian Nights", "Sandy","Available")
book5= Book("Horror", 456,"Ghost","Priya","Available")

books = [book1, book2, book3, book4, book5]
for book in books:
    book.display_info()

book=int(input("Enter Book ID to search:"))

found = False

for b in books:
    if b.ID == book:
        b.display_info()
        found = True
        
if found == False:
        print("Book not found")

delete_id = int(input("Enter Book ID to delete:"))
delete_found = False

for b in books:
    if b.ID == delete_id:
        books.remove(b)
        print("Deleted")
        delete_found = True
        
if delete_found == False:
    print("Book not found")

availability_id = int(input("Enter Book ID to check Availability:"))

availability_found = False

for b in books:
    if b.ID == availability_id:
        availability_found = True
    if b.status == "Available":
        print("Book is already issued")
    else:
        print("Book is already issued")

if availability_found == False:
    print("Book not found")

class Member:
    def __init__(self, member_id, member_name):
        self.member_id = member_id
        self.member_name = member_name
        self.issued_books=[]
    def display_info(self):
        print("\n---------Member Details-------")
        print("member_id =", self.member_id)
        print("member_name", self.member_name)
        print("Issued_books", [])

member1 = Member(1, "Prudhvi",)
member2 = Member(2, "Sandeepa")
member3 = Member(3, "Shalini")


members = [member1, member2, member3]
for member in members:
    member.display_info()

book = int(input("Enter a bookID to issue:"))

for b in books:
    if b.ID == book:
        b.display_info()
