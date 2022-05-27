from confluent_kafka import Producer
KAFKA_PRODUCER_CONFIGURATION = {
    'bootstrap.servers': 'localhost:9092',
    'security.protocol' : 'SASL_PLAINTEXT',
    'sasl.username': 'alice',
    'sasl.password': 'alice-secret',
    'sasl.mechanism':'PLAIN'
}
producer = Producer(KAFKA_PRODUCER_CONFIGURATION)

for i in range(10):
    producer.produce("test-topic", f"msg:{i}")
    producer.flush()