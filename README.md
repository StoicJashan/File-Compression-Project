# File Compressor

A simple desktop application built with Python and FreeSimpleGUI that allows users to compress one or more files into a single ZIP archive.

## Features

* Select multiple files to compress
* Choose a destination folder for the ZIP archive
* Automatically creates a `compressed.zip` file
* Simple and beginner-friendly graphical interface

## Technologies Used

* Python
* FreeSimpleGUI
* `zipfile` (built-in Python module)
* `pathlib` (built-in Python module)

## Project Structure

```text
.
├── bonus_GUI.py            # GUI application
├── zip_creator.py     # ZIP archive creation logic
└── README.md
```

## How It Works

1. Select one or more files using the **Choose** button.
2. Select the destination folder where the ZIP file will be saved.
3. Click **Compress**.
4. The application creates a `compressed.zip` file in the selected destination containing all the chosen files.

## Learning Outcomes

This project helped me practice:

* Building desktop GUI applications with FreeSimpleGUI
* Working with Python modules and functions
* Handling user input and GUI events
* Creating ZIP archives using the `zipfile` module
* Managing file paths with `pathlib`
* Organizing code into multiple Python files
