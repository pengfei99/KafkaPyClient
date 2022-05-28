from kafka import KafkaProducer

KAFKA_SERVER_URL = 'localhost:9092'
LOGIN = "alice"
PWD = "alice-secret"
TOPIC = "test-topic"


producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER_URL, security_protocol="SASL_PLAINTEXT",
                         sasl_mechanism='PLAIN', sasl_plain_username=LOGIN, sasl_plain_password=PWD)

for i in range(1000):
    producer.send(TOPIC, b'msg %d' % i)
    producer.flush()
