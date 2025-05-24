# Command Line To-Do List App
A colourful command-line to-do list app built with Python


A simple, colorful command-line to-do list application built with Python. This project demonstrates fundamental programming concepts including file handling, error handling, and user input validation.

## Features

- ✅ **Add Tasks**: Add new tasks to your to-do list
- 📋 **Display Tasks**: View all current tasks with numbering
- ✅ **Mark Complete**: Mark tasks as completed and move them to completed list
- 🗑️ **Delete Tasks**: Remove tasks from your list
- 💾 **Auto-Save**: Tasks are automatically saved to file and persist between sessions
- 🌈 **Colorful Interface**: Color-coded menu and feedback using Colorama

## Screenshots

```
Main Menu
1: Add a new task
2: Display all tasks
3: Mark a task as completed
4: Delete a task
5: Exit the program
```

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/command-line-todo-list.git
   cd command-line-todo-list
   ```

2. **Install required dependencies**
   ```bash
   pip install colorama
   ```

3. **Run the application**
   ```bash
   python todo_list.py
   ```

## Requirements

- Python 3.6 or higher
- colorama library for colored terminal output

## How to Use

1. Run the program using `python todo_list.py`
2. Choose from the menu options (1-5)
3. Follow the prompts to manage your tasks
4. Your tasks are automatically saved to `my_task.txt`
5. Use option 5 to exit the program

## Python Concepts Demonstrated

This project showcases the following Python programming concepts:

- **Data Structures**: Lists for storing tasks
- **File I/O**: Reading from and writing to text files
- **Exception Handling**: Try/except blocks for error management
- **Loops**: While loops for menu system, for loops for displaying items
- **Conditionals**: If/elif/else statements for menu logic
- **Functions**: Modular code organization
- **Input Validation**: Ensuring user input is valid
- **External Libraries**: Using colorama for terminal colors

## Project Structure

```
command-line-todo-list/
│
├── todo_list.py          # Main application file
├── my_task.txt           # Task storage file (created automatically)
├── requirements.txt      # Project dependencies
└── README.md            # Project documentation
```

## Future Enhancements

Potential improvements for future versions:

- Add due dates for tasks
- Implement task priorities
- Create categories for tasks
- Add search functionality
- Export tasks to different formats

## Learning Journey

This is my second Python project, building upon fundamental concepts learned in my first calculator project. It demonstrates progression from basic GUI applications to command-line tools with file persistence.

## Author

Sanni Babalola - Beginner Python Developer

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- Built as part of my Python learning journey
- Inspired by the need for a simple, persistent task management tool
