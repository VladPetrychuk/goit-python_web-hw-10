import json
from models import Author, Quote

# Завантаження авторів
def load_authors():
    with open("authors.json", "r", encoding="utf-8") as f:
        authors = json.load(f)
        for author in authors:
            if not Author.objects(fullname=author["fullname"]).first():
                Author(
                    fullname=author["fullname"],
                    born_date=author["born_date"],
                    born_location=author["born_location"],
                    description=author["description"],
                ).save()

# Завантаження цитат
def load_quotes():
    with open("quotes.json", "r", encoding="utf-8") as f:
        quotes = json.load(f)
        for quote in quotes:
            author = Author.objects(fullname=quote["author"]).first()
            if author:
                if not Quote.objects(quote=quote["quote"]).first():
                    Quote(
                        tags=quote["tags"],
                        author=author,
                        quote=quote["quote"]
                    ).save()

if __name__ == "__main__":
    load_authors()
    load_quotes()
    print("Дані успішно завантажено в базу даних!")