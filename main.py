"""
Library Book Management System - Main Console Interface
Entry point for the application
"""

from library_manager import LibraryManager
from file_handler import FileHandler
import os


class LibraryUI:
    """Console-based user interface for library management"""
    
    def __init__(self):
        self.manager = LibraryManager()
        self.file_handler = FileHandler("library_data.json")
        self.load_sample_data = True  # Load sample data on first run
    
    def clear_screen(self):
        """Clear console screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_header(self, title: str):
        """Print formatted header"""
        print("\n" + "="*60)
        print(f"  {title}")
        print("="*60)
    
    def print_books(self, books):
        """Print list of books in formatted table"""
        if not books:
            print("📭 No books found!")
            return
        
        print(f"\n{'ID':<5} {'Title':<25} {'Author':<15} {'Year':<6} {'Category':<12} {'Status':<10}")
        print("-"*80)
        for book in books:
            status = "✅ ISSUED" if book.is_issued else "📖 AVAIL"
            print(f"{book.book_id:<5} {book.title:<25} {book.author:<15} {book.year:<6} {book.category:<12} {status:<10}")
    
    # ==================== MAIN MENU ====================
    
    def show_main_menu(self):
        """Display main menu options"""
        self.print_header("📚 LIBRARY BOOK MANAGEMENT SYSTEM")
        print("""
1. ➕ Add a new book
2. 🔍 Search books
3. 📊 View books
4. ✏️ Update book status
5. ❌ Delete book
6. 📑 Statistics
7. 💾 Save library
8. 🚪 Exit
        """)
        return input("Enter your choice (1-8): ").strip()
    
    # ==================== ADD BOOK ====================
    
    def add_book_menu(self):
        """Add a new book to library"""
        self.print_header("➕ ADD NEW BOOK")
        
        try:
            title = input("Enter book title: ").strip()
            if not title:
                print("❌ Title cannot be empty!")
                return
            
            author = input("Enter author name: ").strip()
            if not author:
                print("❌ Author cannot be empty!")
                return
            
            year = int(input("Enter publication year: ").strip())
            category = input("Enter category (Fiction/Non-Fiction/Science/History/etc): ").strip()
            
            if self.manager.add_book(title, author, year, category):
                print(f"✅ Book added successfully! (ID: {self.manager.next_id - 1})")
            else:
                print("❌ Failed to add book!")
        
        except ValueError:
            print("❌ Invalid input! Please enter a valid year.")
    
    # ==================== SEARCH BOOKS ====================
    
    def search_menu(self):
        """Display search options"""
        self.print_header("🔍 SEARCH BOOKS")
        print("""
1. Search by title
2. Search by author
3. Search by ID
4. Filter by category
5. Back to main menu
        """)
        choice = input("Select search type (1-5): ").strip()
        
        if choice == '1':
            title = input("Enter title keywords: ").strip()
            results = self.manager.search_by_title(title)
            print(f"\n📌 Found {len(results)} book(s)")
            self.print_books(results)
        
        elif choice == '2':
            author = input("Enter author name: ").strip()
            results = self.manager.search_by_author(author)
            print(f"\n📌 Found {len(results)} book(s)")
            self.print_books(results)
        
        elif choice == '3':
            try:
                book_id = int(input("Enter book ID: ").strip())
                book = self.manager.search_by_id(book_id)
                if book:
                    print("\n📌 Book found:")
                    self.print_books([book])
                else:
                    print("❌ Book not found!")
            except ValueError:
                print("❌ Invalid ID format!")
        
        elif choice == '4':
            print(f"\nAvailable categories: {', '.join(self.manager.get_categories())}")
            category = input("Enter category: ").strip()
            results = self.manager.filter_by_category(category)
            print(f"\n📌 Found {len(results)} book(s)")
            self.print_books(results)
        
        elif choice == '5':
            return
        else:
            print("❌ Invalid choice!")
    
    # ==================== VIEW BOOKS ====================
    
    def view_menu(self):
        """Display view options"""
        self.print_header("📊 VIEW BOOKS")
        print("""
1. View all books
2. View available books
3. View issued books
4. Sort by title
5. Sort by author
6. Sort by year
7. Back to main menu
        """)
        choice = input("Select view option (1-7): ").strip()
        
        if choice == '1':
            results = self.manager.get_all_books()
            print(f"\n📚 Total books: {len(results)}")
            self.print_books(results)
        
        elif choice == '2':
            results = self.manager.get_available_books()
            print(f"\n📖 Available books: {len(results)}")
            self.print_books(results)
        
        elif choice == '3':
            results = self.manager.get_issued_books()
            print(f"\n✅ Issued books: {len(results)}")
            self.print_books(results)
        
        elif choice == '4':
            results = self.manager.sort_by_title()
            print("\n🔤 Books sorted by title (A-Z)")
            self.print_books(results)
        
        elif choice == '5':
            results = self.manager.sort_by_author()
            print("\n✍️ Books sorted by author (A-Z)")
            self.print_books(results)
        
        elif choice == '6':
            results = self.manager.sort_by_year()
            print("\n📅 Books sorted by year (newest first)")
            self.print_books(results)
        
        elif choice == '7':
            return
        else:
            print("❌ Invalid choice!")
    
    # ==================== UPDATE BOOK ====================
    
    def update_menu(self):
        """Update book status (issue/return)"""
        self.print_header("✏️ UPDATE BOOK STATUS")
        print("""
1. Issue a book
2. Return a book
3. Back to main menu
        """)
        choice = input("Select action (1-3): ").strip()
        
        if choice == '1':
            try:
                book_id = int(input("Enter book ID to issue: ").strip())
                book = self.manager.search_by_id(book_id)
                
                if not book:
                    print("❌ Book not found!")
                elif book.is_issued:
                    print("❌ This book is already issued!")
                elif self.manager.issue_book(book_id):
                    print(f"✅ Book '{book.title}' issued successfully!")
                else:
                    print("❌ Failed to issue book!")
            except ValueError:
                print("❌ Invalid ID format!")
        
        elif choice == '2':
            try:
                book_id = int(input("Enter book ID to return: ").strip())
                book = self.manager.search_by_id(book_id)
                
                if not book:
                    print("❌ Book not found!")
                elif not book.is_issued:
                    print("❌ This book is already available!")
                elif self.manager.return_book(book_id):
                    print(f"✅ Book '{book.title}' returned successfully!")
                else:
                    print("❌ Failed to return book!")
            except ValueError:
                print("❌ Invalid ID format!")
        
        elif choice == '3':
            return
        else:
            print("❌ Invalid choice!")
    
    # ==================== DELETE BOOK ====================
    
    def delete_menu(self):
        """Delete a book from library"""
        self.print_header("❌ DELETE BOOK")
        
        try:
            book_id = int(input("Enter book ID to delete: ").strip())
            book = self.manager.search_by_id(book_id)
            
            if not book:
                print("❌ Book not found!")
            else:
                confirm = input(f"Are you sure you want to delete '{book.title}'? (yes/no): ").strip().lower()
                if confirm == 'yes':
                    if self.manager.delete_book(book_id):
                        print("✅ Book deleted successfully!")
                    else:
                        print("❌ Failed to delete book!")
                else:
                    print("🚫 Deletion cancelled.")
        except ValueError:
            print("❌ Invalid ID format!")
    
    # ==================== STATISTICS ====================
    
    def show_statistics(self):
        """Display library statistics"""
        self.print_header("📊 LIBRARY STATISTICS")
        
        stats = self.manager.get_statistics()
        print(f"""
📚 Total Books: {stats['total_books']}
📖 Available: {stats['available_books']}
✅ Issued: {stats['issued_books']}
📑 Categories: {stats['total_categories']}
✍️ Authors: {stats['total_authors']}

📋 All Categories: {', '.join(sorted(self.manager.get_categories())) if self.manager.get_categories() else 'None'}
        """)
    
    # ==================== SAMPLE DATA ====================
    
    def load_sample_books(self):
        """Load sample data for demonstration"""
        samples = [
            ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Fiction"),
            ("Sapiens", "Yuval Noah Harari", 2011, "Non-Fiction"),
            ("Python Crash Course", "Eric Matthes", 2015, "Programming"),
            ("The Catcher in the Rye", "J.D. Salinger", 1951, "Fiction"),
            ("Atomic Habits", "James Clear", 2018, "Self-Help"),
            ("Introduction to Algorithms", "CLRS", 2009, "Programming"),
            ("A Brief History of Time", "Stephen Hawking", 1988, "Science"),
            ("Dune", "Frank Herbert", 1965, "Science-Fiction"),
        ]
        
        for title, author, year, category in samples:
            self.manager.add_book(title, author, year, category)
        
        # Issue a few books for demo
        self.manager.issue_book(1)
        self.manager.issue_book(3)
        print("✅ Sample data loaded!")
    
    # ==================== MAIN LOOP ====================
    
    def run(self):
        """Main application loop"""
        # Load existing data
        self.file_handler.load_library(self.manager)
        
        # Load sample data if library is empty
        if len(self.manager.books) == 0 and self.load_sample_data:
            print("📚 Loading sample books...\n")
            self.load_sample_books()
            self.file_handler.save_library(self.manager)
        
        while True:
            self.clear_screen()
            choice = self.show_main_menu()
            
            if choice == '1':
                self.add_book_menu()
            elif choice == '2':
                self.search_menu()
            elif choice == '3':
                self.view_menu()
            elif choice == '4':
                self.update_menu()
            elif choice == '5':
                self.delete_menu()
            elif choice == '6':
                self.show_statistics()
            elif choice == '7':
                if self.file_handler.save_library(self.manager):
                    print("✅ Library saved successfully!")
                else:
                    print("❌ Failed to save library!")
            elif choice == '8':
                confirm = input("Save before exiting? (yes/no): ").strip().lower()
                if confirm == 'yes':
                    self.file_handler.save_library(self.manager)
                print("\n👋 Thank you for using Library Management System!")
                break
            else:
                print("❌ Invalid choice! Please try again.")
            
            if choice in ['1', '2', '3', '4', '5', '6']:
                input("\n\nPress Enter to continue...")


def main():
    """Application entry point"""
    ui = LibraryUI()
    ui.run()


if __name__ == "__main__":
    main()
