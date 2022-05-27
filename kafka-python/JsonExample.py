import json
import logging
import threading
import time

from kafka import KafkaProducer, KafkaConsumer


class Producer(threading.Thread):
    daemon = True

    def run(self):
        topic = "test-topic"
        producer = KafkaProducer(bootstrap_servers='localhost:9092',
                                 value_serializer=lambda v: json.dumps(v).encode('utf-8'))
        while True:
            producer.send(topic, {"dataObjectID": "test1"})
            producer.send(topic, {"dataObjectID": "test2"})
            time.sleep(200)


class Consumer(threading.Thread):
    daemon = True

    def run(self):
        topic = "hive-meta"
        consumer = KafkaConsumer(bootstrap_servers='localhost:9092',
                                 auto_offset_reset='earliest',
                                 value_deserializer=lambda m: json.loads(m.decode('utf-8')))
        consumer.subscribe([topic])
        for message in consumer:
            print(message)


def main():
    threads = [
       # Producer(),
        Consumer()
    ]
    for t in threads:
        t.start()
    time.sleep(10)


if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:' +
               '%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO
    )
    main()
