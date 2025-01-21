import pika
from faker import Faker
from models import Contact

# Ініціалізація Faker
faker = Faker()

# Підключення до RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

# Створення черги
channel.queue_declare(queue="email_queue")

# Генерація контактів і публікація в RabbitMQ
def generate_contacts(count=10):
    for _ in range(count):
        contact = Contact(
            fullname=faker.name(),
            email=faker.email()
        )
        contact.save()  # Зберігаємо контакт у базі даних

        # Відправляємо ID контакту в RabbitMQ
        channel.basic_publish(
            exchange="",
            routing_key="email_queue",
            body=str(contact.id)
        )
        print(f"Відправлено контакт {contact.fullname} ({contact.email}) до черги.")

if __name__ == "__main__":
    generate_contacts(10)  # Генерація 10 контактів
    connection.close()