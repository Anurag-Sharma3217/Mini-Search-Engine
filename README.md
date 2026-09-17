# Mini Search Engine V2

A beginner Python project that simulates a simple local search engine using Python data structures, functions, multiple modules, and file handling.

This project was built as part of my Python learning journey to understand how search systems can store, retrieve, and match information.

## Features

* Search documents by keyword
* Display all stored documents
* Add new documents
* Store and display search history
* Save documents to a text file
* Load documents when the program starts
* Save search history to a text file
* Load previous search history
* Case-insensitive searching
* Modular Python code using multiple files
* Basic input validation

## Project Structure

```text
Search Engine V2/
│
├── main.py
├── Function.py
├── Utils.py
├── FileHandling.py
├── documents.txt
├── historyfile.txt
├── README.md
├── .gitignore
└── LICENSE
```

### `main.py`

Controls the main program flow and menu.

### `Function.py`

Contains the main application functions such as searching, viewing documents, adding documents, and displaying history.

### `Utils.py`

Contains reusable helper functions used by the application.

### `FileHandling.py`

Handles saving and loading documents and search history.

### `documents.txt`

Stores the documents used by the search engine.

### `historyfile.txt`

Stores previous search queries.

## How It Works

When the program starts, it loads previously saved documents and search history from text files.

The user can then:

1. Search for information
2. View stored documents
3. Add a new document
4. View search history
5. Exit the program

When new documents or searches are added, the information can be saved to the corresponding files.

## Technologies

* Python
* File Handling
* Lists
* Strings
* Loops
* Functions
* Modules
* Basic searching and matching
* Git & GitHub

## Learning Goals

This project was created to practice:

* Breaking a program into multiple modules
* Writing reusable functions
* Working with lists and strings
* Searching and matching data
* Persisting program data using files
* Debugging and handling edge cases
* Structuring a larger Python program

## Future Improvements

Planned improvements include:

* Multi-keyword searching
* Search relevance/ranking
* Better result presentation
* More advanced indexing
* Improved error handling
* Object-oriented design
* GUI interface
* Possible API/web integration

## Status

**Version 2 — In Development**

This is an educational project and is not intended to compete with real-world search engines.

## Author

Anurag Sharma

Built as part of my Python and software development learning journey.

