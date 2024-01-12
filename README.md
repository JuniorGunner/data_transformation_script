# Data Transformation Script 🔄

## Purpose of the Project 🚀
The project is designed to transform a specific structure of data from an Excel file into a more structured and usable format.

## Expected Input and Output 📥📤
- Input: Excel file containing site metrics in rows.
- Output: Excel file with columns ['Day of Month', 'Date', 'Site ID', 'Page Views', 'Unique Visitors', 'Total Time Spent', 'Visits', 'Average Time Spent on Site'].

## Installation Steps 🔧
1. Clone the `data_transformation_test` repository to your local machine.
2. Navigate to the project folder.
3. Ensure you have `pandas`, `openpyxl` and all other dependencies installed:
    ```bash
    pip install -r requirements.txt
    ```

## Instructions to Run the Project 🏃
1. Place your Excel file inside the `data_transformation_test` directory.
2. Execute `data_transformation.py`:
    ```bash
    python data_transformation.py
    ```
3. Check for a `output.xlsx` file at the root of your repository;

## Instructions to Run Tests 🧪
1. Install `pytest` (should be already satisfied when you installed requirements.txt):
    ```bash
    pip install pytest
    ```
2. Execute the test file:
    ```bash
    pytest test_data_transformation.py
    ```

## Use Cases and Edge Cases 🛠️
- The code is designed to handle Excel files that have metrics every three rows per site.
- Missing values are managed.

## Known Limitations 🚫
- The code assumes metrics are grouped in three rows per site.
- It's assumed the sheet name in Excel is `input_refresh_template`.
