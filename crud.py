from students import db, Students

#CREATE
owen=Students("Owen", "Portharcourt", "Rumigbo", 2211)
chike=Students("Chike", "Portharcourt", "Ikwerre", 2211)
george=Students("George", "lagos", "Yaba", 2211)
db.session.add_all([owen, chike, george])
db.session.commit()

#READ
# all_students=Students.query.all()
# db.session.delete(all_students)
# print(all_students)

# first_student= Students.query.get(2)
# print(first_student)

# students_in_yaba= Students.query.filter_by(addr="Yaba").delete()
# db.session.commit()


#UPDATE
# third_student=Students.query.get(3)
# fourth_student=Students.query.get(4)
# # third_student.name="Jude"
# # fourth_student.name="Jessica"
# # # db.session.add_all([third_student, fourth_student])
# # db.session.commit()

# #DELETE
# db.session.delete(third_student)
# db.session.query(Students).delete()
# db.session.commit()