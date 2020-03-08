import pika
import random

credentials = pika.PlainCredentials('rabbitmq_root', 'rabbitmquser_pw')
parameters = pika.ConnectionParameters("rabbitmq", 5672, "/", credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue="doctor_queue_prio", arguments={'x-max-priority': 10})


def emergency():
    channel.basic_publish(exchange="",
                          routing_key="doctor_queue_prio",
                          body="I have bleeding!",
                          properties=pika.BasicProperties(priority=9))
    print("Patient with an emergency entered to doctor's room!")


def cardiology():
    channel.basic_publish(exchange="",
                          routing_key="doctor_queue_prio",
                          body="I'm having a heart attack!",
                          properties=pika.BasicProperties(priority=3))
    print("Patient with an cardiology problem entered to doctor's room!")


def esthetic():
    channel.basic_publish(exchange="",
                          routing_key="doctor_queue_prio",
                          body="I need a plastic surgery!")
    print("Patient with an esthetic problem entered to doctor's room!")


# Run 10 times queuing
for x in range(0, 10):
    # Everytime 10 patients enter into the hospital
    # Consider queue line for 3 emergency, 5 cardiology and 2 esthetic patients
    patient_queue = [0, 0, 0, 1, 1, 1, 1, 1, 2, 2]

    # Shuffle patient_queue
    random.shuffle(patient_queue)

    # Call the patients inside the doctor's room by queue number
    for patient in patient_queue:
        if patient == 0:
            emergency()
        elif patient == 1:
            cardiology()
        else:
            esthetic()

connection.close(reply_text="End of the patients")
