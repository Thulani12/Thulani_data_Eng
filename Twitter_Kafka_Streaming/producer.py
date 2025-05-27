from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers="localhost:9092", value_serializer=lambda v: json.dumps(v).encode("utf-8"))

for i in range(5):
    data = {"tweet": f"Sample tweet {i}"}
    producer.send("twitter-stream", data)
    print(f"Sent: {data}")
