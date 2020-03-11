import pika
import pymongo
from decouple import config

credentials = pika.PlainCredentials('rabbitmq_root', 'rabbitmquser_pw')
parameters = pika.ConnectionParameters("rabbitmq", 5672, "/", credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue="doctor_queue_prio",
                      arguments={'x-max-priority': 10})


def db_login():
    myclient = pymongo.MongoClient("db",
                                   username=config("DB_USER"),
                                   password=config("DB_PASSWORD"),
                                   authSource="patients_db",
                                   authMechanism="SCRAM-SHA-256")
    return myclient


def db_check_or_create():
    myclient = db_login()
    dblist = myclient.list_database_names()
    if "patients_db" in dblist:
        print("DB exists.")
    else:
        mydb = myclient["mydatabase"]
        mycol = mydb["patients"]
        print("DB created.")


# Subscribe to callback function to a queue.
def callback(ch, method, properties, body):
    # decode body to remove b' letter and symbol
    message = body.decode()
    print(" [x] Patient received {}".format(message))


channel.basic_consume(queue='doctor_queue_prio',
                      auto_ack=True,
                      on_message_callback=callback)


channel.start_consuming()
