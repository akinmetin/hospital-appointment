import pika
import pymongo
from decouple import config
import datetime

credentials = pika.PlainCredentials('rabbitmq_root', 'rabbitmquser_pw')
parameters = pika.ConnectionParameters("rabbitmq", 5672, "/", credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue="doctor_queue_prio",
                      arguments={'x-max-priority': 10})

# db connection
client = pymongo.MongoClient(host=config("DB_HOST"),
                             port=int(config("DB_PORT")),
                             username=config("DB_USER"),
                             password=config("DB_PASSWORD"),
                             authSource="admin")
db = client["patients-db"]
col = db["patients"]


# global bulk list for sending 50 entries in 1 query to reduce connections.
bulk = []


# insert bulk data into database
def insert_data(bulk_data):
    col.insert_many(bulk_data)


def add_into_bulk(disease):
    # create a temporary dictionary variable
    temp_dict = {}

    # use global "bulk" list variable
    global bulk

    if len(bulk) < 50:
        # use timestamp for appointment time
        timestamp = datetime.datetime.now().timestamp()

        '''add unique patient id, current timestamp
        and disease into temporary dictionary
        '''
        temp_dict["time"] = timestamp
        temp_dict["disease"] = disease
        bulk.append(temp_dict)
    else:
        '''
        when "bulk" has 50 elements in it, insert elements into db
        then, reset the content of "bulk" and add current data
        as the a element
        '''
        insert_data(bulk)
        bulk = []
        add_into_bulk(disease)


# Subscribe to callback function to a queue.
def callback(ch, method, properties, body):
    # decode body to remove b' letter and symbol
    message = body.decode()

    # add patient disease info into db
    if "bleeding" in message:
        add_into_bulk("emergency")
    elif "heart" in message:
        add_into_bulk("cardiology")
    else:
        add_into_bulk("esthetic")

    print(" [x] Patient received {}".format(message))


channel.basic_consume(queue='doctor_queue_prio',
                      auto_ack=True,
                      on_message_callback=callback)

channel.start_consuming()
