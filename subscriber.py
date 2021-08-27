#!/usr/bin/env python
import pika

params = pika.URLParameters('amqp://LOGIN:PASSWORD@FQDN:PORT/%2fVHOST')
connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='test_queue')

def print_message(ch, method, properties, body):
    print(" Hello %r" % body)

channel.basic_consume(queue='test_queue', on_message_callback=print_message)

channel.start_consuming()

channel.close()
