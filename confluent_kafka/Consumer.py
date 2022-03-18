import sys
from time import sleep

from confluent_kafka import Consumer, KafkaError, KafkaException


class ExampleConsumer:
    broker = "localhost:9092"
    topic = "test-topic"
    group_id = "consumer-1"

    def start_listener(self):
        consumer_config = {
            'bootstrap.servers': self.broker,
            'group.id': self.group_id,
            'auto.offset.reset': 'largest',
            'enable.auto.commit': 'false',
            'max.poll.interval.ms': '86400000'
        }

        consumer = Consumer(consumer_config)
        consumer.subscribe([self.topic])

        try:
            while True:
                print("Listening")
                # read single message at a time
                msg = consumer.poll(0)

                if msg is None:
                    sleep(5)
                    continue
                if msg.error():
                    print("Error reading message : {}".format(msg.error()))
                    continue
                # You can parse message and save to database here
                # all message is serialized in kafka (everything is in byte),
                # to get string, need to convert byte to string
                msg_value = msg.value().decode("utf-8")
                print(f"key: {msg.key()}, value: {msg_value}")
                consumer.commit()

        except Exception as ex:
            print("Kafka Exception : {}", ex)

        finally:
            print("closing consumer")
            consumer.close()


def main():
    ###################### Step 1 build a consumer ##################################
    """
    The group.id property is mandatory and specifies which consumer group the consumer is a member of.
    The auto.offset.reset property specifies what offset the consumer should start reading from in the event there
    are no committed offsets for a partition, or the committed offset is invalid (perhaps due to log truncation).

    """
    # conf = {'bootstrap.servers': "localhost:9092",
    #         'group.id': "foo",
    #         'auto.offset.reset': 'smallest'}
    #
    # consumer = Consumer(conf)
    ######################### Step2 start a consume poll loop ############################
    # RUNNING CONSUMER FOR READING MESSAGE FROM THE KAFKA TOPIC
    my_consumer = ExampleConsumer()
    my_consumer.start_listener()


if __name__ == "__main__":
    main()
