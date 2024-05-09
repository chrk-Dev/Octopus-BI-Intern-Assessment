import csv

csv_file_path = "sampledata/data.csv"

def fetchStudentIDAndName():
    result = []
    with open(csv_file_path, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  
        for row in csv_reader:
            student_id = row[2]
            student_name = f"{row[7]} {row[8]}"  
            result.append({"student_id": student_id, "student_name": student_name})
    return result

def fetchStudentIDAndClass():
    result = []
    with open(csv_file_path, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  
        for row in csv_reader:
            student_id = row[2]
            student_class = row[3]  
            result.append({"student_id": student_id, "student_class": student_class})
    return result

def fetchStudentIDAndAssessmentAreas():
    result = []
    with open(csv_file_path, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  
        for row in csv_reader:
            student_id = row[2]
            assessment_areas = row[23]  
            result.append({"student_id": student_id, "assessment_areas": assessment_areas})
    return result

def fetchStudentIDAndFirstNameLastName():
    result = []
    with open(csv_file_path, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  
        for row in csv_reader:
            student_id = row[2]
            first_name = row[7]  
            last_name = row[8]  
            result.append({"student_id": student_id, "first_name": first_name, "last_name": last_name})
    return result

def fetchStudentIDAndAnswers():
    result = []
    with open(csv_file_path, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  
        for row in csv_reader:
            student_id = row[2]
            answers = row[27]  
            result.append({"student_id": student_id, "answers": answers})
    return result

def fetchStudentIDAndAward():
    result = []
    with open(csv_file_path, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  
        for row in csv_reader:
            student_id = row[2]
            award = row[25]  
            result.append({"student_id": student_id, "award": award})
    return result

def fetchSubjectAndContents():
    result = []
    with open(csv_file_path, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader) 
        for row in csv_reader:
            subject = row[20]  
            contents = row[21]  
            result.append({"subject": subject, "contents": contents})
    return result

def fetchAverageScore():
    result = {}
    with open(csv_file_path, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  
        for row in csv_reader:
            subject = row[20]  
            score = float(row[24])  
            if subject in result:
                result[subject].append(score)
            else:
                result[subject] = [score]
    return result


print(fetchStudentIDAndName())
print(fetchStudentIDAndClass())
print(fetchStudentIDAndAssessmentAreas())
print(fetchStudentIDAndFirstNameLastName())
print(fetchStudentIDAndAnswers())
print(fetchStudentIDAndAward())