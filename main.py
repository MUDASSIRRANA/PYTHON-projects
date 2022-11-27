import mysql.connector as mysql

db =mysql.connect(host="localhost",user="root",database="library1") # HERE THE PROGRAM IS BEING CONNECTED WITH DATABASE


command_hander= db.cursor(buffered=True)    # db.cursor IS USED TO IMPLIMENT CHANGES IN DATABASE

def reg_student():               # FUNCTION USED FOR REGISTRATION OF NEW COMING USERS

    print("Register New Student")

    name = input(str("Enter your name: "))

    reg_no = input("Enter your reg # ")

    phone_no = int(input("Enter your phone_no: "))

    email = input(str("Enter your your email: "))

    query_vals = (name,reg_no,phone_no,email)

    command_hander.execute("INSERT INTO user1 (name,reg_no,phone_no,email) VALUES (%s,%s,%s,%s)" ,query_vals)

    db.commit()       #THIS FUNCTION IS USED TO CONFIRM CHANGES MADE BY USER IN DATABASE

    print(name+ " has been registered as a library member.")


def enter_books():              # THIS FUNCTION IS USED TO ENTER NEW COMING BOOKS FOR REGISTARTION

    book_name = str(input("Enter the name of the book: "))

    book_code = int(input("Enter the Book code: "))

    book_subject = str(input("Enter the book subject: "))

    query_vals = (book_name,book_code,book_subject)

    command_hander.execute("INSERT INTO books (book_name,book_code,book_subject) VALUES (%s,%s,%s)" ,query_vals)

    db.commit() #THIS FUNCTION IS USED TO CONFIRM CHANGES MADE BY USER IN DATABASE

    print(book_name+ "has been entered in system.")

def list_of_student():

    command_hander.execute("SELECT reg_no FROM user1")

    list_ = command_hander.fetchall()

   

    return list_



def display_avaliable_books():

    print("Displaying the list of avaliable books:")

    command_hander.execute("SELECT book_name FROM books")

    records = command_hander.fetchall()

    #

    print(records)
    
    return records

def bookcodes():
    command_hander.execute("SELECT book_code FROM books")

    list_of_books=command_hander.fetchall()

    return(list_of_books)


    

def List_of_books():
    
    command_hander.execute("SELECT book_name FROM books")
    
    records = command_hander.fetchall()
    
    return (records)

def issue_books():

    name = str(input("Enter your name: "))

    reg_no =int(input("Enter your reg # "))

    regno= (reg_no,)

    a = list_of_student()



    if regno in a:

        book = str(input("Enter the name of the book you want to borrow: "))

        book_code = int(input("Enter the book code : "))

        bc = (book_code,)

        #print(B)
        f = bookcodes()
    
        if bc in f:

            print("You have been issued " +book+ ". Please keep it safe and return it within 30 days") 

            
        else: 

            print("Sorry, This book is not available . Please wait until the book is available.")
    else:
        
        print("Register yourself in library.")    


    
def return_book():

    return__book= input("Enter the name of the book you want to return: ")

   

    B = (return__book,)

    c = List_of_books()
    
    if B in c:
        
        print("Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!")

    else:
        print("Sorry this book doesn't belong to our library")

   

def main():
   
    while (True):

        print('''\n ====== Welcome to  Library ======
    1. Register in a library.
    2. List of all books.
    3. Want to add new book.
    4. Request a book.
    5. Return a book.
    6. Exist the library

    ''')

        choice=int(input("Enter your choice: "))
        if choice==1:
            reg_student()
        elif choice==2:
            
            display_avaliable_books()
        elif choice==3:
            enter_books()
        elif choice==4:
            issue_books()
        elif choice==5:
            return_book()
        elif choice>6:

            print("Invalid choice.")
        elif choice==6:
            print("Thanks for choosing our library. Have a great day ahead!")
            exit()
main()
