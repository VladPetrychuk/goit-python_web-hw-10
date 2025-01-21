from mongoengine import Document, StringField, ReferenceField, ListField, BooleanField, EmailField, connect

# Підключення до MongoDB
connect(db="email_system", host="mongodb+srv://dbuser:2KocWCKPaVTi5vzI@cluster0.pmbcv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

class Author(Document):
    fullname = StringField(required=True, unique=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()

class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author, required=True)
    quote = StringField(required=True)

class Contact(Document):
    fullname = StringField(required=True)
    email = EmailField(required=True, unique=True)
    is_sent = BooleanField(default=False)