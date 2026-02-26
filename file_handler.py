"""
File Handler - Persistence Layer
Handles saving and loading library data from JSON file
"""

import json
import os
from typing import List, Dict
from library_manager import Book, LibraryManager


class FileHandler:
    """Handle file I/O operations for library data"""
    
    def __init__(self, filename: str = "library_data.json"):
        self.filename = filename
    
    def save_library(self, manager: LibraryManager) -> bool:
        """
        Save all library data to JSON file
        Format: List of book dictionaries + metadata
        """
        try:
            data = {
                'next_id': manager.next_id,
                'books': [book.to_dict() for book in manager.books]
            }
            
            with open(self.filename, 'w') as f:
                json.dump(data, f, indent=4)
            
            return True
        except Exception as e:
            print(f"❌ Error saving library: {e}")
            return False
    
    def load_library(self, manager: LibraryManager) -> bool:
        """
        Load library data from JSON file
        Reconstructs all books and metadata
        """
        try:
            if not os.path.exists(self.filename):
                print(f"📝 No existing library file. Starting fresh!")
                return True
            
            with open(self.filename, 'r') as f:
                data = json.load(f)
            
            manager.next_id = data.get('next_id', 1)
            
            for book_data in data.get('books', []):
                book = Book.from_dict(book_data)
                manager.books.append(book)
                manager.book_map[book.book_id] = book
                manager.categories.add(book.category)
                manager.authors.add(book.author)
            
            return True
        except Exception as e:
            print(f"❌ Error loading library: {e}")
            return False


def export_to_json(manager: LibraryManager, filename: str = "library_export.json") -> bool:
    """Export library data in a readable format"""
    try:
        data = [book.to_dict() for book in manager.get_all_books()]
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except Exception as e:
        print(f"❌ Export failed: {e}")
        return False
