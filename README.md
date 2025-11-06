# Lab Overview

A basic Python program to load, filter, and analyze CSV data about cities and their temperatures.
The script demonstrates basic data manipulation — such as filtering cities by country, computing averages, and counting unique values — using Python’s built-in features and the csv module.

---

## Project Structure

* **`README.md`**: This file
* **`Cities.csv`**: A file contains city, country, latitude, longitude and temperature of many cities across the world.
* **`data_processing.py`**: A simple Python program to load, filter and aggregate data from `Cities.csv`.

---

## Design Overview

* **Load CSV data** into a list of dictionaries using a custom `DataLoader` class.
* **Filter data** with user-defined conditions via the `Table` class.
* **Aggregate data** using custom `aggregation` functions (e.g., average, max) via the `Table` class.

---

##  How to test and run your code

To run the demonstration script, execute `data_processing.py` from your terminal:

```bash
python data_processing.py
