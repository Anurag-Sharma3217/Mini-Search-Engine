# Mini Search Engine V2

A command-line search engine built in Python as part of my software development learning journey.

This project stores documents, searches through them using keywords, tracks search history, saves data using file handling, and provides basic search analytics.

## Features

### Search System

* Search documents by keyword
* Multi-keyword search
* Case-insensitive matching
* Display all matching results
* Result numbering
* Result count display

### Document Management

* Add new documents
* View all documents
* Persistent storage using text files
* Automatic loading when the program starts

### Search History

* Store search history
* Load previous search history
* View all past searches

### Analytics

* Total searches performed
* Last search performed
* History size
* Most searched keyword

### Reliability

* Handles empty files
* Handles missing files
* Input validation
* Modular code structure

---

## Project Structure

```text
Mini-Search-Engine/
│
├── main.py
├── function.py
├── utils.py
├── fileHandling.py
│
├── documents.txt
├── historyfile.txt
│
├── README.md
├── .gitignore
└── LICENSE
```

### File Overview

#### main.py

Controls program flow and menu navigation.

#### Function.py

Contains application features such as searching, viewing data, analytics, and history.

#### Utils.py

Contains helper functions used throughout the project.

#### FileHandling.py

Handles saving and loading documents and search history.

#### documents.txt

Stores searchable documents.

#### historyfile.txt

Stores previous search queries.

---

## Example Workflow

1. Start program
2. Documents and history load automatically
3. Add documents
4. Search using one or multiple keywords
5. View search analytics
6. Exit program
7. Data is available next time the program runs

---

## Concepts Practiced

* Python functions
* Lists
* Dictionaries
* Loops
* Strings
* File handling
* Modular programming
* Searching algorithms
* Input validation
* Basic analytics
* Git
* GitHub

---

## Learning Goal

The purpose of this project is not to build a production search engine.

The purpose is to learn how software systems are structured, how data is stored and retrieved, and how multiple Python concepts work together inside one project.

---

## Future Improvements

* Search ranking and relevance scoring
* Better indexing system
* Object-oriented redesign
* GUI version using Tkinter
* Database storage
* API integration

---

## Status

Current Version: V2

Actively developed as part of my Python learning roadmap.

---

## Author

Anurag Sharma

Software engineering student and builder.
