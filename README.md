# Lab Overview

A basic Python program to load and analyze CSV data from cities and countries.
The script demonstrates basic data manipulation — such as filtering, aggregation, and joining — using Python’s built-in features and the csv module.

---

## Project Structure

```
oop_lab_1/
│
├── Cities.csv             # CSV file containing city data (e.g., country, temperature)
├── Countries.csv          # CSV file containing country data (e.g., population, EU status, coastline)
├── data_processing.py     # The main Python script
└── README.md              # This file

```

---

## Design Overview

### Class: DataLoader
- Responsible for loading CSV files and converting them into lists of dictionaries.
- Attributes:
  - `base_path` — The base directory path where the CSV files are located.
- Key Methods:
  - `load_csv(filename)` — Reads a CSV file and returns its content as a list of dictionaries, where each key corresponds to a column name.

### Class: DB
- Acts as an in-memory database to manage and search tables.
- Attributes:
  - `tables` — A list that holds all Table objects.
- Key Methods:
  - `insert(table)` — Adds a Table object to the database.
  - `search(table_name)` — Finds and returns a Table object by its name.

### Class: Table
- Represents a single table of data (a list of dictionaries). Provides methods for filtering, aggregating, and joining tables.
- Attributes:
  - `table_name` — The name of the table.
  - `table` — The list of dictionaries representing rows of data.
- Key Methods:
  - `filter(condition)` — Returns a new Table object containing only rows that meet a given condition (lambda function).
  - `aggregate(aggregation_function, aggregation_key)` — Applies an aggregation (e.g., sum, min, max, len) to a column of data.
  - `join(another_table, common_key)` — Merges two tables based on a shared column (key).
  - `__str__()` — Returns a string representation of the table for easy printing.

---

##  How to test and run your code

To run the demonstration script, execute `data_processing.py` from your terminal:

```bash
python data_processing.py
```