# ============================================================
# Day 19 - Library Management System
#
# Difficulty:
# Medium
#
# Concepts:
# - OOP
# - Composition
# - Dictionary/List
# - Exception Handling
# - Object State
#
# ------------------------------------------------------------
#
# Problem Statement
#
# Design a Library Management System.
#
# Create TWO classes:
#
# 1. Book
# 2. Library
#
# ------------------------------------------------------------
#
# Book should contain:
#
# - book_id
# - title
# - author
# - is_issued
# - issued_to
#
# ------------------------------------------------------------
#
# Library should support:
#
# add_book(book)
#
# remove_book(book_id)
#
# search_book(book_id)
#
# issue_book(book_id, student_name)
#
# return_book(book_id)
#
# display_all_books()
#
# display_available_books()
#
# ------------------------------------------------------------
#
# Rules
#
# 1. Book ID must be unique.
#
# 2. Cannot issue an already issued book.
#
# 3. Cannot return a book that wasn't issued.
#
# 4. Removing a non-existing book should show a proper message.
#
# 5. Searching should return the Book object or None.
#
# ------------------------------------------------------------
#
# Bonus
#
# Track:
#
# - issue_date
# - return_date
#
# using datetime.
#
# ------------------------------------------------------------
#
# Bonus 2
#
# Show how many books are currently issued.
#
# ============================================================


class Book:
    def __init__(self,book_id,title,author,is_issued, issued_to):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = is_issued
        self.issued_to = issued_to


class Library:
    def __init__(self):
        books_list = []
    
    def add_books(self):
        pass

    def remove_book(self, book_id):
        pass

    def search_book(self, book_id):
        pass

    def issue_book(self, book_id, student_name):
        pass

    def return_book(self, book_id):
        pass

    def display_all_books(self,book_id):
        pass

    def display_available_books(self):
        pass

    

if __name__=="__main__":
    pass