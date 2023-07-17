from django.db import connection
from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from datetime import date, datetime, timedelta
from secrets import choice

from dateutil.relativedelta import relativedelta

from . import models


# Create your views here.


def index(req: HttpRequest):
    # teacher = models.Teacher()
    # teacher.firstname = "Malathi"
    # teacher.surname = "Jeevan"
    # teacher.save()
    # teacher = models.Teacher()
    # teacher.firstname = "Aathira"
    # teacher.surname = "Gokul"
    # teacher.save()
    # teacher = models.Teacher()
    # teacher.firstname = "Inthumathi"
    # teacher.surname = "Varun"
    # teacher.save()
    # student = models.Student()
    # student.firstname = "Balaji"
    # student.surname = "Varun"
    # student.dateofbirth = date(2013, 6, 2)
    # student.classroom = 7
    # student.teacher = "Aathira Gokul"
    # student.save()
    # student = models.Student()
    # student.firstname = "Brindha"
    # student.surname = "Varun"
    # student.dateofbirth = date(2017, 6, 2)
    # student.classroom = 3
    # student.teacher = "Malathi Jeevan"
    # student.save()
    # student = models.Student()
    # student.firstname = "Meena"
    # student.surname = "Jeevan"
    # student.dateofbirth = date(2016, 6, 2)
    # student.classroom = 4
    # student.teacher = "Aathira Gokul"
    # student.save()
    # student = models.Student()
    # student.firstname = "Vennila"
    # student.surname = "Gokul"
    # student.dateofbirth = date(2018, 6, 2)
    # student.classroom = 2
    # student.teacher = "Inthumathi Varun"
    # student.save()
    return render(
        request=req,
        template_name="app_006/index.html",
        context={
            "web_page_title": "App 006",
        },
    )


def student_list(request: HttpRequest):
    # All Students
    students = models.Student.objects.all()
    print(students)
    query = students.query
    print()
    print(query)
    print()
    print(connection.queries)
    """

    Simple Or Query

    """
    student_list = models.Student.objects.filter(
        surname__startswith="Varun"
    ) | models.Student.objects.filter(surname__startswith="Jeevan")

    print(student_list)
    print()
    """

    Simple Or Query Using `Q`

    """
    student_list = models.Student.objects.filter(
        (Q(surname__startswith="Varun") | Q(surname__startswith="Jeevan"))
        & ~Q(classroom=3),
    )
    print()
    print(student_list)
    #
    print(" fetch some values only ")
    """

    All Students

    """
    students = models.Student.objects.all().values("firstname", "classroom")
    print("names, classrooms of students", students)
    print()
    students = models.Student.objects.all().values_list("firstname", "surname")
    print("firstnames, surnames of students", students)
    print()
    """

    Union Results

    """
    students = (
        models.Student.objects.all()
        .values_list("firstname", "surname")
        .union(models.Teacher.objects.all().values_list("firstname", "surname"))
    )
    print("firstnames, surnames of students, teachers as obj\n", students)
    print()
    students = (
        models.Student.objects.all()
        .values("firstname", "surname")
        .union(models.Teacher.objects.all().values("firstname", "surname"))
    )
    print("firstnames, surnames of students, teachers as dict\n ", students)
    print()
    query = students.query
    print()
    print(query)
    print()
    print(connection.queries)
    print()

    """
    Select individual fields
    """

    students = models.Student.objects.filter(Q(classroom=7)).only(
        "firstname", "surname"
    )
    print(students)
    print()
    #
    """
        Executing Custom Sql Queries Directly
    """

    cursor = connection.cursor()
    print()
    cursor.execute("select * from app_006_teacher limit 10")
    print(cursor.description, cursor.fetchall())
    print()
    cursor.execute("select count(*) from app_006_teacher limit 10")
    print(cursor.fetchall()[0][0], "Teachers teaching.")
    print()
    print(connection.queries)
    print()

    """--------------------------"""
    students = models.Student.objects.all()

    for stu in students:
        print(stu, stu.age())

    return render(
        request=request,
        template_name="app_006/student_list.html",
        context={
            "web_page_title": "App 006",
            "student_list": students,
        },
    )
