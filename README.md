# Library Management System

A simple Python-based application to manage a library's book collection, handle issuing/returning books, and manage a waiting list for popular titles.

# Project Overview
This project was built to demonstrate how different **Data Structures** work together in a real-world scenario. Instead of just storing everything in a basic list, this system uses specific logic for different tasks:

* **Linked List:** Used for the main book database to store details like ID, Title, and Author.
* **Queue:** Used for the "Waiting List." The person who joins the list first gets the book first when it's returned.
* **Stack:** Used to track "Recently Returned" books. The most recently returned book appears at the top of the stack.
* **Searching:** A simple linear search algorithm to find books by their unique ID or Title.

# Features
* **Add Books:** Input a book's ID, title, and author to add it to the library system.
* **Search:** Quickly find if a book exists using its name or ID.
* **Issue Books:** Mark a book as "Issued." If the book is already out, the system automatically adds the user to a waiting list.
* **Return Books:** Mark a book as "Available" and automatically notify the next person in the waiting queue.
* **Display All:** View the entire collection and see the current status of the Stack and Queue.

## How to Run
1. Ensure you have **Python 3** installed on your machine.
2. Clone this repository to your local VS Code environment.
3. Create a file named `code.py` and paste the logic there.
4. Run the following command in your terminal:
   ```bash
   python code.py
