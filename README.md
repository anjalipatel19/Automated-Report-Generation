# Automated-Report-Generation
A Python script that analyzes student performance data from Excel files and generates formatted PDF reports with statistics and visualizations.

**COMPANY:** CODETECH IT SOLUTIONS

**Name:** Anjali Dilip Patel

**INTERN ID:** CT06DL927

**Domain:** Python Programming

**BATCH Duration:** 6 Weeks

**Mentor:** Neela Santhosh Kumar

**PROJECT:** AUTOMATED REPORT GENERATION  

# Data Analysis and PDF Report Generator

## Overview

This Python project reads student performance data from an Excel file and generates a professional PDF report containing analysis and visual representation of academic performance metrics.

## Features

* *Excel Integration*: Reads data directly from Excel files (.xlsx format)
* *Data Analysis*:
  * Calculates subject averages (Math, Science, English)
  * Computes overall attendance percentage
  * Identifies top performers in each subject
* *PDF Report Generation*:
  * Summary statistics section
  * Top performers highlight
  * Clean data table with alternating row colors
* *Professional Styling*:
  * Consistent font styling
  * Proper section spacing
  * Clear headers and labels

## Requirements  
- Python 3.x  
- Required libraries:
 
  ```bash
  pip install fpdf pandas openpyxl
  ```

## Usage  
1. Prepare your Excel file (`student_data.xlsx`) with columns: Name, Math, Science, English, Attendance  
2. Run the script:
   
   ```bash
   python automated_report_generation.py
   ```  
3. The report will be generated as `student_performance_report.pdf`  

## Example Excel Format  
| Name     | Math | Science | English | Attendance |
|----------|------|---------|---------|------------|
| Alice    | 85   | 92      | 88      | 95         |
| Bob      | 78   | 85      | 80      | 90         |
| Charlie  | 92   | 88      | 95      | 98         |
| Diana    | 80   | 75      | 82      | 85         |
| Ethan    | 88   | 90      | 92      | 94         |

## Output

The script generates `student_performance_report.pdf` containing:

* Summary section with average scores
* Top performers highlight
* Complete data table with all student records
* Professional formatting with alternating row colors

![image](https://github.com/user-attachments/assets/f7a2c3cf-d499-4a65-9f22-c7e46db37880)

## Customization

* Modify `col_widths` list to adjust table column sizes
* Change colors using `set_fill_color()`
* Add additional analysis metrics in `analyze_students()` function
* Update fonts and styling with `set_font()`

## License

* **This project**: [MIT License](LICENSE) - Free to use, modify, and distribute
