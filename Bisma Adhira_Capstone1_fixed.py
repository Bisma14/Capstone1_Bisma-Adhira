from datetime import datetime, timedelta
from tabulate import tabulate
import maskpass

# Books dummy data
books_data = [
    {"book_ID":1,"book_title":"Statistic Inferential", "genre":"Education","publication_year":2021,"author":"Julian Alvarez","stock": 1,"fine_per_day":3},
    {"book_ID":2,"book_title":"4 Sehat 5 Presiden", "genre":"Education","publication_year":2021,"author":"Julian Samosir","stock": 10,"fine_per_day":3},
    {"book_ID":3,"book_title":"Indonesia Maju", "genre":"fiction","publication_year":2021,"author":"Satria Yuda","stock": 10,"fine_per_day":3},
    {"book_ID":4,"book_title":"Garuda in My Chest", "genre":"Education","publication_year":2021,"author":"Johny Sins","stock": 10,"fine_per_day":3},
    {"book_ID":5,"book_title":"Bisma Adhira : The Legend of Fire", "genre":"Education","publication_year":2021,"author":"Evan Dimas Darmono","stock": 10,"fine_per_day":3},
    {"book_ID":6,"book_title":"My SQL Introduction", "genre":"Education","publication_year":2021,"author":"Yanto Alvarez","stock": 10,"fine_per_day":3},
    {"book_ID":7,"book_title":"Bitcoin vs Altcoin", "genre":"Education","publication_year":2021,"author":"Chairul Robert Tanjung","stock": 10,"fine_per_day":3},
    {"book_ID":8,"book_title":"5 Cara Sukses Menjadi Biliuner by Handoko", "genre":"economy","publication_year":2021,"author":"Solikin Robert","stock": 10,"fine_per_day":3},
    {"book_ID":9,"book_title":"5 km", "genre":"Education","publication_year":2021,"author":"Sandy Walsh","stock": 10,"fine_per_day":3},
    {"book_ID":10,"book_title":"Marmud Merah Maroon", "genre":"Education","publication_year":2021,"author":"Julian Alvarez","stock": 10,"fine_per_day":3}
]
# Genre buku yang tersedia di perpustakaan
book_genre = ['History','Science','Education','Philosophy','Economy','Self Improvement','Magazine','Fiction']

# Data dummy untuk peminjam buku perpustakaan
users = {
    "Sulaiman Jassa": {
        "borrowed_books": [
            {"book_ID": 2, "borrow_date": datetime(2024, 7, 10), "return_date": None, "deadline_date": datetime(2024, 7, 17)},
            {"book_ID": 3, "borrow_date": datetime(2024, 8, 15), "return_date": None, "deadline_date": datetime(2024, 8, 22)}
        ],
        "total_fine": 0.0,
        "payments": []
    },
    "Justin Hubner": {
        "borrowed_books": [
            {"book_ID": 1, "borrow_date": datetime(2024, 8, 5), "return_date": None, "deadline_date": datetime(2024, 8, 12)},
            {"book_ID": 2, "borrow_date": datetime(2024, 9, 1), "return_date": None, "deadline_date": datetime(2024, 9, 8)}
        ],
        "total_fine": 0.0,
        "payments": []
    },
    "Juliana Batubara": {
        "borrowed_books": [
            {"book_ID": 3, "borrow_date": datetime(2024, 9, 1), "return_date": None, "deadline_date": datetime(2024, 9, 8)}
        ],
        "total_fine": 0.0,
        "payments": []
    },
    "Bisma Adhira": {
        "borrowed_books": [
            {"book_ID": 1, "borrow_date": datetime(2024, 8, 10), "return_date": None, "deadline_date": datetime(2024, 8, 17)},
            {"book_ID": 4, "borrow_date": datetime(2024, 8, 20), "return_date": None, "deadline_date": datetime(2024, 8, 27)}
        ],
        "total_fine": 0.0,
        "payments": []
    },
    "Joko Samudro": {
        "borrowed_books": [
            {"book_ID": 6, "borrow_date": datetime(2024, 9, 5), "return_date": None, "deadline_date": datetime(2024, 9, 12)},
            {"book_ID": 10, "borrow_date": datetime(2024, 9, 10), "return_date": None, "deadline_date": datetime(2024, 9, 17)}
        ],
        "total_fine": 0.0,
        "payments": []
    }
}
admin_staff = {
    "admin1":{
        "username" : "admin1",
        "password" :"123"
    },
    "admin2":{
        "username" : "admin2",
        "password" : "123"
    }
}


#create
def add_new_books(Title, Genre, Publication_Year,Author,Stock):
    if not Title.strip():
        return "Book title cannot be empty"
    
    valid_genre = []
    for g in book_genre:
        valid_genre.append(g.lower())
    if Genre.lower() not in valid_genre:
        return "Invalid genre name. Please Select right genre"
    
    current_year = 2024
    if Publication_Year > current_year:
        return f"Year must be less than current year. Please change year"

    for char in Author:
        if char.isdigit():
            return "Author cannot be empty or contain any number"
        
    for book in books_data:
        if book['book_title'].lower() == Title.lower() and book['author'].lower() == Author.lower():
            return f"Book '{Title}' by {Author} already exists in the system. Cannot add duplicate."
        
    if Stock < 0:
        return "Please input number more than 0"

    new_id = len(books_data) + 1

    books_data.append({
        "book_ID" : new_id,
        "book_title":Title.title(),
        "genre" :Genre.capitalize(),
        "publication_year": Publication_Year,
        "author":Author.title(),
        "stock" :Stock
    })

    return f"book {Title.title()} was added successfully with new ID {new_id}"

#read
def view_all_books():
    table_headers = ["Book ID","Title","Genre","Publication Year","Author","Book Stock"]
    book_table = []
    for book in books_data:
        if book['stock'] >= 0:
            book_table.append([book["book_ID"], book['book_title'], book['genre'], book['publication_year'], book['author'], book['stock']])
    return tabulate(book_table, table_headers, tablefmt="grid")

#update
def update_book_stock(ID, add_or_reduce, stock_change):
    for book in books_data:
        if book["book_ID"] == ID:
            if add_or_reduce == "add":
                book['stock'] = book['stock'] + stock_change
                return f"stock updated"
            elif add_or_reduce == 'reduce':
                if book['stock'] >= stock_change :
                    book['stock'] = book['stock'] - stock_change 
                    return f"Stock Updated"
                else:
                    return f"Not Enough Stock"

            else:
                return "Your Input is wrong"         
    else:
        return "Book not found"
    
def delete_book(ID):
    global books_data
    new_books = [] #new list for adding books_data except book_ID that was deleted
    for book in books_data:
        if book["book_ID"] != ID:
            new_books.append(book)
    
    #make sure len new_books is not same like global books_data
    if len(new_books) != len(books_data):
        books_data = new_books #update books_data
        return f"Book with ID {ID} deleted succesfully" 
    else:
        return f"Book bot found"

#additional feature (search by genre, borrow and return book, login admin)
def search_by_genre(Genre):
    
    table_headers = ['book_ID','Title','Genre','Author','Publication Year','Stock']
    book_table = []
    for book in books_data:
        if (book['genre']).lower() == Genre.lower():
            book_table.append([book["book_ID"], book['book_title'], book['genre'], book['publication_year'], book['author'], book['stock']])
    if len(book_table) == 0:
        return "No Books found for the specified genre"
    
    return tabulate(book_table, table_headers, tablefmt="grid")

def view_book_status():
   # Define the headers for the table
    headers = ["Username", "Book ID", "Title", "Borrow Date", "Deadline Date", "Return Date", "Status", "Fine"]
    table = []

    # Iterate over all users
    for username, user in users.items():
        # Iterate over all books borrowed by the current user
        for borrowed in user["borrowed_books"]:
            # Find the corresponding book in the books list
            book = None
            for b in books_data:
                if b["book_ID"] == borrowed["book_ID"]:
                    book = b
                    break

            if book is not None:
                # Gather details about the borrowed book
                book_title = book["book_title"]
                borrow_date = borrowed["borrow_date"].strftime("%Y-%m-%d")
                deadline_date = borrowed["deadline_date"].strftime("%Y-%m-%d")
                return_date = borrowed["return_date"].strftime("%Y-%m-%d") if borrowed["return_date"] else "Not Returned"

                # Initialize fine and status variables
                fine = 0.0
                status = "Not Returned"

                # Determine the status of the book
                if borrowed["return_date"]:
                    status = "Returned"
                elif datetime.now() > borrowed["deadline_date"]:
                    overdue_days = (datetime.now() - borrowed["deadline_date"]).days
                    fine_per_day = book.get("fine_per_day", 0.0)
                    fine = overdue_days * fine_per_day

                # Add the data to the table
                table.append([username, borrowed["book_ID"], book_title, borrow_date, deadline_date, return_date, status, f"${fine:.2f}"])

    # Return the formatted table
    return tabulate(table, headers, tablefmt="grid")

def borrow_or_return_books(username, book_id, return_book=False):
    # Fetch the user object
    if username not in users:
        # Create a new user entry
        users[username] = {
            "borrowed_books": [],
            "total_fine": 0.0,
            "payments": []
        }
        print(f"New user '{username}' created.")
    user = users.get(username)
    if not user:
        return "User not found."

    # Find the book in the list of books by its ID
    book = None
    for b in books_data:
        if b["book_ID"] == book_id:
            book = b

    if not book:
        return "Book not found."

    if return_book:
        # Find the borrowed book in the user's borrowed books list
        borrowed_book = None
        for b in user["borrowed_books"]:
            if b["book_ID"] == book_id and b["return_date"] is None:
                borrowed_book = b
                break

        if not borrowed_book:
            return "This book was not borrowed or is already returned."

        # Update the return date and increment the stock
        borrowed_book["return_date"] = datetime.now()
        book["stock"] += 1

        # Calculate any fines
        fine = 0.0
        if borrowed_book["return_date"] > borrowed_book["deadline_date"]:
            overdue_days = (borrowed_book["return_date"] - borrowed_book["deadline_date"]).days
            fine = overdue_days * book.get("fine_per_day", 0.0)

        if fine > 0:
            user["total_fine"] += fine
            return f"Book returned successfully. You have a fine of IDR {fine:.2f} for this book. Please pay the fine."
        else:
            return "Book returned successfully. No fine due."

    else:
        # Check if the user has any outstanding fines
        if has_fines(user):
            return "You have outstanding fines. Please pay your fines before borrowing more books."

        # Check if the book is available in stock
        if book["stock"] <= 0:
            return "Book is not available."

        # Check if the user already borrowed the book
        for borrowed in user["borrowed_books"]:
            if borrowed["book_ID"] == book_id and borrowed["return_date"] is None:
                return "You already borrowed this book and have not returned it yet."

        # Add the borrowed book to the user's list
        user["borrowed_books"].append({
            "book_ID": book_id,
            "borrow_date": datetime.now(),
            "return_date": None,
            "deadline_date": datetime.now() + timedelta(days=7)
        })
        book["stock"] -= 1

        return "Book borrowed successfully."


def has_fines(user):
    for borrowed in user["borrowed_books"]:
        if borrowed["return_date"] is None:
            current_date = datetime.now()
            deadline_date = borrowed["deadline_date"]
            if current_date > deadline_date:
                for book in books_data:
                    if book["book_ID"] == borrowed["book_ID"]:
                        overdue_fine_days = (current_date - borrowed["deadline_date"]).days
                        fine = overdue_fine_days * book.get("fine_per_day", 0)
                        if fine > 0:
                            return True
    return False

def handle_payment_for_user(username,amount):
    user = users.get(username)
    if not user:
        return "User is not found"
    if amount > user["total_fine"]:
        return f"Payment exceeds total fine amount. Please pay {user["total_fine"]}"
    
    user["total_fine"] = user["total_fine"] - amount
    user["payments"].append({
        "amount": amount,
        "date":datetime.now()
    })

    if user["total_fine"] == 0:
        return "Fine is fully settled. Thank you"
    else:
        return f"fine partially settled. {username} still having fine {user["total_fine"]}"
    


def main_menu():
    while True:
        print("-----------Login Admin Menu---------------")
        print("1. Admin Login ")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = maskpass.advpass(prompt="Enter your password: ", mask="*")

            if username in admin_staff and admin_staff[username]["password"] == password:
                print("Login Success")
                library_menu()
            else:
                print("Invalid Username or Password. Try Again")
        elif choice == "2":
            exit()
        else:
            print("Invalid Input. Try Again")

def library_menu():
    while True:
        print("-------------------------\nPlease Choose One Menu of Library: ")
        print("1. Add New Book ")
        print("2. Show Available Books ")
        print("3. Update Book Stock ")
        print("4. Delete Book ")
        print("5. Search Book by Genre: ")
        print("6. View Book Status")
        print("7. Borrow or Return Book")
        print("8. Logout")
        
        choice = None
        while choice is None:
            user_input = input("Insert Number: ").strip()
            if user_input.isdigit():
                choice = int(user_input)
            else:
                print("Invalid Input. Please Write right number")
        try:
            if choice == 1:
                Title = input("Input title of book: ")
                Genre = input("Input genre of book: ")
                Author = input("Input author of book: ")
                Publication_Year = int(input("Input publication year of book: "))
                Stock = int(input("Input stock of book: ")) 
                print(add_new_books(Title, Genre, Publication_Year,Author,Stock))
            elif choice == 2:
                print(view_all_books())
            elif choice == 3:
                ID = int(input("Enter book ID to update stock of books: "))
                add_or_reduce = input("Choose add or reduce book stock: ")
                stock_change = int(input("Input stock change: "))
                if stock_change > 0 and add_or_reduce == "add":
                    print(update_book_stock(ID, add_or_reduce, stock_change))
                elif stock_change > 0 and add_or_reduce == "reduce":
                    print(update_book_stock(ID, add_or_reduce, stock_change))
                else:
                    print("Please input right action or number")
            elif choice == 4:
                ID = int(input("Input ID Book: "))
                aut = input('Do you want to the delete this book: ')
                while True:
                    try:
                        if aut.lower()  == "y":
                            print(delete_book(ID))
                            break
                        elif aut.lower() == "n":
                            library_menu()
                        else:
                            print('Wrong selection.')
                            break
                    except ValueError:
                        print("Wrong Input")
                        break
            elif choice == 5:
                Genre = input("Input genre: ")
                print(search_by_genre(Genre))
            elif choice == 6:
                print(view_book_status())
            elif choice == 7:
                username = input("input your username: ")
                if not username.isalpha():
                    print("Username must not contain any numerical digits. Please try again.")
                book_id  = int(input("Enter book ID: "))
                action = input("Type 'b' to borrow or type 'r' to return: ").strip().lower()
                if action == "b":
                    print(borrow_or_return_books(username, book_id))
                elif action == "r":
                    result = borrow_or_return_books(username, book_id, return_book=True)
                    print(result)
                    if "fine" in result:
                        while True:
                            amount = int(input("Enter amount to pay: "))
                            payment_result = handle_payment_for_user(username, amount)
                            if "fully settled" in payment_result:
                                break
                else:
                    print("Invalid action. Please type 'r or 'b' ")

            elif choice == 8:
                while True:
                    try:
                        logout_y_or_n = (input('Do you want to logout?')).lower()
                        if logout_y_or_n.lower() == "y":
                            main_menu()
                        elif logout_y_or_n.lower() == "n":
                            break
                        else:
                            print('Wrong Input. Please write correct input')
                    except ValueError:
                        print("Error not found : Wrong Input")
                        
        
        
        except ValueError:
            print('Invalid Input. Please Input the right number!!')

main_menu()