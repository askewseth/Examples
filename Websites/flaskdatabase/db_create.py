from app import db
from models import BlogPost

#create the database and the tables
db.create_all()

#insert
db.session.add(BlogPost("Good", "Im Good."))
db.session.add(BlogPost("Good", "Im Bad."))

#commit the changes
db.session.commit()
