# 📚 Library Book Management System (DSA-Based)

A beginner to intermediate-level Python project demonstrating core Data Structures and Algorithms concepts in a practical, real-world application.

## 🎯 Project Overview

This is a console-based library management system that showcases fundamental DSA principles while solving a real problem. The system allows librarians to manage books efficiently with features like searching, filtering, sorting, and persistence.

### Key Learning Outcomes
- ✅ **List**: Sequential data storage and manipulation
- ✅ **Dictionary (HashMap)**: Fast O(1) lookups for book IDs
- ✅ **Set**: Tracking unique categories and authors efficiently
- ✅ **Searching**: Linear and HashMap-based searching strategies
- ✅ **Filtering**: Conditional data extraction
- ✅ **Sorting**: Multiple sorting criteria and algorithms
- ✅ **File Persistence**: JSON-based data storage

---

## 📁 Project Structure

```
librarymanagement/
│
├── main.py                 # Console UI and application entry point
├── library_manager.py      # Core DSA logic and business operations
├── file_handler.py         # File I/O and data persistence
├── library_data.json       # Persistent library data (auto-generated)
└── README.md              # This file
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.7+ (no external dependencies required)

### Installation & Running

1. **Clone or download the project**
```bash
cd librarymanagement
```

2. **Run the application**
```bash
python main.py
```

3. **Sample data will auto-load on first run** with 8 pre-populated books for demonstration

---

## 📖 Features

### 1. **Add Books**
- Add new books with title, author, year, and category
- Auto-incrementing book IDs using simple counter
- Books stored in List, Dictionary, and Sets simultaneously

### 2. **Search & Find**
- **Search by Title**: Case-insensitive partial matching
- **Search by Author**: Find all books by an author
- **Search by ID**: O(1) direct lookup using HashMap
- **Filter by Category**: Find books within a category

### 3. **View & Display**
- View all, available, or issued books
- Multiple sorting options:
  - Sort by Title (A-Z)
  - Sort by Author (A-Z)
  - Sort by Year (newest first)

### 4. **Issue & Return**
- Issue books (mark as unavailable)
- Return books (mark as available)
- View availability status

### 5. **Delete Books**
- Remove books from library with confirmation

### 6. **Statistics Dashboard**
- Total books count
- Available vs Issued breakdown
- Unique categories and authors

### 7. **Data Persistence**
- Auto-save to `library_data.json`
- Auto-load on startup
- Export functionality

---

## 💡 Data Structures & Algorithms Used

### **1. List** - `books: List[Book]`
```python
self.books: List[Book] = []  # Sequential storage
# Operations:
# - append(): Add books → O(1) amortized
# - remove(): Delete books → O(n)
# - iteration: Search/filter → O(n)
```
**When Used**: Storing all books sequentially, iterating for searches and filters.

---

### **2. Dictionary (HashMap)** - `book_map: Dict[int, Book]`
```python
self.book_map: Dict[int, Book] = {}  # book_id → Book object
# Operations:
# - insert/lookup/delete: → O(1) average case
```
**When Used**: 
- `search_by_id()`: Direct O(1) lookup instead of O(n) linear search
- `issue_book()`, `return_book()`: Direct access to book objects
- **Interview Tip**: "This prevents us from linearly searching through all books when we know the ID!"

---

### **3. Set** - `categories: Set[str]`, `authors: Set[str]`
```python
self.categories: Set[str] = set()  # Unique categories
self.authors: Set[str] = set()      # Unique authors
# Operations:
# - add(): Insert → O(1) average case
# - membership check: "is 'Fiction' in categories?" → O(1)
```
**When Used**:
- Tracking unique authors and categories
- Fast membership checks
- Preventing duplicates automatically

---

### **Time Complexity Analysis**

| Operation | Time Complexity | Why |
|-----------|-----------------|-----|
| Add Book | O(1) | List append + Dict insert both O(1) |
| Search by ID | O(1) | Direct HashMap lookup |
| Search by Title/Author | O(n) | Linear scan through all books |
| Filter by Category | O(n) | Must check every book |
| Issue/Return Book | O(1) | HashMap lookup + update |
| Delete Book | O(n) | List removal is O(n) |
| Sort by Title/Author/Year | O(n log n) | Python's Timsort algorithm |
| Get Available Books | O(n) | Filter all books |

---

## 🎓 How to Explain This in an Interview

### **Q: "Walk me through your data structure choices."**

**A**: "I used a combination of three data structures for different purposes:

1. **List** stores books sequentially for when I need to iterate through all books for general searches and filtering.

2. **Dictionary** maps book IDs to Book objects, giving me O(1) lookup time instead of O(n). When a user searches for a specific book by ID, I can retrieve it instantly.

3. **Set** automatically handles uniqueness and gives O(1) membership checks for categories and authors. No duplicates, no overhead."

---

### **Q: "Why not just use a List for everything?"**

**A**: "Great question! A List would work, but with tradeoffs:
- Searching by ID in a List is O(n) — I'd check every book
- With Dictionary, it's O(1) — I go straight to the book
- Sets ensure categories have no duplicates without manual checking
- For a small library, it's fine, but at scale (millions of books), this matters."

---

### **Q: "Can you describe a specific feature and its complexity?"**

**A**: "Sure! The `search_by_id` feature is particularly efficient:
```python
book = self.book_map.get(book_id)  # O(1) - direct lookup
```

Compare that to a less optimized version:
```python
book = None
for b in self.books:
    if b.book_id == book_id:  # O(n) - checking every book
        book = b
        break
```

The first approach scales from 100 books to 1 million books with no performance degradation."

---

### **Q: "What about the sorting feature?"**

**A**: "I use Python's built-in `sorted()` function with a lambda key:
```python
sorted(self.books, key=lambda book: book.title.lower())
```

This uses Timsort, which is O(n log n) and highly optimized. I could implement quicksort or merge sort, but standard library functions are battle-tested and often faster due to C-level optimizations."

---

### **Q: "What trade-offs did you make?"**

**A**: "When I delete a book, I remove it from both the List and Dictionary:
- List removal is O(n) because lists need to shift elements
- Dictionary removal is O(1)
- Overall: O(n) due to the List operation

For better deletion performance, I could use a linked list (O(1) removal) or just mark books as deleted instead of truly removing them. But for a library system, deletion is rare, and List's cache locality benefits outweigh this."

---

## 📊 Sample Usage

### Screen 1: Main Menu
```
============================================================
  📚 LIBRARY BOOK MANAGEMENT SYSTEM
============================================================

1. ➕ Add a new book
2. 🔍 Search books
3. 📊 View books
4. ✏️ Update book status
5. ❌ Delete book
6. 📑 Statistics
7. 💾 Save library
8. 🚪 Exit

Enter your choice (1-8): 6
```

### Screen 2: Statistics
```
============================================================
📊 LIBRARY STATISTICS
============================================================

📚 Total Books: 8
📖 Available: 6
✅ Issued: 2
📑 Categories: 6
✍️ Authors: 8

📋 All Categories: Fiction, Non-Fiction, Programming, Science, Science-Fiction, Self-Help
```

### Screen 3: Sort by Title
```
ID   Title                    Author           Year   Category     Status    
────────────────────────────────────────────────────────────────────────────
5    Atomic Habits           James Clear      2018   Self-Help    📖 AVAIL  
7    A Brief History of Time Stephen Hawking   1988   Science      📖 AVAIL  
8    Dune                    Frank Herbert    1965   Science-Fict📖 AVAIL  
1    The Great Gatsby        F. Scott Fitzer  1925   Fiction      ✅ ISSUED 
3    Python Crash Course     Eric Matthes     2015   Programming  📖 AVAIL  
2    Sapiens                 Yuval Noah Hara  2011   Non-Fiction  📖 AVAIL  
6    Introduction to Alg...  CLRS             2009   Programming  📖 AVAIL  
4    The Catcher in the R... J.D. Salinger   1951   Fiction      ✅ ISSUED 
```

---

## 🏆 Resume Bullet Points

Use these points when describing this project on your resume:

- **"Designed and implemented a Library Management System using DSA concepts (List, Dictionary, Set) to optimize search operations from O(n) to O(1) using HashMap lookups"**

- **"Built three-layered architecture separating UI (main.py), business logic (library_manager.py), and persistence (file_handler.py) following clean code principles"**

- **"Implemented 6+ search and filtering algorithms with various time complexities (O(1), O(n), O(n log n)), demonstrating understanding of performance tradeoffs"**

- **"Integrated JSON-based file persistence allowing auto-save/load with proper error handling and data validation"**

- **"Achieved 100% O(1) lookup for book ID searches using HashMap, enabling scalable performance for large datasets"**

- **"Applied sorting algorithms (Timsort) with multiple criteria and demonstrated data structure selection based on use case requirements"**

---

## 🧪 Testing the Features

### Test 1: Add & Search by ID
```
1. Add a book: "Clean Code", "Robert Martin", 2008, "Programming"
2. Note the ID
3. Search by ID → Should return instantly (and explain O(1) lookup!)
```

### Test 2: Sorting Performance
```
1. Add 10 books
2. Try sorting by title/author/year
3. Notice the output is sorted correctly
```

### Test 3: Persistence
```
1. Add a book
2. Save (option 7)
3. Exit and restart the program
4. The book should still be there (loaded from JSON)
```

### Test 4: Filtering
```
1. Filter by category "Programming"
2. Note how it only shows Programming books (O(n) scan)
```

---

## 📝 Code Quality Highlights

✅ **Clean Naming**: Variables like `is_issued`, `book_map`, `categories` are self-documenting
✅ **Type Hints**: All functions have argument and return types
✅ **Docstrings**: Every method explains what it does and why
✅ **Separation of Concerns**: UI, Logic, and Storage are separate
✅ **Comments**: DSA concepts are highlighted with complexity analysis
✅ **Error Handling**: Graceful error messages for invalid inputs
✅ **Constants**: Magic numbers avoided (uses `next_id` counter instead)

---

## 🎯 Next Steps (For Your Own Learning)

Want to extend this project? Consider:

1. **SQLite Integration**: Replace JSON with a database
2. **User Authentication**: Track who issues/returns books
3. **Fine Calculation**: Auto-calculate fines for overdue books
4. **Member Management**: Store member details
5. **Book Reservations**: Queue system for unavailable books
6. **Performance Testing**: Measure actual O(n) vs O(1) operations with large datasets
7. **Unit Tests**: Add pytest to test each component

---

## 📞 Interview Q&A Prep

**Q: Why did you choose this project?**
A: "I wanted to build something practical that clearly demonstrates DSA concepts. A real-world library system had multiple use cases (searching, filtering, sorting) that naturally needed different data structures and algorithms."

**Q: What was the most challenging part?**
A: "Deciding between List and Dictionary for storage. I realized that while a simple List works, Dictionary lookups are asymptotically faster. This taught me the importance of analyzing operations when choosing data structures."

**Q: What would you improve?**
A: "For production, I'd add a relational database (SQL) instead of JSON, implement user authentication, and add comprehensive logging. I'd also profile the code to find actual bottlenecks rather than relying only on theoretical complexity."

**Q: How does this relate to the job?**
A: "This shows I understand tradeoffs in system design. At [Company], choosing the right data structure for billions of records is crucial. This project proves I can think through those decisions."

---

## 📄 License

This project is free to use for educational and portfolio purposes.

---

**Created for: Software Engineer Interns | Learning DSA Through Practical Projects**

**Happy Learning! 🚀**
