"""
Library Book Management System - Core Logic
Demonstrates: List, Dictionary, Set, Searching, Filtering, Sorting
"""

from typing import List, Dict, Set, Optional
from datetime import datetime


class Book:
    """Represents a single book in the library"""
    
    def __init__(self, book_id: int, title: str, author: str, 
                 year: int, category: str, is_issued: bool = False):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.category = category
        self.is_issued = is_issued
    
    def __repr__(self) -> str:
        status = "ISSUED" if self.is_issued else "AVAILABLE"
        return (f"ID: {self.book_id} | {self.title} | {self.author} | "
                f"{self.year} | {self.category} | [{status}]")
    
    def to_dict(self) -> Dict:
        """Convert book to dictionary for file storage"""
        return {
            'book_id': self.book_id,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'category': self.category,
            'is_issued': self.is_issued
        }
    
    @staticmethod
    def from_dict(data: Dict) -> 'Book':
        """Create book from dictionary"""
        return Book(
            data['book_id'], data['title'], data['author'],
            data['year'], data['category'], data['is_issued']
        )


class LibraryManager:
    """
    Core library management system using DSA:
    - List: store books sequentially
    - Dictionary: map book_id to Book object (O(1) lookup)
    - Set: track unique categories and authors (fast membership check)
    - Sorting: sort books by title, author, year
    """
    
    def __init__(self):
        """Initialize library with empty collections"""
        self.books: List[Book] = []                    # List: sequential storage
        self.book_map: Dict[int, Book] = {}            # Dict: O(1) lookup by ID
        self.categories: Set[str] = set()              # Set: unique categories
        self.authors: Set[str] = set()                 # Set: unique authors
        self.next_id: int = 1
    
    # ==================== ADD OPERATIONS ====================
    
    def add_book(self, title: str, author: str, year: int, category: str) -> bool:
        """
        Add a new book to the library
        Time Complexity: O(1) average case
        """
        # Create new book with auto-incremented ID
        book = Book(self.next_id, title, author, year, category)
        
        # Add to List (O(1) append)
        self.books.append(book)
        
        # Add to Dictionary (O(1) insert)
        self.book_map[self.next_id] = book
        
        # Add to Sets (O(1) insert)
        self.categories.add(category)
        self.authors.add(author)
        
        self.next_id += 1
        return True
    
    # ==================== SEARCH OPERATIONS ====================
    
    def search_by_title(self, title: str) -> List[Book]:
        """
        Search books by title (case-insensitive)
        Time Complexity: O(n) - linear search through all books
        """
        title_lower = title.lower()
        results: List[Book] = []
        
        for book in self.books:
            if title_lower in book.title.lower():
                results.append(book)
        
        return results
    
    def search_by_author(self, author: str) -> List[Book]:
        """
        Search books by author (case-insensitive)
        Time Complexity: O(n)
        """
        author_lower = author.lower()
        results: List[Book] = []
        
        for book in self.books:
            if author_lower in book.author.lower():
                results.append(book)
        
        return results
    
    def search_by_id(self, book_id: int) -> Optional[Book]:
        """
        Search book by ID using Dictionary
        Time Complexity: O(1) - direct lookup in dictionary
        This demonstrates why HashMap is useful!
        """
        return self.book_map.get(book_id)
    
    # ==================== FILTER OPERATIONS ====================
    
    def filter_by_category(self, category: str) -> List[Book]:
        """
        Filter books by category
        Time Complexity: O(n)
        """
        return [book for book in self.books if book.category.lower() == category.lower()]
    
    def get_available_books(self) -> List[Book]:
        """
        Get all available (not issued) books
        Time Complexity: O(n)
        """
        return [book for book in self.books if not book.is_issued]
    
    def get_issued_books(self) -> List[Book]:
        """
        Get all issued books
        Time Complexity: O(n)
        """
        return [book for book in self.books if book.is_issued]
    
    # ==================== SORTING OPERATIONS ====================
    
    def sort_by_title(self) -> List[Book]:
        """
        Sort books by title alphabetically
        Time Complexity: O(n log n) - using Python's Timsort
        """
        return sorted(self.books, key=lambda book: book.title.lower())
    
    def sort_by_author(self) -> List[Book]:
        """
        Sort books by author alphabetically
        Time Complexity: O(n log n)
        """
        return sorted(self.books, key=lambda book: book.author.lower())
    
    def sort_by_year(self) -> List[Book]:
        """
        Sort books by year (newest first)
        Time Complexity: O(n log n)
        """
        return sorted(self.books, key=lambda book: book.year, reverse=True)
    
    # ==================== UPDATE OPERATIONS ====================
    
    def update_book(self, book_id: int, title: str = None, author: str = None,
                   year: int = None, category: str = None) -> bool:
        """
        Update book details
        Time Complexity: O(1) - direct dictionary lookup
        """
        book = self.book_map.get(book_id)
        if not book:
            return False
        
        if title:
            book.title = title
        if author:
            book.author = author
        if year:
            book.year = year
        if category:
            book.category = category
        
        # Update category and author sets
        self.categories.add(book.category)
        self.authors.add(book.author)
        
        return True
    
    def issue_book(self, book_id: int) -> bool:
        """
        Mark a book as issued
        Time Complexity: O(1)
        """
        book = self.book_map.get(book_id)
        if not book:
            return False
        if book.is_issued:
            return False  # Already issued
        
        book.is_issued = True
        return True
    
    def return_book(self, book_id: int) -> bool:
        """
        Mark a book as returned (available)
        Time Complexity: O(1)
        """
        book = self.book_map.get(book_id)
        if not book:
            return False
        if not book.is_issued:
            return False  # Already available
        
        book.is_issued = False
        return True
    
    # ==================== DELETE OPERATIONS ====================
    
    def delete_book(self, book_id: int) -> bool:
        """
        Delete a book from the library
        Time Complexity: O(n) - list removal is O(n)
        """
        book = self.book_map.get(book_id)
        if not book:
            return False
        
        # Remove from List (O(n))
        self.books.remove(book)
        
        # Remove from Dictionary (O(1))
        del self.book_map[book_id]
        
        return True
    
    # ==================== UTILITY OPERATIONS ====================
    
    def get_all_books(self) -> List[Book]:
        """Get all books"""
        return self.books
    
    def get_categories(self) -> Set[str]:
        """Get all unique categories (using Set)"""
        return self.categories
    
    def get_authors(self) -> Set[str]:
        """Get all unique authors (using Set)"""
        return self.authors
    
    def get_statistics(self) -> Dict:
        """Get library statistics"""
        return {
            'total_books': len(self.books),
            'available_books': len(self.get_available_books()),
            'issued_books': len(self.get_issued_books()),
            'total_categories': len(self.categories),
            'total_authors': len(self.authors)
        }
