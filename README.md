# Student Performance Tracker (Python)

#### Description:

A command-line based Python application to manage student records, calculate performance metrics, generate reports, and visualize individual student performance using graphs.

#### Features:

Add student records with multiple test marks
Automatically calculates average marks and assigns grades
View all stored student records
Visualize individual student performance trends using line graphs
Generate performance feedback reports
Persistent data storage using JSON file

#### Technologies Used:

Python 3
JSON
Matplotlib
OS module

#### Project Structure:

student.json
student_perfomance_tracker.py
README.md

#### How to Run:

--Clone the repository
git clone https://github.com/your-username/student-performance-tracker.git
--Navigate to the project directory
cd student-performance-tracker
--Install required library
pip install matplotlib
--Run the program
python student_tracker.py

#### Menu Options:

Add Student
View Records
Visualize Performance
Provide Report
Exit

#### Grading Criteria:

Average >= 90 → Grade A
Average >= 75 → Grade B
Average >= 60 → Grade C
Average < 60 → Fail

#### Visualization Details:

Line graph showing test-wise performance
X-axis: Test number
Y-axis: Marks (0 to 100)
Input Validation
Marks must be between 0 and 100
Prevents invalid data entry

#### Skills Demonstrated:

Python programming
File handling using JSON
Data validation
Data visualization using Matplotlib
Modular programming
Command-line application development

#### Future Enhancements:

Class-wise performance comparison
Export reports to CSV or PDF
GUI version using Tkinter
Student ranking system

