# Library Management System

A simple library management system implemented in Python using MySQL.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Add and display books.
- Add and display members.
- Issue and return books.
- Display transaction history.

## Prerequisites

- Python 3.x
- MySQL

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/username/library_management.git
    ```

2. Create a MySQL database named `library`.

3. Create tables using the following queries:

    ```sql
    CREATE TABLE books (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255),
        author VARCHAR(255),
        genre VARCHAR(255),
        copies INT
    );

    CREATE TABLE members (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        address VARCHAR(255),
        phone VARCHAR(15)
    );

    CREATE TABLE transactions (
        id INT AUTO_INCREMENT PRIMARY KEY,
        book_id INT,
        member_id INT,
        FOREIGN KEY (book_id) REFERENCES books(id),
        FOREIGN KEY (member_id) REFERENCES members(id)
    );
    ```

4. Update MySQL credentials in `database.py`.

## Usage

1. Run `main.py` to start the Library Management System.

2. Follow the prompts to perform various operations.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.

2. Create a new branch: `git checkout -b feature/your-feature`.

3. Make your changes and commit them: `git commit -m 'Add some feature'`.

4. Push to the branch: `git push origin feature/your-feature`.

5. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



Make sure to replace placeholders like `username`, and provide specific details related to your project.
