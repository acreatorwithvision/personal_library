#This is used to create book class where objects of book can 
#be created to store the books.

class Book:
    """Represent a single book in the library"""
    
    def __init__(self,title,author,isbn):
        """Initialize the book object"""
        self.title=title
        self.author=author
        self.isbn=isbn

    def __repr__(self):
        """Provide string representation of the book"""
        return f"Book(Title: '{self.title}', Author: '{self.author}', ISBN: '{self.isbn}')"
    

    #Also, returning in dictionary format for JSON serialization
    def __to_dict__(self):
        return {
            'title':self.title,
            'author':self.author,
            'isbn': self.isbn
        }
