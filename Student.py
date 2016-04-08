# coding:UTF-8
class Student:
	studentCount = 0
	__count = 0;
	def __init__(self, name,address):
		self.name = name
		self.address = address
		Student.studentCount += 1
		self.__count += 1;
	
	def displayTotalCount(self):
		print '该类总共有%d个实例' % Student.studentCount

	def displayStudent(self):
		print "name = ",self.name,";address = ",self.address

	def displaySelf(self):
		print "parent function"

	def __str__(self):
		return "value of name = %s ,address = %s" % (self.name,self.address)

	def __add__(self,other):
		return "two instance add togeter"
			
	def __del__(self):
		print "该对象被销毁了"

# stu1 = Student("stu1","http://www.baidu.com")
# stu1.displayStudent()		

def displaySomething():
	print "displaySomething"


class StudentLike(Student):
	"""docstring for StudentLike"""
	def __init__(self,like):
		self.like = like

	def displaySelf(self):
		print "child function"	