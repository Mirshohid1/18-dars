# SQLite Database Example

This project demonstrates basic operations with an SQLite database in Python. It includes creating tables, inserting data, and executing simple queries.

## Requirements

- Python 3.x
- SQLite (included in Python standard library)

## Project Structure

This script performs the following tasks:

1. Connects to (or creates) an SQLite database file named `18-dars.db`.
2. Creates three tables: `city`, `book`, and `user`.
3. Inserts sample data into these tables.
4. Executes queries to fetch data based on specific conditions.
5. Prints the results of the queries.

## Tables

### `city` Table

This table stores information about cities and includes the following columns:

- `id`: An integer that auto-increments and serves as the primary key.
- `city`: Name of the city (text).
- `country`: Name of the country (text).
- `postcode`: Postcode of the city (integer).

### `book` Table

This table stores information about books and includes the following columns:

- `id`: An integer that auto-increments and serves as the primary key.
- `name`: Name of the book (text, max length 50).
- `author`: Name of the author (text, max length 50).
- `category`: Category or genre of the book (text).
- `price`: Price of the book (optional, real number).

### `user` Table

This table stores information about users and includes the following columns:

- `id`: An integer that auto-increments and serves as the primary key.
- `first_name`: First name of the user (text, max length 50).
- `last_name`: Last name of the user (text, max length 50, optional).
- `age`: Age of the user (integer).

## Example Queries

1. Fetch all cities in `country1`:
   ```sql
   SELECT * FROM city WHERE country = 'country1';
