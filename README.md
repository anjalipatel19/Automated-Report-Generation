# Automated-Report-Generation
Python script that automatically generates professional PDF performance reports from Excel student data, complete with statistical analysis and formatted tables.
Here's a customized README for your Student Performance Report project following the same structure:

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

* **Excel Integration**: Reads data directly from Excel files (.xlsx format)
* **Data Analysis**:
  * Calculates subject averages (Math, Science, English)
  * Computes overall attendance percentage
  * Identifies top performers in each subject
* **PDF Report Generation**:
  * Summary statistics section
  * Top performers highlight
  * Clean data table with alternating row colors
* **Professional Styling**:
  * Consistent font styling
  * Proper section spacing
  * Clear headers and labels

## Technical Details

* **Python Libraries Used**:
  * `pandas` for Excel data handling
  * `fpdf` for PDF generation
* **Configuration**:
  * Works with standard Excel files (Sheet1 by default)
  * Adjustable column widths and styling
* **Output**:
  

## Setup Instructions

1. Ensure Python 3.x is installed
2. Install required packages:
   ```bash
   pip install fpdf pandas openpyxl
   ```
3. Prepare your Excel file with columns: Name, Math, Science, English, Attendance
4. Run the script:
   ```bash
   python excel_to_pdf_report.py
   ```

## Sample Output

The script generates `student_performance_report.pdf` containing:

* Summary section with average scores
* Top performers highlight
* Complete data table with all student records
* Professional formatting with alternating row colors

## Customization Options

* Modify `col_widths` list to adjust table column sizes
* Change colors using `set_fill_color()`
* Add additional analysis metrics in `analyze_students()` function
* Update fonts and styling with `set_font()`

## File Structure

```
project_folder/
├── student_data.xlsx      # Input Excel file
├── excel_to_pdf_report.py # Main script
└── student_performance_report.pdf  # Generated output
```

## License

* **This project**: [MIT License](LICENSE) - Free to use, modify, and distribute
