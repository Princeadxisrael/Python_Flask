from students import db, Students

db.create_all()

sam=Students("Samuel", "Lagos", "Yaba", 1234)
esther=Students("Esther", "Lagos", "Surulere", 2234)

db.session.add_all([sam, esther]) #creating a data
db.session.commit()