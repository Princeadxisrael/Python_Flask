from dataorm import db, Puppy, app

db.create_all()

sparky= Puppy("Sparky", "Rotweiler", 16)
frank= Puppy("frank", "Rotweiler", 16)
print(sparky.id)
print(frank.id)
db.session.add_all([sparky, frank])
db.session.commit()
print(sparky.id)
print(frank.id)
print(sparky)
print(frank)