import pandas as pd
from fpdf import FPDF

# Step 1: Read data from Excel file
def read_student_data(filename):
    try:
        # Read the Excel file
        df = pd.read_excel(filename, sheet_name='Sheet1')
        # Convert to list of dictionaries (one per student)
        students = df.to_dict('records')
        return students
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return []

# Step 2: Analyze the data
def analyze_students(students):
    if not students:
        return {}
    
    analysis = {
        'total_students': len(students),
        'math_avg': sum(float(s['Math']) for s in students) / len(students),
        'science_avg': sum(float(s['Science']) for s in students) / len(students),
        'english_avg': sum(float(s['English']) for s in students) / len(students),
        'attendance_avg': sum(float(s['Attendance']) for s in students) / len(students),
        'top_student': max(students, key=lambda s: (float(s['Math']) + float(s['Science']) + float(s['English']))),
        'best_math': max(students, key=lambda s: float(s['Math'])),
        'best_attendance': max(students, key=lambda s: float(s['Attendance'])),
    }
    return analysis

# Step 3: Create PDF report
def create_report(students, analysis):
    pdf = FPDF()
    pdf.add_page()
    
    # Set font for title
    pdf.set_font("Arial", size=16, style='B')
    pdf.cell(200, 10, txt="Student Performance Report", ln=1, align='C')
    pdf.ln(10)
    
    # Report summary
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Total Students: {analysis['total_students']}", ln=1)
    pdf.cell(200, 10, txt=f"Math Average: {analysis['math_avg']:.1f}%", ln=1)
    pdf.cell(200, 10, txt=f"Science Average: {analysis['science_avg']:.1f}%", ln=1)
    pdf.cell(200, 10, txt=f"English Average: {analysis['english_avg']:.1f}%", ln=1)
    pdf.cell(200, 10, txt=f"Attendance Average: {analysis['attendance_avg']:.1f}%", ln=1)
    pdf.ln(10)
    
    # Top performers
    pdf.set_font("Arial", size=12, style='B')
    pdf.cell(200, 10, txt="Top Performers:", ln=1)
    pdf.set_font("Arial", size=12)
    
    top = analysis['top_student']
    pdf.cell(200, 10, txt=f"Overall Best: {top['Name']} (Score: {float(top['Math'])+float(top['Science'])+float(top['English']):.1f})", ln=1)
    
    math = analysis['best_math']
    pdf.cell(200, 10, txt=f"Best in Math: {math['Name']} ({math['Math']}%)", ln=1)
    
    attend = analysis['best_attendance']
    pdf.cell(200, 10, txt=f"Best Attendance: {attend['Name']} ({attend['Attendance']}%)", ln=1)
    pdf.ln(10)
    
    # Student details table
    pdf.set_font("Arial", size=12, style='B')
    pdf.cell(200, 10, txt="Student Details:", ln=1)
    
    # Table header
    pdf.set_fill_color(200, 220, 255)  # Light blue background
    col_widths = [40, 25, 25, 25, 30]
    headers = ["Name", "Math", "Science", "English", "Attendance"]
    
    for i, header in enumerate(headers):
        pdf.cell(col_widths[i], 10, txt=header, border=1, fill=True)
    pdf.ln()
    
    # Table rows
    pdf.set_font("Arial", size=10)
    fill = False  # Alternate row colors
    for student in students:
        for i, field in enumerate(headers):
            pdf.cell(col_widths[i], 10, txt=str(student[field]), border=1, fill=fill)
        pdf.ln()
        fill = not fill  # Alternate the fill
    
    # Save the PDF
    pdf.output("student_performance_report.pdf")
    print("Report generated as 'student_performance_report.pdf'")

# Main program
def main():
    # Read the data
    students = read_student_data("student_data.xlsx")
    
    if not students:
        print("No student data found. Please check your Excel file.")
        return
    
    # Analyze the data
    analysis = analyze_students(students)
    
    # Generate the report
    create_report(students, analysis)

if __name__ == "__main__":
    main()