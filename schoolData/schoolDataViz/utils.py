import csv

csv_file_path = "sampledata/data.csv"


def getSchool():
    result = []
    with open(csv_file_path, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader) 
        for row in csv_reader:
            student_id = row[2]
            school_name = row[0]  
            result.append({"student_id": student_id, "school_name": school_name})
    return result




def getStudent():
    result = []
    with open(csv_file_path, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader) 
        for row in csv_reader:
            student_id = row[2]
            first_name = row[3]
            last_name = row[4]
            student_name = first_name + " " + last_name
            result.append({"student_id": student_id, "student_name": student_name})
    return result

def getStudentClass():
    result = []
    with open(csv_file_path, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  
        for row in csv_reader:
            student_id = row[2]
            student_class = row[6] 
            result.append({"student_id": student_id, "student_class": student_class})
    return result


def getAssessmentAreas():
    result = []
    with open(csv_file_path, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  
        for row in csv_reader:
            student_id = row[2]
            assessment_areas = row[12]  
            result.append({"student_id": student_id, "assessment_areas": assessment_areas})
    return result


def getAnswers():
    result = []
    with open(csv_file_path, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  
        for row in csv_reader:
            student_id = row[2]  
            answers = row[8]  
            result.append({"StudentID": student_id, "Answers": answers})
    return result


def getSummary():
    result = []
    with open(csv_file_path, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  
        for row in csv_reader:
            school_name = row[0]  
            sydney_participants = row[15]  
            assessment_areas = row[12]  
            award = row[30]  
            student_class = row[6]  
            correct_answer_percentage = row[21]  
            correct_answers = row[9]  
            student_id = row[2]  
            participant = row[20]  
            student_score = row[16]  
            subject = row[7]  
            answers = row[8]  
            result.append({
                "school_name": school_name,
                "sydney_participants": sydney_participants,
                "assessment_areas": assessment_areas,
                "award": award,
                "Class": student_class,
                "correct_answer_percentage_per_class": correct_answer_percentage,
                "Correct_Answers": correct_answers,
                "StudentID": student_id,
                "participant": participant,
                "student_score": student_score,
                "Subject": subject,
                "Answers": answers
            })
    return result



def getAward():
    result = []
    with open(csv_file_path, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  
        for row in csv_reader:
            student_id = row[2]  
            award = row[30]  
            result.append({"StudentID": student_id, "Award": award})
    return result


def getSubject():
    result = []
    with open(csv_file_path, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  
        for row in csv_reader:
            student_id = row[2]  
            subject = row[7]  
            average_score = row[22]  
            result.append({"StudentID": student_id, "Subject": subject, "Average_Score": average_score})
    return result