# 🚀 Quick Start Guide

## Running the Project

```bash
cd c:\Users\deepa\OneDrive\Desktop\librarymanagement
python main.py
```

## What You Get

✅ **Console Menu Interface** - User-friendly navigation
✅ **Sample Data** - 8 pre-loaded books on first run
✅ **Auto-Save** - Data persists in `library_data.json`
✅ **Full Features** - Add, search, filter, sort, delete books

---

## 📋 File Structure Explained

| File | Purpose | Lines |
|------|---------|-------|
| **main.py** | Console UI and user interactions | ~350 |
| **library_manager.py** | Core DSA logic and algorithms | ~280 |
| **file_handler.py** | JSON persistence layer | ~50 |
| **README.md** | Complete technical documentation | ~400 |
| **INTERVIEW_GUIDE.md** | Interview Q&A and explanations | ~300 |
| **RESUME_GUIDE.md** | Resume bullets and talking points | ~250 |

---

## 🎯 Understanding the Data Structures

### Visualized:

```python
# Adding a book with ID 1:
manager.add_book("Sapiens", "Yuval Noah Harari", 2011, "Non-Fiction")

# Now we have:

# 1. LIST (Sequential)
self.books = [
    Book(1, "Sapiens", "Yuval Noah Harari", 2011, "Non-Fiction", False)
]

# 2. DICTIONARY (Fast lookup by ID)
self.book_map = {
    1: Book(1, "Sapiens", ...) → Direct pointer to book
}

# 3. SETS (Unique tracking)
self.categories = {"Non-Fiction"}
self.authors = {"Yuval Noah Harari"}
```

### When Each Gets Used:

```
┌─────────────────────────────────────────────┐
│ Operation              │ Data Structure Used │
├─────────────────────────────────────────────┤
│ Add book               │ List + Dict + Sets  │
│ Search by ID           │ Dict (O(1)) ✨     │
│ Search by title        │ List (O(n))        │
│ Filter by category     │ List (O(n))        │
│ Sort by title          │ List (O(n log n))  │
│ Get all categories     │ Set (O(1) access)  │
│ Remove book            │ List + Dict        │
└─────────────────────────────────────────────┘
```

---

## 📊 Complexity Sheet (Memorize This!)

```
┌────────────────────────────────────────────┐
│ Operation           │ Complexity │ Why?    │
├────────────────────────────────────────────┤
│ Add Book            │ O(1)       │ append  │
│ Search by ID        │ O(1)       │ dict    │
│ Search Title/Author │ O(n)       │ scan    │
│ Sort                │ O(nlogn)   │ timsort │
│ Delete              │ O(n)       │ remove  │
│ Filter              │ O(n)       │ iterate │
│ Get categories      │ O(1)       │ set ref │
└────────────────────────────────────────────┘
```

---

## 🧪 Testing Ideas

Try these to understand the code:

### Test 1: Add & Search
```
1. Add: "Clean Code", "Robert Martin", 2008, "Programming"
2. Note the ID (should be 1 if first book)
3. Search by ID → O(1) lookup!
4. Search by Title → O(n) scan!
```

### Test 2: Sorting
```
1. Add 3 books with different years
2. Sort by year → See them reordered
3. Sort by title → See alphabetical order
```

### Test 3: Persistence
```
1. Add a book
2. Save (menu option 7)
3. Exit the program
4. Run again
5. Your book is still there! (loaded from JSON)
```

### Test 4: Categories
```
1. Add 3 books with category "Fiction"
2. Add 2 books with category "Science"
3. Check Statistics → Shows unique categories
4. Filter by "Fiction" → Shows all Fiction books
```

---

## ❓ Quick FAQ

**Q: Why no external libraries?**
A: Keeps focus on DSA. In production, I'd use SQLAlchemy, Pydantic, etc.

**Q: Why console, not GUI?**
A: Demonstrates DSA logic clearly without UI complexity.

**Q: Why so much documentation?**
A: Shows communication skills and interview readiness.

**Q: Can I add features?**
A: Yes! Add user authentication, fines, reservations, etc.

**Q: Should I use this as-is for interviews?**
A: Yes, but customize the talking points and add 1-2 features to make it uniquely yours.

---



