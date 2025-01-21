import redis
from models import Quote, Author

# Налаштування Redis
redis_client = redis.StrictRedis(host="localhost", port=6379, db=0, decode_responses=True)

def search_by_author(name):
    cached_result = redis_client.get(f"author:{name}")
    if cached_result:
        print("Результат з кешу:")
        print(cached_result)
        return

    author = Author.objects(fullname__icontains=name).first()
    if not author:
        print(f"Автор {name} не знайдений.")
        return

    quotes = Quote.objects(author=author)
    result = "\n".join([q.quote for q in quotes])
    redis_client.set(f"author:{name}", result, ex=3600)  # Кешуємо на 1 годину
    print(result)

def search_by_tag(tag):
    cached_result = redis_client.get(f"tag:{tag}")
    if cached_result:
        print("Результат з кешу:")
        print(cached_result)
        return

    quotes = Quote.objects(tags__icontains=tag)
    result = "\n".join([q.quote for q in quotes])
    redis_client.set(f"tag:{tag}", result, ex=3600)  # Кешуємо на 1 годину
    print(result)

def search_by_tags(tags):
    tags_list = tags.split(",")
    quotes = Quote.objects(tags__in=tags_list)
    result = "\n".join([q.quote for q in quotes])
    print(result)

def main():
    print("Починаємо пошук цитат. Введіть команду:")
    while True:
        command = input("> ")
        if command.startswith("name:"):
            name = command.split("name:")[1].strip()
            search_by_author(name)
        elif command.startswith("tag:"):
            tag = command.split("tag:")[1].strip()
            search_by_tag(tag)
        elif command.startswith("tags:"):
            tags = command.split("tags:")[1].strip()
            search_by_tags(tags)
        elif command == "exit":
            print("Вихід із програми.")
            break
        else:
            print("Невідома команда. Спробуйте ще раз.")

if __name__ == "__main__":
    main()