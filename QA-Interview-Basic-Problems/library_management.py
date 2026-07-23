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

import datetime

class Book:
    def __init__(self,book_id,title,author):
        self.book_id = book_id
        self.title = title
        self.author = author

        self.is_issued = False
        # self.issued_to = None


class Library:
    def __init__(self):
        self.books_list = []
        self.book_issue_list = []

    def add_books(self,book):
        if not self.search_book(book.book_id):
            self.books_list.append(book)
        else:
            print("Book already exist in the list")


    def remove_book(self, book_id):
        self.book_item = self.search_book(book_id)
        if self.remove_book:
            self.books_list.remove(self.book_item)
        else:
            print("Book not found")

    def search_book(self, book_id):
        for book_item in self.books_list:
            if book_item.book_id == book_id:
                return book_item
        return None

    def issue_book(self, book_id, student_name):
        self.book_item = self.search_book(book_id)
        if not self.book_item:
            self.book_issue_list.append(
                {
                    "book_id": book_id,
                    "student_name" : student_name,
                    "issue_date" : datetime.datetime.now(),
                    "return_date": None
                }
            )
        else:
            print("Book not found")

    def return_book(self, book_id):
        for book in self.books_list:
            if book.book_id == book_id and book.is_issued == True:
                book.is_issued = False

                for book in self.book_issue_list:
                    if book["book_id"] == book_id and book["return_date"] is None:
                        book["return_date"] = datetime.datetime.now()

                

    def display_all_books(self,book_id):
        pass

    def display_available_books(self):
        pass

    

if __name__=="__main__":
    pass