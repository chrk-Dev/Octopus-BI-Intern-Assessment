from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("schooldata/", views.getSchoolData, name="getSchoolData"),
    path("StudentData/", views.getStudentData, name="getStudentData"),
    path("StudentClassData/", views.getStudentClassData, name="getStudentClassData"),
    path("AssessmentAreasData/", views.getAssessmentAreasData, name="getAssessmentAreasData"),
    path("SummaryData/", views.getSummaryData, name="getSummaryData"),
    path("AwardData/", views.getAwardData, name="getAwardData"),
    path("SubjectData/", views.getSubjectData, name="getSubjectData"),
    path("AnswersData/", views.getAnswersData, name="getAnswersData"),
]
