library_books = [] 
waiting_list = []
recent_returns = []

#Functions for Features 

def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author: ")
    
    # Create a 'Node'
    new_book = {
        "id": book_id,
        "title": title,
        "author": author,
        "status": "Available"
    }
    library_books.append(new_book)
    print(f"Book '{title}' added successfully!")

def search_book():
    query = input("Search by Title or ID: ").lower()
    found = False
    
    for book in library_books:
        if query == book["id"].lower() or query == book["title"].lower():
            print(f"\nFound: ID: {book['id']} | Title: {book['title']} | Status: {book['status']}")
            found = True
            break
            
    if not found:
        print("Book not found in the library.")

def issue_book():
    title = input("Enter the title of the book to issue: ")
    for book in library_books:
        if book["title"].lower() == title.lower():
            if book["status"] == "Available":
                book["status"] = "Issued"
                print(f"Book '{title}' has been issued.")
                return
            else:
                print(f"Book is already issued. Adding you to the waiting list.")
                user_name = input("Enter your name: ")
                waiting_list.append(user_name) # Queue: Add to end
                return
    print("Book title does not exist.")

def return_book():
    title = input("Enter the title of the book to return: ")
    for book in library_books:
        if book["title"].lower() == title.lower():
            book["status"] = "Available"
            recent_returns.append(title) # Stack: Add to top
            print(f"Book '{title}' returned.")
            
            if waiting_list:
                next_person = waiting_list.pop(0) # Queue: Remove from front
                print(f"NOTICE: {next_person} is next in line for this book.")
            return
    print("This book does not belong to our library.")

def display_books():
    print("\n--- Current Library Collection ---")
    if not library_books:
        print("The library is empty.")
    for book in library_books:
        print(f"ID: {book['id']} | Title: {book['title']} | Status: {book['status']}")
    
    print(f"\nRecently Returned (Stack): {recent_returns[-3:]}") # Shows last 3
    print(f"Current Waiting List (Queue): {waiting_list}")

#Main Menu 

while True:
    print("\n=== Library Menu ===")
    print("1. Add New Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display All Books")
    print("6. Exit")
    
    choice = input("Select an option (1-6): ")
    
    if choice == '1':
        add_book()
    elif choice == '2':
        search_book()
    elif choice == '3':
        issue_book()
    elif choice == '4':
        return_book()
    elif choice == '5':
        display_books()
    elif choice == '6':
        print("Exiting system. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")