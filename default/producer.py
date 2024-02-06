import pika


#create connection 
connection_parameters = pika.ConnectionParameters('localhost')

#create a connection to rabbitmq broker
connection = pika.BlockingConnection(connection_parameters) 


# create channel
channel = connection.channel()


channel.queue_declare(queue='letterbox')

message = 'Hello this is my first message'

#default exchange 
channel.basic_publish(exchange='', routing_key='letterbox', body=message)


print(f'sent message: {message}')

connection.close()