# Practice Python Core Programming 

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)

Welcome to the **Practice Python Core Programming** repository! This project serves as a comprehensive, structured learning path for mastering Python, progressing from fundamental syntax to advanced concepts and practical application development.

## Repository Structure

The exercises and projects are organized sequentially by topic to facilitate step-by-step learning.

### Part 1: Fundamentals
* **[`01_basics`](./01_basics)**: Introduction to Python syntax, variables, and basic I/O.
* **[`02_object_types`](./02_object_types)**: Deep dive into Python's data types (numbers, strings, lists, dictionaries, tuples, sets).
* **[`03_conditionals`](./03_conditionals)**: Control flow using `if`, `elif`, and `else` statements.
* **[`04_loops`](./04_loops)**: Iteration with `for` and `while` loops.
* **[`05_iteration_tools`](./05_iteration_tools)**: Advanced iteration techniques and tools.

### Part 2: Functional Programming & Scopes
* **[`06_functions`](./06_functions)**: Defining functions, arguments, parameters, and return values.
* **[`07_scopes_and_closure`](./07_scopes_and_closure)**: Understanding variable scope (global vs local) and closures.
* **[`09_decorator`](./09_decorator)**: Implementing decorators to modify function behavior.

### Part 3: Object-Oriented Programming (OOP)
* **[`08_oops`](./08_oops)**: Classes, objects, inheritance, polymorphism, and encapsulation.

### Part 4: Practical Projects (YouTube Manager)
A series of mini-projects building a manager application using different data storage methods to understand persistence:
* **[`10_youtube_manager`](./10_youtube_manager)**: A simple CLI-based YouTube video manager using **File I/O** (txt/json) for storage.
* **[`11_youtubemanager_sqlite`](./11_youtubemanager_sqlite)**: Upgraded version of the manager using **SQLite** for relational database storage.
* **[`13_Python_and_mongodb`](./13_Python_and_mongodb)**: Advanced version integrating **MongoDB** (NoSQL) for data persistence.

### Part 5: Advanced Topics & Tools
* **[`12_api_handling`](./12_api_handling)**: Fetching and processing data from external APIs.
* **[`14_virtualpy`](./14_virtualpy)**: Setting up and managing Python Virtual Environments.
* **[`15_using_jupyter_notebook_vscode`](./15_using_jupyter_notebook_vscode)**: Guide/examples for using Jupyter Notebooks within VS Code.

---

## Getting Started

### Prerequisites
* **Python 3.x** installed on your system.
* Basic understanding of using the terminal/command prompt.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/aman6303/practice-python-core-programming.git](https://github.com/aman6303/practice-python-core-programming.git)
    cd practice-python-core-programming
    ```

2.  **Set up a Virtual Environment (Recommended):**
    It is good practice to run projects in an isolated environment.
    ```bash
    # Create virtual environment
    python -m venv venv

    # Activate it (Windows)
    venv\Scripts\activate

    # Activate it (Mac/Linux)
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    Most basic folders rely only on the Python standard library. However, for **Folder 13 (MongoDB)**, you need `pymongo`:
    ```bash
    pip install pymongo
    ```

## Acknowledgements

I learned these concepts and built these projects following the tutorial series by **Chai aur code**. 
You can find the original playlist here: https://youtube.com/playlist?list=PLu71SKxNbfoBsMugTFALhdLlZ5VOqCg2s&si=IT9v8s8x4kEEopsz

Special thanks to the instructor for the clear explanations!


## License
### This project is open-source and available for educational purposes.
---

