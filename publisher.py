#!/usr/bin/env python
import pika

params = pika.URLParameters('amqp://LOGIN:PASSWORD@FQDN:PORT/%2fVHOST')
connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='test_queue')

channel.basic_publish(exchange='test_pika', routing_key='test_pika', body='pikapika')

connection.close()
