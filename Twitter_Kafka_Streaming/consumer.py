from kafka import KafkaConsumer
import json

consumer = KafkaConsumer("twitter-stream", bootstrap_servers="localhost:9092", value_deserializer=lambda v: json.loads(v.decode("utf-8")))

for message in consumer:
    print(f"Received: {message.value}")
