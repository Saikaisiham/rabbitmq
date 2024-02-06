import pika 

def on_message_recieved(ch, method, properties, body):
    print(f'recieved new message: {body}')


#create connection 
connection_parameters = pika.ConnectionParameters('localhost')

#create a connection to rabbitmq broker
connection = pika.BlockingConnection(connection_parameters) 


# create channel
channel = connection.channel()


channel.queue_declare(queue='letterbox')


channel.basic_consume(queue='letterbox', auto_ack=True, 
                      on_message_callback=on_message_recieved)


print('Starting Consuming')

channel.start_consuming()

