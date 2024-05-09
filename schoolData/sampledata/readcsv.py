import csv


csv_file_path = "data.csv"


with open(csv_file_path, "r") as file:
    csv_reader = csv.reader(file)
    
    next(csv_reader)
    
    for row in csv_reader:
        school_name = row[0]
        student_id = row[2]
        
        print("School Name:", school_name)
        print("Student ID:", student_id)
