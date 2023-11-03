from dataorm import db, Puppy

db.create_all() #creates the database

sparky= Puppy('sparky', 'rotweirler', 24)
jacky= Puppy('Jacky', 'Sheep dog', 4)

print(sparky.id)
print(jacky.id)

db.session.add_all([sparky, jacky])
db.session.commit()
print(sparky.id)
print(jacky.id)
print(sparky)
print(jacky)