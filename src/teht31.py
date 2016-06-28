#!/usr/bin/python
#coding=UTF-8
class Student:
	def __init__(self,name,age,student_id):
		self.age=age;
		self.name=name;
		self.student_id=student_id;
		self.courses=[];
	def add_course(self,course_name):
		self.courses.append(course_name)
	def list_courses(self):
		return self.courses;

#joe = Student("Joe", 25, "f1234")
#josie = Student("Josie", 21, "f5678")
#
#print joe.list_courses()
#joe.add_course("script programming")
#print joe.list_courses()
#
#josie.add_course("network programming")
#josie.add_course("mathematics 2")
#
#print josie.list_courses()

