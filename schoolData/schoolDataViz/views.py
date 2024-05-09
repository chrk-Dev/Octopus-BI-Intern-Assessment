from django.shortcuts import render
from .utils import *



def index(req):
    return render(req, 'index.html')

def getSchoolData(req):
    tableHeaders=['Student ID','School Name']
    data = getSchool() 
    return render(req, 'schoolDataTable.html', {'data': data, 'tableHeaders': tableHeaders})


def getStudentData(req):
    tableHeaders=['Student ID','Student Name']
    data = getStudent() 
    return render(req, 'Student.html', {'data': data, 'tableHeaders': tableHeaders})


def getStudentClassData(req):
    tableHeaders=['Student ID','Student Class']
    data = getStudentClass() 
    return render(req, 'StudentClass.html', {'data': data, 'tableHeaders': tableHeaders})



def getAssessmentAreasData(req):
    tableHeaders=['Student ID','Assessment Areas']
    data = getAssessmentAreas() 
    return render(req, 'AssessmentAreas.html', {'data': data, 'tableHeaders': tableHeaders})

def getAnswersData(req):
    tableHeaders=['Student ID','Answers']
    data = getAnswers() 
    return render(req, 'AnswersData.html', {'data': data, 'tableHeaders': tableHeaders})


def getSummaryData(req):
    tableHeaders = [
        "School Name",
        "Sydney Participants",
        "Assessment Areas",
        "Award",
        "Class",
        "Correct Answer Percentage Per Class",
        "Correct Answers",
        "StudentID",
        "participant",
        "Student Score",
        "Subject",
        "Answers",
    ]
    data = getSummary() 
    return render(req, 'SummaryData.html', {'data': data, 'tableHeaders': tableHeaders})


def getAwardData(req):
    tableHeaders=['Student ID','Award']
    data = getAward() 
    return render(req, 'AwardData.html', {'data': data, 'tableHeaders': tableHeaders})

def getSubjectData(req):
    tableHeaders=['Student ID','Subject','Average Score']
    data = getSubject() 
    return render(req, 'SubjectData.html', {'data': data, 'tableHeaders': tableHeaders})