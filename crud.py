from student import db, Students

##CREATE
# Jessica= Students("Jessica", "Lagos","Yaba" ,1234)
# Putin= Students("Putin", "Russia","Russian", 2234)

# db.session.add_all([Jessica, Putin])
# db.session.commit()

##READ
# all_students= Students.query.all()
# print(all_students)

# fifth_student=Students.query.get(5)
# print(fifth_student)

# students_in_yaba=Students.query.filter_by(addr="Yaba")
# print(students_in_yaba.all())

##Update

##DELETE
db.session.query(Students).filter_by(name="Jessica")