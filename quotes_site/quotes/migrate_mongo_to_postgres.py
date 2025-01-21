from quotes.models_mongo import Author as MongoAuthor, Quote as MongoQuote
from quotes.models import Author as PostgresAuthor, Quote as PostgresQuote

def migrate_authors():
    mongo_authors = MongoAuthor.objects.all()
    for author in mongo_authors:
        # Створюємо автора в PostgreSQL
        postgres_author = PostgresAuthor(
            fullname=author.fullname,
            born_date=author.born_date,
            born_location=author.born_location,
            description=author.description
        )
        postgres_author.save()

def migrate_quotes():
    mongo_quotes = MongoQuote.objects.all()
    for quote in mongo_quotes:
        # Знаходимо автора у PostgreSQL
        try:
            postgres_author = PostgresAuthor.objects.get(fullname=quote.author.fullname)
        except PostgresAuthor.DoesNotExist:
            continue

        # Створюємо цитату в PostgreSQL
        postgres_quote = PostgresQuote(
            text=quote.quote,
            author=postgres_author,
            tags=','.join(quote.tags)  # Об'єднуємо теги в строку
        )
        postgres_quote.save()

if __name__ == '__main__':
    migrate_authors()
    migrate_quotes()
    print("Міграція даних завершена.")