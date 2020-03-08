import pika

credentials = pika.PlainCredentials('rabbitmq_root', 'rabbitmquser_pw')
parameters = pika.ConnectionParameters("rabbitmq", 5672, "/", credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue="doctor_queue_prio",
                      arguments={'x-max-priority': 10})


# Subscribe to callback function to a queue.
def callback(ch, method, properties, body):
    # decode body to remove b' letter and symbol
    message = body.decode()
    print(" [x] Patient received {}".format(message))


channel.basic_consume(queue='doctor_queue_prio',
                      auto_ack=True,
                      on_message_callback=callback)


channel.start_consuming()
