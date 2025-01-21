import pika
from models import Contact

# Підключення до RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

# Створення черги
channel.queue_declare(queue="email_queue")

# Імітація надсилання email
def send_email(contact):
    print(f"Надсилаємо email до {contact.fullname} ({contact.email})...")
    contact.is_sent = True
    contact.save()  # Оновлюємо статус у базі даних
    print(f"Email надіслано контакту {contact.fullname}.")

# Функція обробки повідомлення
def callback(ch, method, properties, body):
    contact_id = body.decode("utf-8")
    contact = Contact.objects(id=contact_id).first()
    if contact:
        send_email(contact)
    else:
        print(f"Контакт із ID {contact_id} не знайдено.")

# Перевірка черги перед початком обробки
def consume_messages():
    print("Очікуємо повідомлень...")
    while True:
        method_frame, header_frame, body = channel.basic_get(queue="email_queue", auto_ack=True)
        if body:
            callback(None, method_frame, header_frame, body)
        else:
            print("Черга порожня. Завершуємо роботу.")
            break

if __name__ == "__main__":
    consume_messages()
    connection.close()